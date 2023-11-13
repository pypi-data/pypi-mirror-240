# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from nomos.api_resources.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    PROJECT_VERSION_GET_ACTIVE = "/project/version/get_active"
    PROJECT_VERSION_GET = "/project/version/get"
    LOG_CREATE = "/log/create"
