require('../utils/common_utils');
const _ = require('lodash');
const Constants = require('../utils/constants');
const qs = require('qs');
const { Route, Api, Inventory } = require('../reports/inventory');
const HeartbeatCache = require('../reports/heartbeat_cache');
const Logger = require('../utils/logger');
const toJsonSchema = require('to-json-schema');
const { RequestData } = require('../reports/request_data');

function cacheGraphqlEndpoint(data) {
    try {
        if (!_.isString(data.data)) {
            return;
        }

        HeartbeatCache.cacheGraphqlEndpoint(data.data);
    } catch (error) {
        Logger.write(
            Logger.ERROR && `api.cacheGraphqlEndpoint: Failed to cache graphql endpoint: ${error}`
        );
    }
}

function storeGraphqlSchema(inputData) {
    try {
        if (!_.isObject(inputData.data)) {
            return;
        }

        _addGraphqlSchemaToInventory(inputData.data);
    } catch (error) {
        Logger.write(
            Logger.ERROR && `api.storeGraphqlSchema: Failed to store graphql schema: ${error}`
        );
    }
}

function _addGraphqlSchemaToInventory(graphqlSchema) {
    let inventory = HeartbeatCache.getInventory();
    if (!_.isObject(inventory) || !_.isObject(inventory.api)) {
        inventory = new Inventory(new Api());
    }
    inventory.api.addGraphqlSchema(graphqlSchema);
    HeartbeatCache.cacheInventory(inventory);
}

function storeRoute(inputData) {
    try {
        const routes = inputData.data;
        if (!_.isArray(routes)) {
            return;
        }

        let inventory = HeartbeatCache.getInventory();
        routes.forEach((route) => {
            route.paths.forEach((path) => {
                if (!_.isString(path) || !(_.isArray(route.methods) || _.isString(route.methods)) || !_.isString(route.host)) {
                    return;
                }
                const trimmedPath = path !== '/' ? path.replace(
                    Constants.PATH_TRIMMING_REGEX,
                    ''
                ) : path;

                const routeToBeAdded = new Route(
                    trimmedPath,
                    _getMethodsForRoute(route.methods),
                    route.host
                );
                inventory = _populateInventory(inventory, routeToBeAdded);
            });
        });

        HeartbeatCache.cacheInventory(inventory);
    } catch (error) {
        Logger.write(
            Logger.ERROR && `api.StoreRoute: Failed to store route: ${error}`
        );
    }
}

function _getMethodsForRoute(routeMethods) {
    if (_.isString(routeMethods) && routeMethods === '*') {
        return Constants.SUPPORTED_HTTP_METHODS;
    }

    if (_.isArray(routeMethods)) {
        return routeMethods.filter((method) =>
            Constants.SUPPORTED_HTTP_METHODS.includes(method)
        );
    }

    return [];
}

function _populateInventory(inventory, routeToBeAdded) {
    if (inventory && inventory.api && _.isArray(inventory.api.routes)) {
        _addRouteToExistingInventory(inventory, routeToBeAdded);
        return inventory;
    }
    return new Inventory(new Api([routeToBeAdded]));
}

function _addRouteToExistingInventory(inventory, routeToBeAdded) {
    const existingRoute = inventory.api.routes.find(
        (route) => route.path === routeToBeAdded.path
    );
    if (existingRoute) {
        existingRoute.addMethods(routeToBeAdded.methods);
        return;
    }
    inventory.api.addRoute(routeToBeAdded);
}

function _getRequestPath(inputData, requestData) {
    if (_.isObject(inputData) && _.isString(inputData.requestPath)) {
        return inputData.requestPath;
    }

    if (_.isObject(requestData) && _.isString(requestData.requestPath)) {
        return requestData.requestPath;
    }

    return null;
}

function parseHttpData(data) {
    try {
        const inputData = data.data;
        if (!_.isObject(inputData) || _.isEmpty(inputData)) {
            return {};
        }
        let requestData = _createRequestData(inputData);
        if (HeartbeatCache.isGraphqlRequest(requestData.requestPath) && !data.context.includes('graphql')) {
            HeartbeatCache.cacheRequestData(requestData);
            return inputData;
        }

        requestData = _mapRequestData(requestData, inputData);
        HeartbeatCache.cacheRequestData(requestData);
        return inputData;
    } catch (error) {
        Logger.write(
            Logger.ERROR &&
            `api.parseHttpData: Failed to parse http data: ${error}`
        );
        return {};
    }
}

function _createRequestData(inputData) {
    let requestData = HeartbeatCache.getRequestData(inputData.poSessionId);
    if (!requestData) {
        requestData = new RequestData();
        requestData.requestId = inputData.poSessionId;
        if (_.isString(inputData.poRequestId) && inputData.poRequestId.includes(Constants.WORKLOAD_ID_SEPARATOR)) {
            requestData.poRequestId = inputData.poRequestId;
        }
    }
    
    let requestPath = _getRequestPath(inputData, requestData);
    if (_.isString(requestPath) && requestPath !== '/') {
        requestPath = requestPath.replace(Constants.PATH_TRIMMING_REGEX, '');
    }
    if (_.isString(requestPath) && !_.isEmpty(requestPath)) {
        requestData.requestPath = requestPath;
    }
    requestData.requestVerb = inputData.method;
    requestData.protocol = inputData.protocol;
    requestData.host = inputData.host;
    requestData.ipAddress = inputData.sourceIP;
    requestData.requestHeaders = inputData.requestHeaders;
    requestData.responseHeaders = inputData.responseHeaders;

    requestData.statusCode = inputData.statusCode;
    const trigger = _getAWSLambdaEventSource(inputData.requestBody);
    requestData.trigger = trigger;
    _storeApiGatewayAwsProxyRoute(trigger, inputData.requestBody);
    
    return requestData;
}

function _mapRequestData(requestData, inputData) {
    if (_.isObject(inputData.queryParams)) {
        requestData.queryParams = toJsonSchema(inputData.queryParams);
    }

    if (_.isObject(inputData.pathParams)) {
        requestData.pathParams = toJsonSchema(inputData.pathParams);
    }
    const requestHeaders = inputData.requestHeaders || requestData.requestHeaders || {};

    const responseHeaders = inputData.responseHeaders || requestData.responseHeaders || {};

    requestData.requestBodySchema = _getJsonSchema(
        inputData,
        inputData.requestBody,
        requestHeaders && _.getObjectKeysToLower(requestHeaders, 'content-type')
    );
    requestData.responseBodySchema = _getJsonSchema(
        inputData,
        inputData.responseBody,
        responseHeaders && _.getObjectKeysToLower(responseHeaders, 'content-type')
    );

    return requestData;
}

function _getJsonSchema(inputData, body, headerToCheck) {
    if (!_.isString(body) && !_.isObject(inputData.formData)) {
        return;
    }
    if (_.isString(body)) {
        const parsedBody = _.parseIfJson(body);
        if (parsedBody) {
            if (_.isGraphqlRequest(inputData.protocol)) {
                return _parseGraphqlBody(parsedBody);
            }

            if (_.isValidJsonRequest(headerToCheck)) {
                return toJsonSchema(parsedBody);
            }
        }
    }

    if (_.isValidEncodedFormDataRequest(headerToCheck)) {
        if (_.isString(body)) {
            const bodyObject = qs.parse(body.toString());
            return toJsonSchema(bodyObject);
        }
        return toJsonSchema(inputData.formData.fields);
    }

    if (_.isObject(inputData.formData)) {
        if (_.isValidMultipartFormDataRequest(headerToCheck)) {
            let formData = {
                type: "object",
                properties: {}
            };
            if (_.isObject(inputData.formData.fields)) {
                formData = toJsonSchema(inputData.formData.fields);
            }
            if (_.isArray(inputData.formData.filesFieldNames) && inputData.formData.filesFieldNames.length) {
                inputData.formData.filesFieldNames.forEach((fileField) => {
                    formData.properties[fileField] = {
                        type: "file"
                    };
                });
            }
            return formData;
        }
    }

    return;
}

function _getAWSLambdaEventSource(body) {
    try {
        if (!_.isAWSLambdaEnv()) {
            return '';
        }
        const event = _.parseIfJson(body);

        if (event.Records && _.isArray(event.Records) && event.Records.length) {
            if (event.Records[0].cf) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.CLOUD_FRONT;
            }
            if (event.Records[0].eventSource === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.CODE_COMMIT) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.CODE_COMMIT;
            }
            if (event.Records[0].eventSource === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.SES) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.SES;
            }
            if (event.Records[0].EventSource === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.SNS) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.SNS;
            }
            if (event.Records[0].eventSource === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.DYNAMODB) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.DYNAMODB;
            }

            if (event.Records[0].eventSource === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.KINESIS) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.KINESIS;
            }

            if (event.Records[0].eventSource === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.S3) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.S3;
            }
        }

        if (event.records && _.isArray(event.records) && event.records.length) {
            if (event.records[0].approximateArrivalTimestamp) {
                return Constants.AWS_LAMBDA_EVENT_SOURCE.KINESIS_FIREHOSE;
            }
        }
        if (event.operation && event.message) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.MOBILE_BACKEND;
        }
        if (event.configRuleId && event.configRuleName && event.configRuleArn) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.AWS_CONFIG;
        }
        if (event.authorizationToken === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.API_GATEWAY_AUTHORIZER) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.API_GATEWAY_AUTHORIZER;
        }
        if (event.StackId && event.RequestType && event.ResourceType) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.CLOUD_FORMATION;
        }
        if (event.pathParameters && event.pathParameters.proxy) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.API_GATEWAY_AWS_PROXY;
        }
        if (event.source === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.SCHEDULED_EVENT) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.SCHEDULED_EVENT;
        }
        if (event.awslogs && event.awslogs.data) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.CLOUD_WATCH_LOGS;
        }
        if (event.deliveryStreamArn && event.deliveryStreamArn.startsWith(Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.KINESIS_FIREHOSE)) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.KINESIS_FIREHOSE;
        }
        if (event.eventType === Constants.AWS_LAMBDA_EVENT_SOURCE_VALUE.CONGNITO_SYNC_TRIGGER && event.identityId && event.identityPoolId) {
            return Constants.AWS_LAMBDA_EVENT_SOURCE.CONGNITO_SYNC_TRIGGER;
        }

    } catch (error) {
        Logger.write(
            Logger.ERROR && `api._getAWSLambdaEventSource: Failed to find event source: ${error}`
        );
    }
    return '';

}

function _storeApiGatewayAwsProxyRoute(trigger, body) {
    if (!_.isAWSLambdaEnv()) {
        return;
    }
    if (_.isAWSLambdaEnv() && trigger === Constants.AWS_LAMBDA_EVENT_SOURCE.API_GATEWAY_AWS_PROXY) {
        const event = _.parseIfJson(body);
        const apiGatewayRoute = {
            data: [
                {
                    paths: [event.path],
                    methods: [event.httpMethod],
                    host: event.Host || ''
                }
            ]
        }

        storeRoute(apiGatewayRoute);
    }
}

function _parseGraphqlBody(parsedBody) {
    try {
        if (!_.isArray(parsedBody) && isEmpty(parsedBody)) {
            return {};
        }

        return parsedBody.map((requestOperation) => ({
            operation: requestOperation.operation,
            endpoint: requestOperation.endpoint,
            schema: toJsonSchema(requestOperation.data)
        }));
    } catch (error) {
        Logger.write(
            Logger.ERROR &&
            `parseGraphqlBody: Failed to parse graphql body: ${error}`
        );
        return {};
    }
}

function addPoRequestId(data) {
    try {
        if (!data) {
            return {};
        }
        const workLoadIdFromRequest = data.data.requestHeaders ?
            data.data.requestHeaders[Constants.OUTGOING_REQUEST_HEADER_POREQUESTID.toLowerCase()] : "";
        const workLoadId = HeartbeatCache.getWorkloadId();
        let mergedworkLoadId = workLoadId;
        if (workLoadIdFromRequest) {
            mergedworkLoadId = workLoadIdFromRequest + (workLoadId ? Constants.WORKLOAD_ID_SEPARATOR + workLoadId : "");
        }
        data.data.poRequestId = mergedworkLoadId;
        return data.data;
    } catch (error) {
        Logger.write(
            Logger.ERROR &&
            `api.addPoRequestId: Failed to add addPoRequestId: ${error}`
        );
    }
}

module.exports = {
    storeRoute,
    parseHttpData,
    addPoRequestId,
    storeGraphqlSchema,
    cacheGraphqlEndpoint
};
