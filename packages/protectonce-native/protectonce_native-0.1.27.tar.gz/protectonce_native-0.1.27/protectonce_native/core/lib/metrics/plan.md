- we need implement a per-metric reporting strategy that includes the frequency
- consider where values need to be objects not strings (or numbers)


dataReporter.register("DA-CONNECTIONS", HISTOGRAM);



dataReporter.report("DA-CONNECTIONS", {path: "a/b/c", schema: "aaa", type: ""})
dataReporter.report("DA-CONNECTIONS", {path: "a/b/c", schema: "bbb"})




// when capturing outgoing request to dynamo
// ddb.query("somthing");

-- We will need specialized field extractors for specific domains/services that know to grab things like tableName, queueName, topicArn...

https://dynamodb.../query

body
{
    tableName: "table123",
}

reportInfo = {
    context: "/a/b/c",
    url: "https://dynamoDb.amazonaws.com/someTable/otherstuff",
    tableName: "table123",
    mime_type: "application/json",
    schema: { "key": "string", "key2": ["string", "string"], "key3": { "key4": "string"} }
}

dataReporter.report("DA-OUTGOING-CONNECTIONS", reportInfo)




...

dataReporter.getMetrics()

{
    DA-OUTGOING-CONNECTIONS: [
        {
            value:  {
                        context: "/a/b/c",
                        url: "https://dynamoDb.amazonaws.com/someTable/otherstuff",
                        mime_type: "application/json",
                        schema: { "key": "string", "key2": ["string", "string"], "key3": { "key4": "string"} }
                    },
            count: 100
        },
        {
            context: "/a/b/c",
            url: "https://dynamoDb.amazonaws.com/someTable/otherstuff",
            mime_type: "application/json",
            schema: { "key": "string", "key2": ["string", "string"] }
        },
        
    ]
}