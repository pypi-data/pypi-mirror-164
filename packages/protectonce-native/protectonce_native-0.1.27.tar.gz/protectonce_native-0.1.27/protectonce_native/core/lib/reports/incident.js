const _ = require('lodash');

//Occurrence of the waf or rasp incident will be stored inside the Incident object along with metadata related to the incident.
class Incident {
  constructor() {
    this._category = undefined;
    this._requestId = undefined;
    this._action = undefined;
    this._confidenceLevel = undefined;
    this._ruleId = undefined;
    this._type = undefined;
    this._stackTrace = undefined;
    this._redirectUrl = undefined;
    this._statusCode = undefined;
    this._requestPath = undefined;
    this._requestVerb = undefined;
    this._ipAddress = undefined;
    this._date = new Date();
    this._protocol = undefined;
    this._poRequestId = undefined;
    this._trigger = undefined;
    this._outgoingUrls = undefined;
    this._raspDetails = undefined;
    this._wafDetails = undefined;
    this._userInfo = undefined;
    this._host = undefined;
  }

  set category(category) {
    if (_.isString(category)) {
      this._category = category;
    }
  }

  set requestId(requestId) {
    if (_.isString(requestId)) {
      this._requestId = requestId;
    }
  }

  set type(type) {
    if (_.isString(type)) {
      this._type = type;
    }
  }

  set action(action) {
    if (_.isString(action)) {
      this._action = action;
    }
  }

  set confidenceLevel(confidenceLevel) {
    if (confidenceLevel) {
      this._confidenceLevel = confidenceLevel;
    }
  }

  set ruleId(ruleId) {
    if (_.isString(ruleId)) {
      this._ruleId = ruleId;
    }
  }

  set stackTrace(stackTrace) {
    if (_.isArray(stackTrace) && !_.isEmpty(stackTrace)) {
      this._stackTrace = stackTrace;
    }
  }

  set redirectUrl(redirectUrl) {
    if (_.isString(redirectUrl)) {
      this._redirectUrl = redirectUrl;
    }
  }

  set statusCode(statusCode) {
    if (statusCode) {
      this._statusCode = statusCode;
    }
  }

  set requestPath(requestPath) {
    if (_.isString(requestPath)) {
      this._requestPath = requestPath;
    }
  }

  set requestVerb(requestVerb) {
    if (_.isString(requestVerb)) {
      this._requestVerb = requestVerb;
    }
  }

  set ipAddress(ipAddress) {
    if (_.isString(ipAddress)) {
      this._ipAddress = ipAddress;
    }
  }

  set date(date) {
    if (_.isDate(date)) {
      this._date = date;
    }
  }

  set protocol(protocol) {
    if (_.isString(protocol)) {
      this._protocol = protocol;
    }
  }

  set poRequestId(poRequestId) {
    if (_.isString(poRequestId)) {
      this._poRequestId = poRequestId;
    }
  }

  set trigger(trigger) {
    if (_.isString(trigger)) {
      this._trigger = trigger;
    }
  }

  set outgoingUrls(outgoingUrls) {
    if (_.isArray(outgoingUrls)) {
      this._outgoingUrls = outgoingUrls;
    }
  }

  set raspDetails(raspDetails) {
    if (_.isString(raspDetails)) {
      this._raspDetails = raspDetails;
    }
  }

  set wafDetails(wafDetails) {
    if (_.isString(wafDetails)) {
      this._wafDetails = wafDetails;
    }
  }

  set userInfo(userInfo) {
    if (_.isObject(userInfo)) {
      this._userInfo = userInfo;
    }
  }

  set host(host) {
    if (_.isString(host)) {
      this._host = host;
    }
  }

  get category() { return this._category; }

  get requestId() { return this._requestId; }

  get action() { return this._action; }

  get confidenceLevel() { return this._confidenceLevel; }

  get ruleId() { return this._ruleId; }

  get type() { return this._type; }

  get stackTrace() { return this._stackTrace; }

  get redirectUrl() { return this._redirectUrl; }

  get statusCode() { return this._statusCode; }

  get requestPath() { return this._requestPath; }

  get requestVerb() { return this._requestVerb; }

  get ipAddress() { return this._ipAddress; }

  get date() { return this._date; }

  get protocol() { return this._protocol; }

  get poRequestId() { return this._poRequestId; }

  get trigger() { return this._trigger; }

  get outgoingUrls() { return this._outgoingUrls; }

  get raspDetails() { return this._raspDetails; }

  get wafDetails() { return this._wafDetails; }

  get userInfo() { return this._userInfo; }

  get host() { return this._host; }

  getJson() {
    return {
      requestId: this.requestId,
      category: this.category,
      action: this.action,
      confidenceLevel: this.confidenceLevel,
      ruleId: this.ruleId,
      type: this.type,
      stackTrace: this.stackTrace,
      raspDetails: this.raspDetails,
      wafDetails: this.wafDetails,
      redirectUrl: this.redirectUrl,
      statusCode: this.statusCode,
      requestPath: this.requestPath,
      requestVerb: this.requestVerb,
      ipAddress: this.ipAddress,
      date: this.date,
      protocol: this.protocol,
      poRequestId: this.poRequestId,
      trigger: this.trigger,
      outgoingUrls: this.outgoingUrls,
      raspDetails: this.raspDetails,
      wafDetails: this.wafDetails,
      userInfo: this.userInfo,
      host: this.host
    };
  }
}

module.exports = { Incident };