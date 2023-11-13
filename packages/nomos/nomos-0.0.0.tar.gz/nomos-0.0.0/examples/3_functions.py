"""
Nomos Simple Example

### Introduction ###
This example corresponds to the simple example on the Nomos dashboard. To see
the prompt template being used for this example, please go to:
app.getnomos.com > Examples > 1. Simple (one task) project

### Setting NOMOS_CLIENT_ID, NOMOS_SECRET, and OPENAI_API_KEY ###
There are two ways to set NOMOS_CLIENT_ID, NOMOS_SECRET, and OPENAI_API_KEY. 
You can choose the best option for your application:

1. Set them as environment variables:
    export NOMOS_CLIENT_ID=<YOUR-NOMOS-CLIENT-ID>
    export NOMOS_SECRET=<YOUR-NOMOS-SECRET-KEY>
    export OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>

2. When initializing the Nomos client, pass them as arguments:
    const client = Nomos(
      client_id="<YOUR-NOMOS-CLIENT-ID>",
      secret="<YOUR-NOMOS-SECRET-KEY>",
      openai_api_key="<YOUR-OPENAI-API-KEY>",
    );

### Let's run the example! ###
To run the example, follow the steps below:

1. Replace <YOUR-NOMOS-SIMPLE-EXAMPLE-PROJECT-ID-HERE> below with the actual project_id.
    You can find your project_id by going to 
    app.getnomos.com > Examples > 1. Simple (one task) project
    and copy the project_id at the top of the page.

2. Run with `python3 -m examples.1_simple`

Note try to specify imports to only the classes you need vs running
```
import nomos *
```
"""

from typing import Optional

from nomos.resources.providers.types import FunctionResponse


from nomos.resources.project import NomosTask
from nomos import Nomos
from pprint import pprint

client = Nomos()

project = client.project.get(
    project_id="<YOUR-NOMOS-SIMPLE-EXAMPLE-PROJECT-ID-HERE>",
)
task: Optional[NomosTask] = project.get_first_task()

pprint("###################### Start of Task 1 ######################")
if task is None:
    raise Exception("No tasks found")

response = task.execute(
    variables={
        "state": "california",
    }
)
pprint(response.data)
pprint("###################### End of Task 1 ######################")

pprint("###################### Send Function Response ######################\n")
if response.data.completion.choices[0].message.function_call is None:
    raise Exception("No function call found")

response = task.send_function_response(
    function_response=FunctionResponse(
        name=response.data.completion.choices[0].message.function_call.name,
        response="80 degress F",
    ),
)
pprint(response.data)

pprint("###################### Chat History ######################")
pprint(response.data.history)
pprint("###################### End of Chat History ######################")
