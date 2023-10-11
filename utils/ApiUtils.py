import requests

from utils.LoggerUtils import LoggerUtils
from utils.ParserUtils import ParserUtils


class ApiUtils:
    __base_url = ParserUtils.parse_json("../resources/config.json")["api_url"]

    @classmethod
    def post(cls, endpoint, body):
        LoggerUtils.info(f"sending post request: {cls.__base_url.format(endpoint)}")
        headers = {"accept": "application/json",
                   "Content-Type": "application/json"}
        return requests.post(cls.__base_url.format(endpoint), data=body, headers=headers)

    @classmethod
    def get(cls, endpoint, params):
        LoggerUtils.info(f"sending post request: {cls.__base_url.format(endpoint)}")
        headers = {"accept": "application/json",
                   "Content-Type": "application/json"}
        return requests.get(cls.__base_url.format(endpoint), params=params, headers=headers)

