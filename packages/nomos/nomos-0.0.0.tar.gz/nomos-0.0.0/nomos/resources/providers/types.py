from typing import List, Optional, NamedTuple
from openai.types.chat.chat_completion import ChatCompletion

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class ChatCompletionMessage(TypedDict, total=False):
    role: str
    content: Optional[str]
    function_call: Optional[dict]
    name: Optional[str]


class FunctionResponse(TypedDict):
    name: str
    response: str


class OpenaiExecuteData(NamedTuple):
    history: List[ChatCompletionMessage]
    completion: ChatCompletion
