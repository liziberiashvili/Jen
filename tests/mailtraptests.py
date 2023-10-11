import re
from urllib.parse import parse_qs, urlparse

import requests

from utils.ParserUtils import ParserUtils

account_id = 1646936
header = {"Api-Token": "101f74fd12864023949365bf4f39d30f"}
response = requests.get(f"https://mailtrap.io/api/accounts/{account_id}/inboxes", headers=header)

response_json = response.json()
inbox_id = response_json[0]["id"]

message_response = requests.get(f"https://mailtrap.io/api/accounts/{account_id}/inboxes/{inbox_id}/messages", headers=header)
message_id = message_response.json()[0]["id"]

email_show_response = requests\
    .get(f"https://mailtrap.io/api/accounts/{account_id}/inboxes/{inbox_id}/messages/{message_id}", headers=header)

print(email_show_response.text)

message_source_response = requests\
    .get(f"https://mailtrap.io/api/accounts/{account_id}/inboxes/{inbox_id}/messages/{message_id}/body.htmlsource",
         headers=header)

url_list = ParserUtils.parse_link(message_source_response.text)
url = [string for string in url_list if "localhost" in string][0]
print(url)
parsed_url = urlparse(url)

query_params = parse_qs(parsed_url.query)

customer_id = query_params.get('customer_id', [None])[0]
remember_token_pattern = r'remember_token=([^&]+)'
match = re.search(remember_token_pattern, url)
remember_token = match.group(1) if match else None

print("Customer ID:", customer_id)
print("Remember Token:", remember_token)