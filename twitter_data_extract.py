import requests
from env import bearer_token

headers = {"Authorization": f"Bearer {bearer_token}"}

print(headers)

params = {"q": "VW ID.4","expansions": "conversation_id"}

response = requests.get("https://api.twitter.com/2/tweets/search/recent", headers=headers, params=params)

# Check the response status code.
if response.status_code == 200:
    # The request was successful.
    print(response.json())
else:
    # The request failed.
    print(response.status_code)
