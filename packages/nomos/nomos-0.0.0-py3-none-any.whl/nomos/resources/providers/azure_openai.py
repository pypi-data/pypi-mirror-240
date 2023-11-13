from typing import List

from nomos.resources.providers.base_openai import BaseOpenai

from nomos.api_resources.models import (
    DynamicParameters,
    AzureOpenAIChatCompletionParams,
    AzureOpenAIChatCompletionPrompt,
)
from nomos.resources.providers.types import (
    ChatCompletionMessage,
    OpenaiExecuteData,
)
from openai import AzureOpenAI
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.completion_create_params import Function
import json


class AzureOpenai(BaseOpenai):
    def __init__(
        self,
        client: AzureOpenAI,
        prompt: AzureOpenAIChatCompletionPrompt,
        parameters: AzureOpenAIChatCompletionParams,
    ):
        self.client = client
        self.prompt = prompt
        self.parameters = parameters

    def llm_request(
        self,
        messages: List[ChatCompletionMessage],
        parameters: AzureOpenAIChatCompletionParams,
    ) -> OpenaiExecuteData:
        chat_completion_args = dict(
            messages=messages,
        )
        for key, value in parameters.items():
            if key not in set(
                [
                    "deployment_name",
                    "top_p",
                    "temperature",
                    "stop",
                    "max_tokens",
                    "presence_penalty",
                    "frequency_penalty",
                    "logit_bias",
                    "function_call",
                    "functions",
                    "user",
                ]
            ):
                continue
            # Convert functions into openai's format
            if key == "functions":
                openai_functions: List[Function] = []
                for nomos_function in value:
                    try:
                        parameters = (
                            json.loads(nomos_function["parameters"]["value"])
                            if isinstance(
                                nomos_function["parameters"], DynamicParameters
                            )
                            else nomos_function["parameters"]["value"]
                        )
                    except Exception:
                        raise ValueError(
                            f'Unable to parse function parameters value as json {nomos_function["parameters"]["value"]}'
                        )
                    openai_functions.append(
                        Function(
                            **{
                                k: v
                                for k, v in nomos_function.items()
                                if k != "parameters"
                            },
                            parameters=parameters,
                        )
                    )
                chat_completion_args[key] = openai_functions
            elif key == "deployment_name":
                # Example from openai: https://github.com/openai/openai-python/blob/main/examples/azure.py#L15
                chat_completion_args["model"] = value
            else:
                chat_completion_args[key] = value

        chat_completion: ChatCompletion = self.client.chat.completions.create(
            **chat_completion_args,
        )

        for choice in chat_completion.choices:
            messages.append(
                ChatCompletionMessage(choice.message.model_dump(exclude_unset=True))
            )

        return OpenaiExecuteData(
            history=messages,
            completion=chat_completion,
        )
