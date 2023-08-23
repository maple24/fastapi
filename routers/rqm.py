from .utils.CRQM.CRQM import CRQMClient
from fastapi import APIRouter
from enum import Enum

cRQM = CRQMClient(
    "ets1szh", "estbangbangde4", "Zeekr", "https://rb-alm-20-p.de.bosch.com"
)


class ResourceType(str, Enum):
    testcase = "testcase"
    testscript = "testscript"
    testcaseexecutionresult = "testcaseexecutionresult"


router = APIRouter()


@router.get("/rqm/{resourceType}")
async def getTestCase(resourceType: ResourceType):
    cRQM.login()
    response = cRQM.getAllByResource(resourceType)
    cRQM.disconnect()
    return response
