import typing_extensions

from nomos.api_resources.apis.tags import TagValues
from nomos.api_resources.apis.tags.nomos_api import NomosApi

TagToApi = typing_extensions.TypedDict(
    "TagToApi",
    {
        TagValues.NOMOS: NomosApi,
    },
)

tag_to_api = TagToApi(
    {
        TagValues.NOMOS: NomosApi,
    }
)
