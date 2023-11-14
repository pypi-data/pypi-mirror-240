import re
from pathlib import Path
from typing import List, Optional

from ValLib.api import get_shard

from ..api import local_api
from ..lock import LocalAppData
from ..structs import LockFile

ValorantLogs = LocalAppData / "VALORANT" / "Saved" / "Logs"


def match_region(region: str):
    region = region.lower()
    eu = ["euw", "eune", "ru", "tr"]
    ap = ["ph", "sg", "tw", "th", "vn", "oce"]
    latam = ["las", "lan"]
    na = ["na", "pbe"]
    if region == "kr":
        return "kr"
    if region == "br":
        return "br"
    if region in eu:
        return "eu"
    if region in ap:
        return "ap"
    if region in latam:
        return "latam"
    if region in na:
        return "na"
    return "na"


def get_args(data) -> Optional[List[str]]:
    try:
        args: List[str] = data["host_app"]["launchConfiguration"]["arguments"]
    except IndexError:
        return
    if "ares-deployment" not in "".join(args):
        return
    return args


def get_by_args(lock: LockFile) -> Optional[str]:
    r = local_api(lock, "GET", "/product-session/v1/external-sessions")
    if r.is_error:
        return
    data = r.json()
    args = get_args(data)
    if args is None:
        return
    deploy: str = args[4]
    region = re.split("=|&", deploy)[1]
    return region


def get_by_locale(lock: LockFile) -> str:
    data = local_api(lock, "GET", "/riotclient/region-locale").json()
    region = match_region(data["region"])
    return region


def get_by_logs(id: str):
    log = f"Logged in user changed: {id}"
    reg = r"https://shared\..*?\.a\.pvp\.net/v1/config/(.*?)]"
    # Can be optimized but it's not worth it
    for p in ValorantLogs.glob("ShooterGame*.log"):
        with p.open("r") as f:
            data = f.read()
            if log not in data:
                continue
            match = re.search(reg, data)
            if match is None:
                continue
            return match.group(1)


def get_region(lock: LockFile, id: str) -> str:
    args = get_by_args(lock)
    if args is not None:
        return args
    logs = get_by_logs(id)
    if logs is not None:
        return logs
    return get_by_locale(lock)


def get_locale(lock: LockFile, id: str):
    region = get_region(lock, id)
    shard = get_shard(region)
    return (region, shard)
