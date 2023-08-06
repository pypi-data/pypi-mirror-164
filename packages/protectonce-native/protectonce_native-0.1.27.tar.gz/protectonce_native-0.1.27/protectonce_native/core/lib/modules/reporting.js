const _ = require('lodash');

const Constants = require('../utils/constants');
const { ReportType } = require('../reports/report');
const HeartbeatCache = require('../reports/heartbeat_cache');
const Logger = require('../utils/logger');
const { Incident } = require('../reports/incident');
const ProtectOnceContext = require('../modules/context');

function storeStackTrace(data) {
  let sessionId = null;
  try {
    if (_.isArray(data.data) && data.data[0] && data.data[0].poSessionId) {
      sessionId = data.data[0].poSessionId;
      return _mapIncidentsAndGetAction(data.data, sessionId);
    }
  } catch (error) {
    Logger.write(
      Logger.ERROR && `Error occurred while storing stackTace : ${error}`
    );
  }
  return {
    action: ReportType.REPORT_TYPE_NONE,
    sessionId
  };
}

function _mapIncidents(eventsToMap) {
  try {
    let blocked = false;
    const mappedIncidents = eventsToMap.reduce((acc, event) => {
      if (
        _.isString(event.eventType) &&
        event.reportType &&
        event.poSessionId &&
        event.resultName
      ) {
        blocked = blocked || event.reportType === ReportType.REPORT_TYPE_BLOCK;

        acc.push(_getMappedIncident(event));
      }
      return acc;
    }, []);
    const actionObject = _getAction(blocked, mappedIncidents);
    return {
      mappedIncidents,
      action: actionObject.action,
      redirectUrl: actionObject.redirectUrl
    };
  } catch (e) {
    Logger.write(Logger.DEBUG && `Failed to _mapIncidents with error: ${e}`);
    return {};
  }
}

function _getMappedIncident(event) {
  const context = ProtectOnceContext.get(event.poSessionId);
  const incident = new Incident();
  incident.requestId = event.poSessionId;
  incident.category = event.eventType;
  incident.action = event.reportType;
  incident.confidenceLevel = event.resultConfidence;
  incident.ruleId = event.ruleId;
  incident.stackTrace = event.stackTrace;
  incident.attackAttribute = event.attackAttribute;
  incident.redirectUrl = event.redirectUrl;
  incident.type = event.resultName;
  if (event.eventType === 'rasp') {
    incident.raspDetails = event.resultMessage;
  }
  if (_.isObject(context)) {
    incident.requestPath = context.requestPath;
    incident.requestVerb = context.method;
    incident.ipAddress = context.sourceIP;
    incident.protocol = context.protocol;
    incident.poRequestId = context.poRequestId;
  }
  return incident;
}

function _getAction(blocked, incidents) {
  if (incidents.some((incident) => incident.category === Constants.PLAYBOOK_EVENT_TYPE)) {
    const playbookIncident = incidents.find((incident) => incident.category === Constants.PLAYBOOK_EVENT_TYPE);
    return {
      action: playbookIncident.action,
      redirectUrl: playbookIncident.redirectUrl
    };
  }

  incidents = incidents.filter(incident => incident.category !== Constants.PLAYBOOK_EVENT_TYPE);

  if (blocked) {
    if (incidents.find((incident) => incident.category === Constants.RASP_EVENT_TYPE)) {
      return {
        action: ReportType.REPORT_TYPE_BLOCK
      };
    }
    if (incidents.find((incidents) => incidents.category === Constants.WAF_EVENT_TYPE)) {
      return {
        action: ReportType.REPORT_TYPE_ABORT
      };
    }
  }

  return {
    action: ReportType.REPORT_TYPE_NONE
  };
}

function generateWafEvents(data) {
  let sessionId = null;
  try {
    sessionId = data.data.poSessionId;
    const findings = data.data.findings;
    if (!_.isArray(findings) || _.isEmpty(findings)) {
      return {
        action: ReportType.REPORT_TYPE_NONE,
        sessionId
      };
    }
    let events = [];
    for (let finding of findings) {
      events.push({
        eventType: finding.eventType ? finding.eventType : Constants.WAF_EVENT_TYPE,
        poSessionId: sessionId,
        reportType: finding.action,
        redirectUrl: finding.redirectUrl,
        ruleId: finding.ruleId,
        resultName: finding.flowName
      });
    }

    return _mapIncidentsAndGetAction(events, sessionId);
  } catch (e) {
    Logger.write(Logger.ERROR && `Failed to generateWafEvents with error: ${e}`);
  }
  return {
    action: ReportType.REPORT_TYPE_NONE,
    sessionId
  };
}

function _mapIncidentsAndGetAction(events, sessionId) {
  try {
    const { mappedIncidents, action, redirectUrl } = _mapIncidents(events);
    if (_.isArray(mappedIncidents) && _.isString(action)) {
      HeartbeatCache.cacheIncidents(mappedIncidents);
      return {
        action,
        redirectUrl,
        sessionId
      };
    }
  } catch (e) {
    Logger.write(Logger.ERROR && `Failed to _mapIncidentsAndGetAction with error: ${e}`);
  }
  return {
    action: ReportType.REPORT_TYPE_NONE,
    sessionId
  };
}


module.exports = {
  generateWafEvents,
  storeStackTrace
};