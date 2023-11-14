# import openai
import plotly.express as px
import requests
from bs4 import BeautifulSoup
import json
import gandai as ts

from openai import OpenAI

client = OpenAI(
    api_key=ts.secrets.access_secret_version("OPENAI_KEY"),
)

## gpt4


def ask_gpt4(messages: list) -> str:
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4",
        temperature=0.0
    )
    #
    print(chat_completion.usage)
    return chat_completion.choices[0].message.content

# def ask_gpt35(messages: list):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-16k", messages=messages, temperature=0.0
#     )
#     print(response['usage'])
#     return response.choices[0]["message"]["content"]


# ## gpt3


# def ask_gpt(prompt: str, max_tokens: int = 60):
#     response = openai.Completion.create(
#         engine="text-davinci-003",  # or "text-curie-003" for a less expensive engine
#         prompt=prompt,
#         max_tokens=max_tokens,
#     )

#     return response.choices[0].text.strip()


# def get_top_zip_codes(area: str, top_n: int = 25) -> list:
#     resp = ask_gpt(
#         f"As a python array List[str], the top {top_n} zip codes in {area} are:",
#         max_tokens=1000,
#     )
#     return eval(resp)[0:top_n]  # top_n of 1 was giving me a ton of results



HOW_TO_RESPOND = """
You will respond with an JSON object that looks like this:
{
    "events": List[Event],
}
"""

HOW_TO_IMPORT = """
// example Import(Event)
{
    "search_uid": 19696114,
    "domain": null,
    "actor_key": "4805705555",
    "type": "import",
    "data": {
        "stage": "advance",
        "domains": [
            "buybits.com",
            "lidoradio.com",
            "rocklandcustomproducts.com",
            "sigmasafety.ca",
        ],
    },
}

Here are the stages along with their labels:
The only valid stages are labelMap.keys()
const labelMap = {
    "create": "Inbox",
    "advance": "Review",
    "validate": "Validated",
    "send": "Client Inbox",
    "client_approve": "Client Approved",
    "sync": "Synced",
    "reject": "Reject",
    "conflict": "Conflict",
    "client_conflict": "Client Conflict",
    "client_reject": "Client Reject"
}
"""

HOW_TO_TRANSITION = """
To move a target to a different stage you will create an event with the targets domain and the stage you want to move it to.

// example Event
{
    "search_uid": 19696114,
    "domain": "acme.com",
    "actor_key": "7138248581",
    "type": "send",
    "data": {
        "prompt": "SAVE USER PROMPT HERE",
    },
}


Here are the stages along with their labels:
The only valid event types are the labelMap.keys()
const labelMap = {
    "create": "Inbox",
    "advance": "Review",
    "validate": "Validated",
    "send": "Client Inbox",
    "client_approve": "Client Approved",
    "sync": "Synced",
    "reject": "Reject",
    "conflict": "Conflict",
    "client_conflict": "Client Conflict",
    "client_reject": "Client Reject"
}
"""

HOW_TO_GOOGLE = """

To search Google, you will create an Event object.

@dataclass
class Google(Event):
    search_uid: int  # fk # add index
    actor_key: str  # fk
    type: str  
    data: dict = field(default_factory=dict)
    id: int = field(default=None)  # pk
    # created: int = field(init=False)

List[Event] examples asdict:

[{
  'search_uid': 200,
  'domain': null,
  'actor_key': '3125740050',
  'type': 'google',
  'data': {'q': '"golf cart" AND audio'},
  'created': 1697813193},
{
  'search_uid': 5255570,
  'domain': null,
  'actor_key': '3102835279',
  'type': 'google',
  'data': {'q': '"commercial" AND "door" AND ("repair" OR "maintenance" OR "replacement") AND "new York City"'},
  'created': 1697814555}]

The type is 'google'
You will not set the id or created fields.
The default count is 10

"""