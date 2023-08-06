const Logger = require('../utils/logger');
const Aggregators = require("./aggregators");

const REPORT_TYPE = {
    REPORT_EACH: 1,
    REPORT_UNIQUE: 2,
    REPORT_HISTOGRAM: 3,
    REPORT_AVERAGE: 4
}

const REPORT_FREQUENCY = {
    HEARTBEAT: 0
}


class ReportPolicy {
    constructor(reportType, frequency, options) {
        this.reportType = reportType || REPORT_TYPE.REPORT_EACH;
        this.reportFrequency = frequency || REPORT_FREQUENCY.HEARTBEAT;
        this.options = options || {};
    }
}
ReportPolicy.defaultPolicy = new ReportPolicy();


class DataReporter {
    constructor() {
        this.aggregators = {}
    }

    listMetrics() {
        return Object.keys(this.aggregators);
    }

    register(key, reportPolicy) {
        if (!reportPolicy) {
            reportPolicy = ReportPolicy.defaultPolicy;
        }
        switch (reportPolicy.reportType) {
            case REPORT_TYPE.REPORT_EACH:
                this.aggregators[key] = new Aggregators.EachAggregator(key, reportPolicy.reportFrequency, reportPolicy.options);
                break;
            case REPORT_TYPE.REPORT_UNIQUE:
                this.aggregators[key] = new Aggregators.UniqueAggregator(key, reportPolicy.reportFrequency, reportPolicy.options);
                break;
            case REPORT_TYPE.REPORT_HISTOGRAM:
                this.aggregators[key] = new Aggregators.HistogramAggregator(key, reportPolicy.reportFrequency, reportPolicy.options);
                break;
            case REPORT_TYPE.REPORT_AVERAGE:
                this.aggregators[key] = new Aggregators.AverageAggregator(key, reportPolicy.reportFrequency, reportPolicy.options);
                break;
            default:
                Logger.ERROR && Logger.write(`DataReporter: Invalid Report Type; ignoring.(${reportPolicy.reportType})`);
        }
    }

    remove(key) {
        delete this.aggregators[key]
    }

    record(key, value) {
        let aggregator = this.aggregators[key];
        if (!aggregator) {
            Logger.INFO && Logger.write(`DataReporter: Key not found; ignoring.(${key})`);
            return;
        }
        aggregator.record(value);
    }

    *getMetricReports() {
        for (let [key, aggregator] of Object.entries(this.aggregators)) {
            yield* aggregator.report().map(metric => metric.getData());
        }
    }
}

module.exports = {
    REPORT_TYPE,
    REPORT_FREQUENCY,
    ReportPolicy,
    DataReporter
}
