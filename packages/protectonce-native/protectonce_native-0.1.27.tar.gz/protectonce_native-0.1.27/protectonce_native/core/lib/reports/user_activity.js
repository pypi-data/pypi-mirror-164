const _ = require('lodash');

// class for storing each user activity done via middleware, so that we can send it to the backend.
//Like, what's user data from the request, request metadata, event attributes, action taken for particular user request, etc.
class UserActivity {
  constructor() {
    this._requestId = undefined; // Unique identifier for each request, used to identify to which request, user activity belongs to.
    this._category = undefined; // For user activity, categoty will be 'user.activity'
    this._action = undefined; // Action performed on the request, like blocked, redrected, no_action.
    this._status = undefined; 
    this._redirectUrl = undefined;
    this._userInfo = undefined;
    this._statusCode = undefined;
    this._requestPath = undefined;
    this._requestVerb = undefined;
    this._ipAddress = undefined;
    this._date = new Date();
    this._protocol = undefined;
    this._eventAttributes = undefined;
  }

  set requestId(requestId) {
    if (_.isString(requestId)) {
      this._requestId = requestId;
    }
  }

  set category(category) {
    if (_.isString(category)) {
      this._category = category;
    }
  }

  set action(action) {
    if (_.isString(action)) {
      this._action = action;
    }
  }

  set status(status) {
    if (_.isString(status)) {
      this._status = status;
    }
  }

  set userInfo(userInfo) {
    if (_.isObject(userInfo)) {
      this._userInfo = userInfo;
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

  set eventAttributes(eventAttributes) {
    if (_.isObject(eventAttributes)) {
      this._eventAttributes = eventAttributes;
    }
  }

  get category() { return this._category; }

  get action() { return this._action; }

  get status() { return this._status; }

  get userInfo() { return this._userInfo; }

  get redirectUrl() { return this._redirectUrl; }

  get statusCode() { return this._statusCode; }

  get requestPath() { return this._requestPath; }

  get requestVerb() { return this._requestVerb; }

  get ipAddress() { return this._ipAddress; }

  get date() { return this._date; }

  get protocol() { return this._protocol; }

  get eventAttributes() { return this._eventAttributes; }

  get requestId() { return this._requestId; }

  getJson() {
    return {
      requestId: this._requestId,
      category: this.category,
      action: this.action,
      status: this.status,
      redirectUrl: this.redirectUrl,
      userInfo: this.userInfo,
      statusCode: this.statusCode,
      requestPath: this.requestPath,
      requestVerb: this.requestVerb,
      ipAddress: this.ipAddress,
      date: this.date,
      protocol: this.protocol,
      eventAttributes: this.eventAttributes
    };
  }
}

module.exports = { UserActivity };