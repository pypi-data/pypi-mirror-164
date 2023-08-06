const { Aggregator } = require("./base");
const { Metric } = require('../metric');
const LRU = require('lru-cache');

const DEFAULT_CACHE_SIZE = 1000;
const TTL_NEVER = 0;

class UniqueAggregator extends Aggregator {
    constructor(key, frequency, options) {
        super(key, frequency, options);
        this._cache = new LRU(this.options.max_entries || DEFAULT_CACHE_SIZE);
        this._ttl = this.options.ttl || TTL_NEVER;
        this._values = [];
    }

    _doRecord(valueKey, value) {
        let val = this._cache.get(valueKey);
        if (!val || (this._ttl > 0 && ((Date.now() - val) > this._ttl * 1000/*ms to sec*/))) {
            this._cache.set(valueKey, Date.now());
            this._values.push(value);
        }
    }

    _doReport() {
        let values = this._values;
        this._values = [];
        if (values && values.length > 0) {
            let metric = new Metric(this.key, this.lastReport);
            metric.addValues(values);
            return [metric];
        }
        return [];
    }
}

module.exports = {
    UniqueAggregator: UniqueAggregator
}