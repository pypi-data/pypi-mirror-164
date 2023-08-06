'use strict';
const { DataReporter, ReportPolicy, REPORT_TYPE, REPORT_FREQUENCY } = require('./data_reporter');
const Constants = require('../utils/constants');
const CryptoJS = require("crypto-js");

const DEFAULT_METRICS = {
  "metricList": [{
    "key": Constants.INCIDENT,
    "type": "EACH",
    "frequency": 0,
    "options": {}
  },
  {
    "key": Constants.API_REQUEST_DATA,
    "type": "HISTOGRAM",
    "frequency": 0,
    "options": {}
  },
  {
    "key": Constants.REQUEST_SCHEMA_DATA,
    "type": "UNIQUE",
    "frequency": 0,
    "options": {
      valueKey: (value) => {
        const objectForHash = {
          requestPath: value.requestPath,
          requestVerb: value.requestVerb,
          trigger: value.trigger,
          outgoingUrls: value.outgoingUrls,
          pathParams: value.pathParams,
          queryParams: value.queryParams,
          requestBodySchema: value.requestBodySchema,
          responseBodySchema: value.responseBodySchema
        };

        return CryptoJS.SHA256(JSON.stringify(objectForHash)).toString();
      }
    }
  },
  {
    "key": Constants.USER_ACTIVITY,
    "type": "HISTOGRAM",
    "frequency": 0,
    "options": {
      valueKey: (value) => ({
        action: value.action,
        status: value.status,
        user: value.userInfo,
        eventType: value.eventType,
        ipAddress: value.ipAddress,
        requestPath: value.requestPath,
        requestVerb: value.requestVerb,
        eventAttributes: value.eventAttributes
      })
    }
  }]
};

const metricTypes = {
  "EACH": REPORT_TYPE.REPORT_EACH,
  "UNIQUE": REPORT_TYPE.REPORT_UNIQUE,
  "HISTOGRAM": REPORT_TYPE.REPORT_HISTOGRAM,
  "AVERAGE": REPORT_TYPE.REPORT_AVERAGE
}

class MetricsManager {
  constructor(metricsDef) {
    this.reporter = new DataReporter();
    if (metricsDef === undefined) {
      metricsDef = DEFAULT_METRICS;
    }
    this.updateMetrics(metricsDef);
  }

  updateMetrics(metricsDef) {
    let remainingMetrics = new Set(this.reporter.listMetrics());

    if (metricsDef) {
      for (let metricEntry of metricsDef.metricList || []) {
        let metricType = metricTypes[metricEntry.type || ""];
        let metricFrequency = metricEntry.frequency;
        let metricKey = metricEntry.key;

        if (remainingMetrics.has(metricKey)) { // already have a metric like this - in theory we could check if anything changed....
          this.reporter.remove(metricKey); // make room for the  new one
        }

        this.reporter.register(metricKey, new ReportPolicy(metricType, metricFrequency, metricEntry.options))

        remainingMetrics.delete(metricKey);
      }

      // anything left if the remainingMetrics should be deleted
      for (let oldKey of remainingMetrics) {
        this.reporter.remove(oldKey);
      }
    }
  }

  record(key, value) {
    this.reporter.record(key, value);
  }

  *getMetricReports() {
    yield* this.reporter.getMetricReports();
  }

}

module.exports = {
  MetricsManager
}