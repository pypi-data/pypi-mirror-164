const _ = require('lodash');
const REPORT_TTL_MS = 30 * 1000;
const Constants = require('../utils/constants');

// Each request coming to the application, its metadata will be stored inside the request data object like protocol, schema for request and response, headers, ip address, etc.
class RequestData {
    constructor() {
        this._requestId = undefined;
        this._statusCode = undefined;
        this._ipAddress = undefined;
        this._date = new Date();
        this._requestVerb = undefined;
        this._requestPath = undefined;
        this._protocol = undefined;
        this._closed = false;
        this._host = undefined;
        this._pathParams = undefined;
        this._queryParams = undefined;
        this._requestHeaders = undefined;
        this._responseHeaders = undefined;
        this._requestBodySchema = undefined;
        this._responseBodySchema = undefined;
        this._poRequestId = undefined;
        this._trigger = undefined;
        this._outgoingUrls = new Set();
    }

    set host(host) {
        if (_.isString(host)) {
            this._host = host;
        }
    }

    set pathParams(pathParams) {
        if (_.isObject(pathParams)) {
            this._pathParams = pathParams;
        }
    }

    set queryParams(queryParams) {
        if (_.isObject(queryParams)) {
            this._queryParams = queryParams;
        }
    }

    set requestId(id) {
        if (id) {
            this._requestId = id;
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

    set requestVerb(requestVerb) {
        if (_.isString(requestVerb)) {
            this._requestVerb = requestVerb;
        }
    }

    set requestPath(requestPath) {
        if (_.isString(requestPath)) {
            if (requestPath !== '/') {
                requestPath = requestPath.replace(
                    Constants.PATH_TRIMMING_REGEX,
                    ''
                );
            }

            this._requestPath = requestPath;
        }
    }

    set responseBodySchema(responseBodySchema) {
        if (_.isObject(responseBodySchema)) {
            this._responseBodySchema = responseBodySchema;
        }
    }

    set requestBodySchema(requestBodySchema) {
        if (_.isObject(requestBodySchema)) {
            this._requestBodySchema = requestBodySchema;
        }
    }

    set statusCode(statusCode) {
        if (statusCode) {
            this._statusCode = statusCode;
        }
    }

    set requestHeaders(requestHeaders) {
        if (_.isObject(requestHeaders)) {
            this._requestHeaders = filterSupportedHttpHeaders(requestHeaders);
        }
    }

    set responseHeaders(responseHeaders) {
        if (_.isObject(responseHeaders)) {
            this._responseHeaders = filterSupportedHttpHeaders(responseHeaders);
        }
    }
    set protocol(protocol) {
        if (_.isString(protocol)) {
            this._protocol = protocol;
        }
    }

    setClosed() {
        this.closed = true;
    }

    _checkTTL() {
        const now = new Date();
        if (now - this._date >= REPORT_TTL_MS) {
            this.closed();
        }
    }

    set poRequestId(poRequestId) {
        this._poRequestId = poRequestId;
    }

    set trigger(trigger) {
        this._trigger = trigger;
    }

    addOutgoingUrl(outgoingUrl) {
        if (_.isString(outgoingUrl) && !this._outgoingUrls.has(outgoingUrl)) {
            this._outgoingUrls.add(outgoingUrl);
        }
    }

    get requestId() {
        return this._requestId;
    }

    get host() {
        return this._host;
    }

    get pathParams() {
        return this._pathParams;
    }

    get queryParams() {
        return this._queryParams;
    }

    get ipAddress() {
        return this._ipAddress;
    }

    get date() {
        return this._date;
    }

    get requestVerb() {
        return this._requestVerb;
    }

    get requestPath() {
        return this._requestPath;
    }

    get responseBodySchema() {

        return this._responseBodySchema;
    }

    get requestBodySchema() {
        return this._requestBodySchema;
    }

    get statusCode() {
        return this._statusCode;
    }

    get requestHeaders() {
        return this._requestHeaders;
    }

    get responseHeaders() {
        return this._responseHeaders;
    }

    get protocol() {
        return this._protocol;
    }

    get poRequestId() {
        return this._poRequestId;
    }

    get trigger() {
        return this._trigger;
    }

    get outgoingUrls() {
        return Array.from(this._outgoingUrls);
    }

    setClosed() {
        this.closed = true;
    }

    isClosed() {
        this._checkTTL();
        return this.closed;
    }

    _checkTTL() {
        const now = new Date();
        if (now - this._date >= REPORT_TTL_MS) {
            this.setClosed();
        }
    }

    getJson() {
        const requestData = {
            ipAddress: this.ipAddress,
            statusCode: this.statusCode,
            date: this.date,
            requestVerb: this.requestVerb,
            requestPath: this.requestPath,
            protocol: this.protocol,
            closed: this.closed,
            host: this.host,
            requestHeaders: this.requestHeaders,
            responseHeaders: this.responseHeaders,
            poRequestId: this.poRequestId,
            trigger: this.trigger,
            outgoingUrls: this.outgoingUrls,
            pathParams: this.pathParams,
            queryParams: this.queryParams,
            requestBodySchema: this.requestBodySchema,
            responseBodySchema: this.responseBodySchema
        };

        return requestData;
    }
}

function filterSupportedHttpHeaders(headers) {
    const SUPPORTED_HTTP_HEADERS = [
        'accept',
        'access-control-allow-origin',
        'content-length',
        'content-type',
        'from',
        'host',
        'origin',
        'referer',
        'server'
    ];
    const filteredHeaders = {};
    for (const [key, value] of Object.entries(headers)) {
        if (SUPPORTED_HTTP_HEADERS.includes(key.toLowerCase())) {
            filteredHeaders[key] = value;
        }
    }

    return filteredHeaders;
}

module.exports = {
    RequestData
}