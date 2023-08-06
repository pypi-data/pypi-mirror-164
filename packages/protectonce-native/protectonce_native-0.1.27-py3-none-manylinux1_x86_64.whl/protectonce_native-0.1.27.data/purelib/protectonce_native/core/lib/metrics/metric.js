class Metric {
    constructor(key, startPeriod, endPeriod) {
        this.key = key;
        if (startPeriod) {
            this.startPeriod = startPeriod;
            this.endPeriod = endPeriod || Date.now();
        };
    }

    addHistogram(histogram) {
        this.histogram = histogram;
    }

    addCount(count) {
        this.count = count;
    }

    addSum(sum) {
        this.sum = sum;
    }

    addAverage(average) {
        this.average = average;
    }

    addValues(values) {
        this.values = values;
    }

    getData() {
        return Object.assign({}, this);
    }
}

module.exports = {
    Metric: Metric
}