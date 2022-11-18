from fastapi import APIRouter
from .utils.artifactory.artifactory_helper import artimonitor

router = APIRouter()

@router.get("/artifactory/latest")
async def get_version_info():
    server = "https://rb-cmbinex-szh-p1.apac.bosch.com:443/artifactory/"
    repo = "zeekr-dhu-repos/builds/rb-zeekr-dhu_hqx424-fc_main_dev/daily"
    return  artimonitor(server=server, repo=repo, pattern="userdebug.tgz")