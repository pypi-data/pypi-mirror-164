const Logger = require('../../utils/logger');
const { parseHttpData } = require('../api');
const { storeHttpRequestInfo, createSession, closeHttpRequest } = require('../httpServer');
const WAF = require('../waf');
const { generateWafEvents } = require('../reporting');
const _ = require('lodash');
const { ReportType } = require('../../reports/report');

function handleAgentlessRequest(data) {
    try {
        if (_.isObject(data) && _.isObject(data.data)) {
            const sessionId = createSession();
            data.data.poSessionId = sessionId;
            const inputData = parseHttpData(data);
            const requestData = {
                data: inputData
            };
            const requestDataForHeaders = {
                data: {
                    requestInfo: inputData
                }
            };
            storeHttpRequestInfo(requestData);
            const paramsFindings = WAF.scanRequestParams(requestData);
            const bodyFindings = WAF.scanHttpBody(requestData);
            const headerFindings = WAF.scanHttpHeaders(requestDataForHeaders);
            const findings = [
                ...paramsFindings.findings,
                ...bodyFindings.findings,
                ...headerFindings.findings
            ];
            if (_.isArray(findings) && !_.isEmpty(findings)) {
                findings.forEach((finding) => {
                    if (_.isString(finding.action) && finding.action === ReportType.REPORT_TYPE_BLOCK) {
                        Logger.write(Logger.INFO && "WAF Incident not blocked, but got reported because we're working in agentless mode.");
                        finding.action = ReportType.REPORT_TYPE_REPORT;
                    }
                });
                generateWafEvents({
                    data: {
                        poSessionId: sessionId,
                        findings
                    }
                });
            }
            closeHttpRequest(requestData);
        }
    } catch (error) {
        Logger.write(Logger.ERROR && "Error occurred inside handleAgentlessRequest : ", error);
    }
}

module.exports = {
    handleAgentlessRequest
}