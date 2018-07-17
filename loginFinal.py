import os
from slackclient import SlackClient
import json

# publictestng = CBHNJN0SU
slack_token = os.environ.get("xoxp-316442097986-384690204849-388447599778-1c4ce04695c0833be9383ffd2c745a16")
sc = SlackClient("xoxp-316442097986-384690204849-388447599778-1c4ce04695c0833be9383ffd2c745a16")

sc.api_call(
    "chat.postMessage",
    channel="publictesting", #change channel name here
    text="Got the history!"

)

convo = sc.api_call(
    "conversations.history",
    channel="CBHNJN0SU", #for the channel name here, you need to copy the URL and use the ending part which will probably start with a C
	count = 10

)

convo_json = json.dumps(convo, indent=4)

f = open('store_convo', 'w')
f.write(convo_json)
f.close()