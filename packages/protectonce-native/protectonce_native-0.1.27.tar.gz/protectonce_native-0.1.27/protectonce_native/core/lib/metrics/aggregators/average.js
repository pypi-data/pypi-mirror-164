const { Aggregator } = require("./base");
const { Metric } = require('../metric');
const Logger = require('../../utils/logger');

class AverageAggregator extends Aggregator {
    constructor(key, frequency, options) {
        super(key, frequency, options);
        this._count = 0;
        this._total = 0;
    }

    _doRecord(__valueKey, value) {
        if (typeof value !== 'number') {
            Logger.write(Logger.ERROR && `AverageAggregator: Got non-numerical value. Ignoring. (${key}=${value})`);
            return;
        }
        this._count++;
        this._total += value;
    }

    _doReport() {

        if (this._count > 0) {
            let metric = new Metric(this.key, this.lastReport);
            metric.addCount(this._count);
            metric.addSum(this._total);
            metric.addAverage(this._total / this._count);
            this._count = 0;
            this._total = 0;
            return [metric];
        }
        this._count = 0;
        this._total = 0;
        return [];
    }
}

module.exports = {
    AverageAggregator: AverageAggregator
}