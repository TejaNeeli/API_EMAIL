import requests
import configparser
import os

class APIClient:
    def __init__(self, env='QA'):
        self.config = configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, 'config', 'config.ini')
        self.config.read(config_path)
        self.base_url_1 = self.config.get(env, "url_1")
        self.base_url_2 = self.config.get(env, "url_2")
        self.base_url_3 = self.config.get(env, "url_3")
        self.timeout = int(self.config.get(env, "timeout"))
        self.headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IkFQUExFX1RFSkEiLCJuYW1laWQiOiI1NDM3OCIsIm5iZiI6MTc4NDIwMzcwNCwiZXhwIjoxNzg0MjkwMTA0LCJpYXQiOjE3ODQyMDM3MDQsImlzcyI6InNlbGYiLCJhdWQiOiJodHRwOi8vd3d3Lm9yYmNvbW0uY29tIn0.WJ3Ubvle4Tmrv6ZXumhNbWL1-edfLIcFDYnuFrL4CXM"
        }

    def get_api_1(self, endpoint):
        url = f"{self.base_url_1}?{endpoint}" if not self.base_url_1.endswith("?") else f"{self.base_url_1}{endpoint}"
        response = requests.get(url, headers=self.headers, timeout=self.timeout)
        return response

    def get_api_2(self, payload):
        url = f"{self.base_url_2}"
        response = requests.post(url, json= payload, headers=self.headers, timeout=self.timeout)
        return response

    def get_api_3(self, endpoint):
        url = f"{self.base_url_3}?{endpoint}" if not self.base_url_3.endswith("?") else f"{self.base_url_3}{endpoint}"
        response = requests.get(url, headers=self.headers, timeout=self.timeout)
        return response


