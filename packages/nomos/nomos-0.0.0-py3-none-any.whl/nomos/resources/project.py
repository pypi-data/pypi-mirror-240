from typing import (
    List,
    NamedTuple,
    Optional,
    Type,
    TYPE_CHECKING,
)
from nomos import (
    ProjectVersionGetActiveRequest,
    ProjectVersion,
    ProjectVersionGetRequest,
    Task,
    OpenAIChatCompletionParams,
    AzureOpenAIChatCompletionParams,
)
from nomos.resources.providers.openai import Openai
from nomos.resources.providers.azure_openai import AzureOpenai
from nomos.resources.providers.types import ChatCompletionMessage, FunctionResponse
from nomos.resources.variable_parser import VariablesData
from nomos.resources.providers.types import OpenaiExecuteData

# Avoids circular import issues with typing
if TYPE_CHECKING:
    from .client import Nomos


class NomosTask:
    def __init__(
        self,
        project: Type["NomosProject"],
        task: Task,
        chat_history: Optional[List[ChatCompletionMessage]] = None,
    ):
        self.project = project
        self.task = task
        self.chat_history = chat_history if chat_history is not None else []
        # Copy chat history. Gets updated after each run.
        self._live_chat_history = self.chat_history[:]

    @property
    def llm(self):
        if isinstance(self.task.parameters, OpenAIChatCompletionParams):
            if self.project.client.openai_client is None:
                raise ValueError(
                    "OpenAI client is not configured. Please set the OPENAI_API_KEY environment variable"
                )
            return Openai(
                client=self.project.client.openai_client,
                prompt=self.task.prompt_template,
                parameters=self.task.parameters,
            )
        elif isinstance(self.task.parameters, AzureOpenAIChatCompletionParams):
            if self.project.client.azure_openai_client is None:
                raise ValueError(
                    "Azure OpenAI client is not configured. Please set the AZURE_OPENAI_API_KEY and AZURE_OPENAI_ENDPOINT environment variables"
                )
            return AzureOpenai(
                client=self.project.client.azure_openai_client,
                prompt=self.task.prompt_template,
                parameters=self.task.parameters,
            )
        else:
            raise ValueError(f"Parameters {self.task.parameters} is not supported")

    def execute(
        self,
        variables: VariablesData,
        group_id: Optional[str] = None,
    ) -> Type["ExecuteResponse"]:
        execute_data = self.llm.execute(self.chat_history, variables)
        next_task = self.project.get_next_task(
            task_id=self.task.id,
            history=execute_data.history,
        )
        # Copy execute history to _live_chat_history
        self._live_chat_history = execute_data.history[:]
        return ExecuteResponse(
            data=execute_data,
            next_task=next_task,
        )
        # TODO log the execute results
        # TODO return the execute results and log results and next task

    def send_function_response(
        self,
        function_response: FunctionResponse,
        variables: Optional[VariablesData] = None,
        group_id: Optional[str] = None,
    ):
        execute_data = self.llm.send_function_response(
            chat_history=self._live_chat_history,
            function_response=function_response,
            variables=variables if variables is not None else {},
        )
        next_task = self.project.get_next_task(
            task_id=self.task.id,
            history=execute_data.history,
        )
        # Copy execute history to _live_chat_history
        self._live_chat_history = execute_data.history[:]
        return ExecuteResponse(
            data=execute_data,
            next_task=next_task,
        )


class NomosProject:
    def __init__(self, client: Type["Nomos"], project_version: ProjectVersion):
        self.client = client
        self.project_version = project_version

    """Gets the first task in the project. Optionally, allows callers to provide a previous chat history to create the first task with.
  This may be useful if the callers workflow separates components into multiple projects and wants to call this project with the history of another.
  """

    def get_first_task(
        self, history: Optional[List[ChatCompletionMessage]] = None
    ) -> Optional[NomosTask]:
        if len(self.project_version.tasks) == 0:
            return None
        return NomosTask(
            project=self,
            task=self.project_version.tasks[0],
            chat_history=history,
        )

    """Given task id and previous history, returns the next task in the project that can be executed with the given history.
  """

    def get_next_task(
        self, task_id: str, history: List[ChatCompletionMessage]
    ) -> Optional[NomosTask]:
        task_index = next(
            (
                index
                for index, task in enumerate(self.project_version.tasks)
                if task.id == task_id
            ),
            None,
        )
        if task_index is None:
            raise ValueError(f"Could not find task with id {task_id}")
        if task_index < len(self.project_version.tasks) - 1:
            return NomosTask(
                project=self,
                task=self.project_version.tasks[task_index + 1],
                chat_history=history,
            )
        return None


class Project:
    def __init__(self, client: Type["Nomos"]):
        self.client = client

    def get(self, project_id: str, branch: Optional[str] = None) -> NomosProject:
        body = (
            ProjectVersionGetActiveRequest(
                project_id=project_id,
                branch_name=branch,
            )
            if branch is not None
            else ProjectVersionGetActiveRequest(project_id=project_id)
        )
        response = self.client.nomos_api.project_version_get_active(body=body)
        project_version = response.body.project_version
        return NomosProject(client=self.client, project_version=project_version)

    def get_version(self, project_version_id: str) -> NomosProject:
        body = ProjectVersionGetRequest(
            project_version_id=project_version_id,
        )
        response = self.client.nomos_api.project_version_get(body=body)
        project_version = response.body.project_version
        return NomosProject(client=self.client, project_version=project_version)


class ExecuteResponse(NamedTuple):
    data: OpenaiExecuteData
    next_task: NomosTask
