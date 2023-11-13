"""
Nomos Advanced Example

### Introduction ###
This example corresponds to the advanced example on the Nomos dashboard. To see
the prompt template being used for this example, please go to:
app.getnomos.com > Examples > 2. Advanced (multiple tasks) project

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

1. Replace <YOUR-NOMOS-ADVANCED-EXAMPLE-PROJECT-ID-HERE> below with the actual project_id.
    You can find your project_id by going to 
    app.getnomos.com > Examples > 2. Advanced (multiple tasks) project
    and copy the project_id at the top of the page.

2. Run with `python3 -m examples.2_advanced`

Note try to specify imports to only the classes you need vs running
```
import nomos *
```
"""

from typing import Optional

from nomos.resources.project import NomosTask
from nomos import Nomos
from pprint import pprint

client = Nomos()

project = client.project.get(
    project_id="<YOUR-NOMOS-ADVANCED-EXAMPLE-PROJECT-ID-HERE>",
)
task: Optional[NomosTask] = project.get_first_task()

pprint("###################### Start of Task 1 ######################")
if task is None:
    raise Exception("No tasks found")

response = task.execute(
    variables={
        "topic": "business marketing",
        "blog_post_1": "How to successfully reinforce your brand",
        "blog_post_2": "How to make your website stand out from your competitors",
    }
)
pprint(response.data)
pprint("###################### End of Task 1 ######################")

pprint("###################### Start of Task 2 ######################")
if response.next_task is None:
    raise Exception("No task 2 found")

response = response.next_task.execute(
    variables={
        "number_of_title_choices": 5,
        "title_additional_requirements": "The title shouldn't be more than five words. Use exactly one emoji at the end.",
    }
)
pprint(response.data)
pprint("###################### End of Task 2 ######################")

pprint("###################### Start of Task 3 ######################")
if response.next_task is None:
    raise Exception("No task 3 found")

response = response.next_task.execute(
    variables={
        "number_of_sections": 5,
    }
)
pprint(response.data)
pprint("###################### End of Task 3 ######################")

if response.next_task is None:
    pprint("No task 4 found")

pprint("###################### Chat History ######################")
pprint(response.data.history)
pprint("###################### End of Chat History ######################")
