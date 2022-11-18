# CRQM-Introduction
Tools for IBM-RQM

[API portal](https://jazz.net/wiki/bin/view/Main/RqmApi#feedUrl_for_interaction_with_a_f)


# Quick Start



## Glossary
1. integrationUrl
   
   `https://<host>:<port>/ <contextRoot>/service/com.ibm.rqm.integration.service.IIntegrationService`
2. contextRoot
   
   `
    The context root of the Rational Quality Manager application.
    Rational Quality Manager 1.x, 2.x, and 3.0: jazz
    Rational Quality Manager 3.0.1 or later: qm
   `
3. feedUrl
   - singleProjectFeedUrl

    `<integrationUrl>/resources/ <projectAlias>/ <resourceType>`

    - crossProjectFeedUrl

    `<integrationUrl>/resources/ <resourceType>`
4. resourceUrl
   
   `<singleProjectFeedUrl>/ <id>`
5. ETM Schema
   
   `<integrationUrl>/schema/<schema file name>`
6. Feed
   
   `Resources can be read ( GET) individually (see <resourceUrl>) or as a feed of similar typed resources (see <feedUrl>)`
   `feed means a series of resource, while resouce typically means single one`


## Tips
1. To determine the XML representation of the resource:

Read an existing resource as XML with abbreviate=false.

Delete the read-only properties (see Detailed Schema Documentation for read-only properties).

Add/modify/delete the writable properties (see Detailed Schema Documentation for writable properties).

2. To generate stepResult of executionresult

href in stepResult is necessary, but the id can be arbitrary(e. use '_' as placeholder).

description cannot be empty

testcript is necessray, otherwise no stepResults will showup.

Attachments/Links is warped with \<ns16:comment>
