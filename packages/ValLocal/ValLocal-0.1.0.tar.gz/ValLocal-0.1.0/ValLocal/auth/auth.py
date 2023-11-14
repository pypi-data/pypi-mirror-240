from ValLib import Auth, ExtraAuth, Token

from ..api import local_api
from ..structs import LockFile
from .region import get_locale


def get_entitlements(lock: LockFile) -> Auth:
    data = local_api(lock, "GET", "/entitlements/v1/token").json()
    token = Token(data["accessToken"], "", 0)
    auth = Auth(token, data["token"], data["subject"], False, {})
    return auth


def get_name(lock: LockFile) -> str:
    data = local_api(lock, "GET", "/chat/v1/session").json()
    return data["name"]


def local_auth(lock: LockFile) -> ExtraAuth:
    auth = get_entitlements(lock)
    region, shard = get_locale(lock, auth.user_id)
    username = get_name(lock)
    extra = ExtraAuth(username, region, shard, auth)
    return extra


__all__ = ["local_auth"]
