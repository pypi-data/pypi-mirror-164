const _ = require('lodash');
const Constants = require('../utils/constants');
const { Route, Inventory, Api } = require('./inventory');
const { MetricsManager } = require('../metrics');
const Logger = require('../utils/logger');
const { isObject } = require('lodash');

class HeartbeatCache {
  constructor() {
    this._cache = {
      requestData: {},
      lastCalled: new Map(),
      incidents: {},
      userActivities: {},
      inventory: {},
      graphqlEndpoints: [],
      isRouteSentToBackend: false,
      workloadId: undefined
    };
    this._metricsManager = new MetricsManager();
  }

  cacheGraphqlEndpoint(graphqlEndpoint) {
    if (graphqlEndpoint !== '/') {
      graphqlEndpoint = graphqlEndpoint.replace(
        Constants.PATH_TRIMMING_REGEX,
        ''
      );
    }
    this._cache.graphqlEndpoints = Array.from(new Set([...this._cache.graphqlEndpoints, graphqlEndpoint]));
    this._cache.isRouteSentToBackend = false;
  }

  getWorkloadId() {
    if (_.isString(this._cache.workloadId)) {
      return this._cache.workloadId;
    }

    return _.getUuid();
  }

  cacheWorkloadId(workloadId) {
    if (_.isString(workloadId)) {
      this._cache.workloadId = workloadId;
    }
  }

  isGraphqlRequest(requestPath) {
    return this._cache.graphqlEndpoints.includes(requestPath);
  }

  cacheInventory(inventory) {
    this._cache.inventory = inventory;
    this._cache.isRouteSentToBackend = false;
  }

  getInventory() {
    return this._cache.inventory;
  }

  cacheIncidents(incidents) {
    try {
      if (_.isArray(incidents) && !_.isEmpty(incidents)) {
        for (const incident of incidents) {
          if (_.isArray(this._cache.incidents[incident.requestId])) {
            this._cache.incidents[incident.requestId].push(incident);
            continue;
          }
          this._cache.incidents[incident.requestId] = [incident];
        }
      }
    } catch (error) {
      Logger.write(Logger.ERROR && `Error occurred while caching incident : ${error}`);
    }
  }

  cacheUserActivity(userActivity) {
    try {
      if (_.isObject(userActivity)) {
        if (_.isArray(this._cache.userActivities[userActivity.requestId])) {
          this._cache.userActivities[userActivity.requestId].push(userActivity);
        } else {
          this._cache.userActivities[userActivity.requestId] = [userActivity];
        }
      }
    } catch (error) {
      Logger.write(Logger.ERROR && `Error occurred while caching user activity : ${error}`);
    }
  }

  cacheRequestData(report) {
    this._cache.requestData[report.requestId] = report;
  }

  getRequestData(requestId) {
    return this._cache.requestData[requestId] || null;
  }

  flush() {
    try {
      let apiRequestData = [], userActivities = [], incidents = [], requestSchemaData = [];
      for (let requestId in this._cache.requestData) {
        if(this._cache.requestData[requestId].isClosed()) {
          this.setClosed(requestId);
        }
      }
      const metricsReport = this._metricsManager.getMetricReports();
      let value = undefined;
      do {
        value = metricsReport.next().value;
        if (_.isObject(value) && _.isString(value.key)) {
          switch (value.key) {
            case Constants.USER_ACTIVITY:
              userActivities = value.histogram;
              break;
            case Constants.INCIDENT:
              incidents = value.values;
              break;
            case Constants.REQUEST_SCHEMA_DATA:
              requestSchemaData = value.values;
              break;
            case Constants.API_REQUEST_DATA:
              apiRequestData = value.histogram;
              break;
            default:
              Logger.write(Logger.DEBUG && `Invalid value key : ${value.key}`);
          }
        }
      } while (value);
      if (!this._cache.isRouteSentToBackend) {
        this._cache.inventory = this._populateInventoryForGraphqlRoutes(this._cache.inventory, this._cache.graphqlEndpoints);
      }
      const inventory = this._cache.inventory;
      this._cache.inventory = {};
      this._cache.isRouteSentToBackend = true;

      apiRequestData.forEach((elem) => {
        elem.value.lastCalled = this._cache.lastCalled.get(`${elem.value.requestVerb}_${elem.value.requestPath}`);
      });

      return {
        apiRequestData,
        requestSchemaData,
        incidents,
        userActivities,
        inventory
      };
    } catch (error) {
      Logger.write(Logger.ERROR && `Error occurred in HeartbeatCache.flush method : ${error}`);
    }
    return {};
  }

  setClosed(id, data) {
    try {
      if (!_.isObject(this._cache.requestData[id]) || (this.isGraphqlRequest(this._cache.requestData[id].requestPath) && _.isObject(data) && _.isString(data.context) && !data.context.includes('graphql'))) {
        return;
      }

      this._cache.requestData[id].setClosed();
      const requestData = this._cache.requestData[id].getJson();
      const incidents = this._cache.incidents[id];
      const userActivities = this._cache.userActivities[id];
      this._cacheEventsData(incidents, userActivities, requestData, id);

      if (_.isString(requestData.requestPath) && _.isString(requestData.requestVerb)) {
        this._metricsManager.record(Constants.API_REQUEST_DATA, {
          statusCode: requestData.statusCode,
          requestPath: requestData.requestPath,
          requestVerb: requestData.requestVerb
        });
      }

      this._cache.lastCalled.set(`${requestData.requestVerb}_${requestData.requestPath}`, requestData.date);
      this._metricsManager.record(Constants.REQUEST_SCHEMA_DATA, requestData);

      delete this._cache.requestData[id];
    } catch (error) {
      Logger.write(Logger.ERROR && `Error occurred while closing request : ${error}`);
    }
  }

  _cacheEventsData(incidents, userActivities, requestData, id) {
    try {
      let graphqlEndpoint, graphqlOperation;
      if (requestData.protocol === 'graphql' && _.isArray(requestData.requestBodySchema) && !_.isEmpty(requestData.requestBodySchema) && _.isString(requestData.requestBodySchema[0].endpoint) && _.isString(requestData.requestBodySchema[0].operation)) {
        graphqlEndpoint = requestData.requestBodySchema[0].endpoint;
        graphqlOperation = requestData.requestBodySchema[0].operation;
        this._cache.lastCalled.set(`${graphqlOperation}_${graphqlEndpoint}`, requestData.date);
        if (_.isString(graphqlEndpoint) && _.isString(graphqlOperation)) {
          this._metricsManager.record(Constants.API_REQUEST_DATA, {
            requestPath: graphqlEndpoint,
            requestVerb: graphqlOperation
          });
        }
      }

      if (_.isArray(incidents) && !_.isEmpty(incidents)) {
        for (const incident of incidents) {
          incident.trigger = requestData.trigger;
          incident.outgoingUrls = requestData.outgoingUrls;
          incident.host = requestData.host;
          incident.statusCode = requestData.statusCode;
          if (graphqlEndpoint && graphqlOperation) {
            incident.requestPath = graphqlEndpoint;
            incident.requestVerb = graphqlOperation;
          }
          if (_.isArray(userActivities) && !_.isEmpty(userActivities)) {
            incident.userInfo = userActivities[0].userInfo;
          }
          this._metricsManager.record(Constants.INCIDENT, incident.getJson());
        }

        delete this._cache.incidents[id];
      }

      if (_.isArray(userActivities) && !_.isEmpty(userActivities)) {
        for (const userActivity of userActivities) {
          if (graphqlEndpoint && graphqlOperation) {
            userActivity.requestPath = graphqlEndpoint;
            userActivity.requestVerb = graphqlOperation;
          }
          this._metricsManager.record(Constants.USER_ACTIVITY, userActivity.getJson());
        }

        delete this._cache.userActivities[id];
      }
    } catch (error) {
      Logger.write(Logger.ERROR && `Error occurred while caching event data: ${error}`);
    }
  }

  _populateInventoryForGraphqlRoutes(inventory, graphqlRoutes) {
    try {
      let paths = [];
      let host = undefined;
      let routes = [];
      if (_.isArray(graphqlRoutes)) {
        if (_.isObject(inventory) && _.isObject(inventory.api) && _.isArray(inventory.api.routes)) {
          routes = inventory.api.routes.map((route) => {
            paths.push(route.path);
            host = route.host;
            if (graphqlRoutes.includes(route.path)) {
              route.isGraphqlRoute = true;
            }
            return route;
          });
        }

        graphqlRoutes.forEach((graphqlRoute) => {
          if (!paths.includes(graphqlRoute)) {
            routes.push(new Route(graphqlRoute, ['POST'], host, true));
          }
        });
      }
      if (_.isObject(inventory) && _.isObject(inventory.api) && _.isArray(inventory.api.routes)) {
        inventory.api.routes = routes;
        return inventory;
      }
      return new Inventory(new Api(routes));
    } catch (error) {
      Logger.write(Logger.ERROR && `Error occurred while populating inventory: ${error}`);
    }
    return new Inventory();
  }
}

module.exports = new HeartbeatCache();
