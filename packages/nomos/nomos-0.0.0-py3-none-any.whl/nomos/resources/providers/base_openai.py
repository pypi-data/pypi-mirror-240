from abc import ABC, abstractmethod
from typing import List, Union

from nomos.api_resources.models import (
    AzureOpenAIChatCompletionParams,
    OpenAIChatCompletionParams,
    AzureOpenAIChatCompletionPrompt,
    OpenAIChatCompletionPrompt,
    OpenAIFunctionCallObject,
    OpenAIFunctionCallValues,
    OpenAIFunction,
    DynamicParameters,
)
from nomos.resources.providers.types import (
    ChatCompletionMessage,
    FunctionResponse,
    OpenaiExecuteData,
)
from nomos.resources.variable_parser import VariablesData, VariableParser
from nomos.resources.prompt_parser import PromptParser
from openai import OpenAI, AzureOpenAI


class BaseOpenai(ABC):
    def __init__(
        self,
        client: Union[OpenAI, AzureOpenAI],
        prompt: Union[OpenAIChatCompletionPrompt, AzureOpenAIChatCompletionPrompt],
        parameters: Union[OpenAIChatCompletionParams, AzureOpenAIChatCompletionParams],
    ):
        self.client = client
        self.prompt = prompt
        self.parameters = parameters

    def execute(
        self,
        chat_history: List[ChatCompletionMessage],
        variables: VariablesData,
    ) -> OpenaiExecuteData:
        parsed_prompt = PromptParser.get_parsed_prompt(
            prompt=self.prompt,
            variables=variables,
        )

        # Copy chat history to avoid modifying the original
        messages = chat_history[:]

        for index, _ in enumerate(parsed_prompt.messages):
            message = parsed_prompt.messages[index]
            chat_completion_message = ChatCompletionMessage(
                {key: value for key, value in message.items()}
            )
            messages.append(chat_completion_message)

        parsed_parameters = self.parse_parameters(self.parameters, variables)
        return self.llm_request(messages, parsed_parameters)

    def send_function_response(
        self,
        chat_history: List[ChatCompletionMessage],
        function_response: FunctionResponse,
        variables: VariablesData,
    ) -> OpenaiExecuteData:
        messages = chat_history[:]
        messages.append(
            ChatCompletionMessage(
                role="function",
                name=function_response["name"],
                content=function_response["response"],
            )
        )
        parsed_parameters = self.parse_parameters(self.parameters, variables)
        return self.llm_request(messages, parsed_parameters)

    def parse_parameters(
        self,
        parameters: Union[AzureOpenAIChatCompletionParams, OpenAIChatCompletionParams],
        variables: VariablesData,
    ) -> Union[AzureOpenAIChatCompletionParams, OpenAIChatCompletionParams]:
        if not isinstance(
            parameters, (AzureOpenAIChatCompletionParams, OpenAIChatCompletionParams)
        ):
            raise ValueError(f"Parameters {parameters} is not supported")
        new_parameters = dict()
        for key, value in parameters.items():
            if key == "function_call":
                new_function_call_value: Union[
                    OpenAIFunctionCallValues, OpenAIFunctionCallObject
                ] = value
                if isinstance(value, OpenAIFunctionCallObject):
                    name = VariableParser.populate_variables(
                        content=value.name,
                        variables=variables,
                    )
                    new_function_call_value = OpenAIFunctionCallObject(name=name)
                new_parameters[key] = new_function_call_value
            elif key == "functions":
                new_functions_value: List[OpenAIFunction] = []
                for function in value:
                    new_function_args = dict()
                    if "description" in function:
                        new_function_args[
                            "description"
                        ] = VariableParser.populate_variables(
                            content=function["description"],
                            variables=variables,
                        )
                    new_function_args["name"] = VariableParser.populate_variables(
                        content=function["name"],
                        variables=variables,
                    )
                    if isinstance(function["parameters"], DynamicParameters):
                        new_function_args["parameters"] = DynamicParameters(
                            **{
                                key: value
                                for key, value in function["parameters"].items()
                                if key != "value"
                            },
                            value=VariableParser.populate_variables(
                                content=function["parameters"]["value"],
                                variables=variables,
                            ),
                        )
                    else:
                        new_function_args["parameters"] = function["parameters"]
                    new_functions_value.append(OpenAIFunction(**new_function_args))
                new_parameters[key] = new_functions_value
            else:
                new_parameters[key] = value
        return parameters.__class__(**new_parameters)

    @abstractmethod
    def llm_request(
        self,
        *args,
        **kwargs,
    ):
        pass
