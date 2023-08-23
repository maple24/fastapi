from CRQM import CRQMClient
from config import *
from datetime import datetime


# get info from config file
lTestcases_id = [i["id"] for i in source["testcases"]]
lTestcases_status = [i["status"] for i in source["testcases"]]
lTestcases_title = [i["title"] for i in source["testcases"]]
lTestcases_stepresults = [i["stepResults"] for i in source["testcases"]]
sTestplan_id = source["testplan"]["id"]
sBuildrecord_title = source["buildrecord"]["title"]
sTestsuite_title = source["testsuite"]["title"]


# 0. log into RQM
RQMclient = CRQMClient(
    "ets1szh", "estbangbangde4", "GAC_A58A88", "https://rb-alm-20-p.de.bosch.com"
)
re = RQMclient.login()
print(f"Login {re}")
RQMclient.lStartTimes.append(datetime.now())

# 1. create buildrecord
"""
params: buildinfo
"""
RQMclient.getAllBuildRecords()
re = RQMclient.createBuildRecord(sBuildrecord_title)
br_id = re["id"]
print(f"Buildreocrd ID is: {br_id}, {re}")
# 2. create test suite
"""
params: suite name
"""
RQMclient.getAllTestsuites()
re = RQMclient.createTestsuite(sTestsuite_title)
ts_id = re["id"]
print(f"Testsuite ID is: {re['id']}, {re}")

# 3. link testcases to testsuite
"""
params: suite id, testcases list
note: EST account is forbbiden
"""
re = RQMclient.linkListTestcase2Testsuite(ts_id, lTestcases_id)
print(f"Testcases linked to Testsuite: {re}")

# 4. link testsuite to testplan
"""
params: suite id, testcases list
"""
re = RQMclient.LinkListTestsuite2Testplan(sTestplan_id, ts_id)
print(f"Testsuite linked to Testplan: {re}")
# 5. create TSER
"""
params: suite id, recordname, plan id
TBD: make a compelete method 
"""
content = RQMclient.createTSERTemplate(ts_id, sTestsuite_title, sTestplan_id)
re = RQMclient.createResource("suiteexecutionrecord", content)
tser_id = re["id"]
print(f"TSER is created with ID: {re['id']}, {re}")


# 6. get all TCERS in TSER
# =======================================================================================
"""
params: testplan id, testcase id
for most cases start from here
TCERS are created when TSER created, so just retrieve them
"""
ltcers_id = [
    RQMclient.getAllTCERSbasedonTestplanandTestcases(sTestplan_id, i)
    for i in lTestcases_id
]
print(f"TCERs are fetched with IDs: {ltcers_id}")

# 7. create testcase execution result
"""
params: case id, result name,  tcer id, status, testplan id
"""
ltcresults_id = list()
for i in zip(
    lTestcases_id,
    lTestcases_title,
    ltcers_id,
    lTestcases_status,
    lTestcases_stepresults,
):
    content = RQMclient.createExecutionResultTemplate(
        testcaseID=i[0],
        testcaseName=i[1],
        TCERID=i[2],
        resultState=i[3],
        testplanID=sTestplan_id,
        stepResults=i[4],
        buildrecordID=br_id,
    )
    re = RQMclient.createResource("executionresult", content)
    ltcresults_id.append(re["id"])
    print(f"Testcase result is created with ID: {re['id']}")

# 8. create testsuite execution result
"""
params: suite id, name, tserid, ltcers id, ltestcase results id
"""
RQMclient.lEndTimes.append(datetime.now())
content = RQMclient.createTestsuiteResultTemplate(
    ts_id, sTestsuite_title, tser_id, ltcers_id, ltcresults_id, br_id
)
re = RQMclient.createResource("testsuitelog", content)
print(f"Testsuite result is created with ID: {re['id']}")

RQMclient.disconnect()
