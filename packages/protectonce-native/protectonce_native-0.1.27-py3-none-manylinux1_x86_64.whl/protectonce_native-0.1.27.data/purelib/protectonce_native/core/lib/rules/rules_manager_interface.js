const RulesManager = require('./rules_manager');
const Constants = require('../utils/constants');
const HeartbeatCache = require('../reports/heartbeat_cache');
const Logger = require('../utils/logger');
const _ = require('lodash');

function getRuntimeRules(data) {
    const resp = {};
    try {
        RulesManager.handleIncomingRules(data.data);
        const rules = RulesManager.runtimeRules;
        const appDeleted = RulesManager.isAppDeleted();
        const features = RulesManager.features
        resp['hooks'] = rules;
        resp['appDeleted'] = appDeleted;
        resp['features'] = features;
        resp['syncInterval'] = RulesManager.getSyncInterval();
        return resp;
    } catch (e) {
        Logger.write(Logger.DEBUG && `rules.getRuntimeRules: Failed error: ${e}`);
    }
    return {};
}

function getHeartbeatInfo(data) {
    try {
        const heartbeatInfo = {};
        heartbeatInfo[Constants.HEARTBEAT_HASH_KEY] = RulesManager.hash;
        const { agentId, workLoadId, requestSchemaData, apiRequestData, incidents, userActivities, inventory, dynamicBom } = HeartbeatCache.flush();
        heartbeatInfo[Constants.HEARTBEAT_API_REQUEST_DATA_KEY] = apiRequestData;
        heartbeatInfo[Constants.HEARTBEAT_INVENTORY_KEY] = inventory;
        heartbeatInfo[Constants.HEARTBEAT_INCIDENTS_KEY] = incidents;
        heartbeatInfo[Constants.HEARTBEAT_REQUEST_SCHEMA_DATA_KEY] = requestSchemaData;
        heartbeatInfo[Constants.HEARTBEAT_USER_ACTIVITIES_KEY] = userActivities;
        heartbeatInfo[Constants.HEARTBEAT_WORKLOADID_KEY] = workLoadId;
        heartbeatInfo[Constants.HEARTBEAT_AGENTID_KEY] = agentId;
        heartbeatInfo[Constants.HEARTBEAT_DYNAMIC_BOM_KEY] = dynamicBom;
        return heartbeatInfo;
    } catch (e) {
        Logger.write(Logger.DEBUG && `rules.getHeartbeatInfo: Failed error: ${e}`);
    }
    return {}
}
// forcefully setClosed for an ongoing request 
// so that incidents will be reported immediately on next heartbeat
function closeRequest(data) {
    try {
        HeartbeatCache.setClosed(data.data);
    } catch (error) {
        Logger.write(Logger.DEBUG && `rules.closeRequest: Failed error: ${e}`);
    }
    return;
}

function storeWorkloadId(data) {
    try {
        if (_.isObject(data) && _.isString(data.data)) {
            HeartbeatCache.cacheWorkloadId(data.data);
        }
    } catch (error) {
        Logger.write(Logger.DEBUG && `rules.storeWorkloadId: Failed with error: ${error}`);
    }
}

module.exports = {
    getRuntimeRules: getRuntimeRules,
    getHeartbeatInfo: getHeartbeatInfo,
    closeRequest: closeRequest,
    storeWorkloadId: storeWorkloadId
}