import re
from urllib.parse import urlparse, parse_qs

from utils.MailTrapUtils import MailTrapUtils
from utils.ParserUtils import ParserUtils


class YouthStepsAPI:
    @classmethod
    def get_approval_url(cls):
        url_list = ParserUtils.parse_link(MailTrapUtils.get_source_response())
        url = [string for string in url_list if "localhost" in string][0]
        return url

    @classmethod
    def get_customer_id(cls):
        parsed_url = urlparse(cls.get_approval_url())
        query_params = parse_qs(parsed_url.query)
        customer_id = query_params.get("customer_id", [None])[0]
        return customer_id

    @classmethod
    def get_remember_token(cls):
        remember_token_pattern = r'remember_token=([^&]+)'
        match = re.search(remember_token_pattern, cls.get_approval_url())
        remember_token = match.group(1) if match else None
        return remember_token
