import json
import re


class ParserUtils:

    @staticmethod
    def parse_json(path):
        f = open(path)
        data = json.load(f)
        f.close()
        return data

    @staticmethod
    def parse_link(text):
        url_pattern = r'https?://\S+|www\.\S+'
        links = re.findall(url_pattern, text)
        return links
