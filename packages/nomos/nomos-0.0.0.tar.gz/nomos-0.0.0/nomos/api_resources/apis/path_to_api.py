import typing_extensions

from nomos.api_resources.paths import PathValues
from nomos.api_resources.apis.paths.project_version_get_active import (
    ProjectVersionGetActive,
)
from nomos.api_resources.apis.paths.project_version_get import ProjectVersionGet
from nomos.api_resources.apis.paths.log_create import LogCreate

PathToApi = typing_extensions.TypedDict(
    "PathToApi",
    {
        PathValues.PROJECT_VERSION_GET_ACTIVE: ProjectVersionGetActive,
        PathValues.PROJECT_VERSION_GET: ProjectVersionGet,
        PathValues.LOG_CREATE: LogCreate,
    },
)

path_to_api = PathToApi(
    {
        PathValues.PROJECT_VERSION_GET_ACTIVE: ProjectVersionGetActive,
        PathValues.PROJECT_VERSION_GET: ProjectVersionGet,
        PathValues.LOG_CREATE: LogCreate,
    }
)
