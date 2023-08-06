const { Aggregator } = require("./base");
const { Metric } = require('../metric');


class HistogramAggregator extends Aggregator {
    constructor(key, frequency, options) {
        super(key, frequency, options);
        this._histogram = {};
    }

    _doRecord(valueKey, value) {
        let entry = this._histogram[valueKey];
        if (!entry) {
            this._histogram[valueKey] = entry = {
                count: 1,
                value: value
            }
        } else {
            entry.count++;
        }
    }

    _doReport() {
        let histogram = this._histogram;
        this._histogram = {};
        if (histogram && Object.keys(histogram).length > 0) {
            histogram = Object.values(histogram);
            let metric = new Metric(this.key, this.lastReport);
            metric.addHistogram(histogram);
            return [metric];
        }
        return [];
    }
}

module.exports = {
    HistogramAggregator: HistogramAggregator
}