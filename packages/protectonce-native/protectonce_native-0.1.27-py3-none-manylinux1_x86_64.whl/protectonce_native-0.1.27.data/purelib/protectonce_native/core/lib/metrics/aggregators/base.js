
class Aggregator {
    constructor(key, frequency, options) {
        this.key = key;
        this.options = options || {};
        this.lastReport = Date.now();
        this.frequency = frequency;
    }
    
    record(value) {
        return this._doRecord(this._valueKey(value), value);
    }

    report() {
        if (this._shouldReport()) {
            const report = this._doReport();
            this.lastReport = Date.now();
            return report;
        } else {
            return [];
        }
    }

    _doRecord(valueKey, value) { throw new Error("Not implemented"); }
    _doReport() { throw new Error("Not implemented"); }

    _valueKey(value) {
        if (this.options.valueKey) return this.options.valueKey(value);
        if (typeof value == 'string') return value;
        if (typeof value == 'object') return JSON.stringify(value);
        return value;
    }

    _shouldReport() {
        if (!this.frequency) return true; // report every heartbeat
        return ((Date.now() - this.lastReport) / 1000 >= this.frequency);
    }
}

module.exports = {
    Aggregator: Aggregator
}