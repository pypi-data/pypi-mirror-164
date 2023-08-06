const { Aggregator } = require("./base");
const { Metric } = require('../metric');


class EachAggregator extends Aggregator {
    constructor(key, frequency, options) {
        super(key, frequency, options);
        this._values = [];
    }

    record(value) {
        this._values.push(value);
    }

    _doRecord(__valueKey, __value) {
        throw new Error("Not implemented");
    }

    _doReport() {
        let values = this._values;
        this._values = []
        if (values && values.length > 0) {
            let metric = new Metric(this.key, this.lastReport);
            metric.addValues(values);
            return [metric];
        }
        return [];
    }
}

module.exports = {
    EachAggregator: EachAggregator
}