const { UserActivity } = require('../../reports/user_activity');
const HeartbeatCache = require('../../reports/heartbeat_cache');
const Logger = require('../../utils/logger');
const userManager = require('./user_manager');
const ProtectOnceContext = require('../context');
const { ReportType } = require('../../reports/report');
const PlaybooksManager = require('../playbooks/playbooks_manager');
const Constants = require('../../utils/constants');
require('../../utils/common_utils');
const _ = require('lodash');
const { EventType } = require('../../utils/event_type');
const SUCCESS = 'success', FAILURE = 'failure';

/* This method creates securityActivity object for signUp data of user
* It adds signup event in Event object inside SecurityActivity object 
* It also returns action object with values (allow and block) based 
  on userName passed is in blocked user list
* @param  {Object} signUpData - signUp data received as input
*          @param {Object} data This holds actual signup data
*              @param {String} poSessionId
*              @param {String} userName
*/
function storeSignUpData(signUpData) {
    try {
        const poSessionId = signUpData.data.poSessionId;
        const userName = signUpData.data.userName;
        const result = PlaybooksManager.checkIfBlockedByUser(userName);
        Logger.write(Logger.DEBUG && `calling storeSignUpData with userName : ${userName}`);
        _cacheUserActivity(poSessionId, createUser(userName), EventType.EVENT_TYPE_SIGNUP, result);
        return {
            result
        };
    } catch (e) {
        Logger.write(Logger.DEBUG && `Failed calling storeSignUpData with error : ${e}`);
        return { "result": { "action": ReportType.REPORT_TYPE_NONE } };
    }
}

function createUser(userName) {
    return {
        "identifier": userName
    }
}

/* This method creates securityActivity object for login data of user
* It adds login event in Event object inside SecurityActivity object 
* It also returns action object with values (allow and block) based 
  on userName passed is in blocked user list
* @param  {Object} loginData - loginData received as input
*          @param {Object} data This holds actual login data
*              @param {String} poSessionId
*              @param {String} success
*              @param {String} userName
*/
function storeLoginData(loginData) {
    try {
        const poSessionId = loginData.data.poSessionId;
        const success = loginData.data.success;
        const userName = loginData.data.userName;

        const result = PlaybooksManager.checkIfBlockedByUser(userName);
        Logger.write(Logger.DEBUG && `calling storeLoginData with status : ${success} ` && `userName : ${userName}`);
        _cacheUserActivity(poSessionId, createUser(userName), EventType.EVENT_TYPE_LOGIN, result, success);
        return { result };
    } catch (e) {
        Logger.write(Logger.DEBUG && `Failed calling storeLoginData with error : ${e}`);
        return { "result": { "action": ReportType.REPORT_TYPE_NONE } };
    }
}

function populateEventAttributes(context, action, status) {
    const requestContentTypeHeader = getContentTypeHeader(context.requestHeaders);
    const responseContentTypeHeader = getContentTypeHeader(context.responseHeaders);
    const responseStatus = getResponseStatus(context, action, status);

    return {
        [Constants.BLOCKED_KEY]: action === ReportType.REPORT_TYPE_BLOCK,
        [Constants.APPLICATION_ENV_KEY]: PlaybooksManager.environment,
        [Constants.REQUEST_HEADERS_CONTENT_TYPE_KEY]: requestContentTypeHeader,
        [Constants.RESPONSE_HEADERS_CONTENT_TYPE_KEY]: responseContentTypeHeader,
        [Constants.RESPONSE_STATUS_KEY]: responseStatus
    };
}

function getContentTypeHeader(headers) {
    return headers && _.getObjectKeysToLower(headers, 'content-type');
}

function getResponseStatus(context, action, status) {
    if (status) {
        return SUCCESS;
    }

    if ([ReportType.REPORT_TYPE_BLOCK, ReportType.REPORT_TYPE_REDIRECT].includes(action)) {
        return FAILURE;
    }
    if (context.statusCode) {
        return isSuccessStatusCode(context.statusCode) ? SUCCESS : FAILURE;
    }

    return SUCCESS;
}

function isSuccessStatusCode(statusCode) {
    return statusCode >= 200 && statusCode <= 399 && statusCode !== 302;
}

function getAction(userName) {
    return userManager.isUserInBlockedList(userName) ? ReportType.REPORT_TYPE_BLOCK : ReportType.REPORT_TYPE_NONE;
}


function _cacheUserActivity(poSessionId, user, eventType, result, status) {
    const context = ProtectOnceContext.get(poSessionId);
    status = status ? SUCCESS : getResponseStatus(context, result.action);
    const userActivity = new UserActivity();
    userActivity.requestId = poSessionId;
    userActivity.category = eventType;
    userActivity.action = result.action;
    userActivity.status = status;
    userActivity.redirectUrl = result.redirectUrl;
    userActivity.userInfo = user;
    userActivity.statusCode = context.statusCode;
    userActivity.requestPath = context.requestPath;
    userActivity.requestVerb = context.method;
    userActivity.ipAddress = context.sourceIP;
    userActivity.protocol = context.protocol;
    userActivity.eventAttributes = populateEventAttributes(context, result.action, status);
    HeartbeatCache.cacheUserActivity(userActivity);
}

/*This method creates securityActivity object for user details 
* It adds user object inside securityActivity object with identifier as key and 
* userName as value
* It also returns action object with values (allow and block) based 
  on userName passed is in blocked user list
* @param  {Object} identifyData - identifyData received as input
*          @param {Object} data This holds actual user data
*              @param {String} poSessionId
*              @param {String} userName
*/
function identify(identifyData) {
    try {
        const poSessionId = identifyData.data.poSessionId;
        const userName = identifyData.data.userName;
        const result = PlaybooksManager.checkIfBlockedByUser(userName);
        if ([ReportType.REPORT_TYPE_BLOCK, ReportType.REPORT_TYPE_REDIRECT].includes(result.action)) {
            _cacheUserActivity(poSessionId, createUser(userName), EventType.EVENT_TYPE_AUTH, result);
        }
        return { result };
    } catch (e) {
        Logger.write(Logger.DEBUG && `Failed calling identify with error : ${e}`);
        return { "result": { "action": ReportType.REPORT_TYPE_NONE } };
    }
}

function checkIfBlocked(userData) {
    try {
        const poSessionId = userData.data.poSessionId;
        const userName = userData.data.userName;
        const result = { "action": getAction(userName) };
        if (result.action === ReportType.REPORT_TYPE_BLOCK) {
            _cacheUserActivity(poSessionId, createUser(userName), EventType.EVENT_TYPE_USER_MONITORING, result);
        }
        return { result };
    }
    catch (e) {
        Logger.write(Logger.DEBUG && `Failed calling checkIfBlocked with error : ${e}`);
    }
    return { "result": { "action": ReportType.REPORT_TYPE_NONE } };
}

module.exports = {
    checkIfBlocked: checkIfBlocked,
    storeSignUpData: storeSignUpData,
    storeLoginData: storeLoginData,
    identify: identify
}

