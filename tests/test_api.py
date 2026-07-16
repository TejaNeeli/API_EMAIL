from utils.api_client import APIClient
import pytest
import json
import os

class TestAPI:
    def api(self):
        return APIClient()

    @pytest.mark.smoke
    @pytest.mark.parametrize("iteration", range(10))
    def test_getapi_1(self, iteration):
        endpoint = 'email=APPLE_TEJA'
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # data_path = os.path.join(base_dir, 'data', 'api_data.json')
        # with open(data_path) as f:
        #     data = json.load(f)
        # payload = data['value']
        result = self.api().get_api_1(endpoint)
        assert result.status_code == 200
        return result.json()

    @pytest.mark.parametrize("iteration", range(50))
    def test_postapi_2(self, iteration):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, 'data', 'api_data.json')
        with open(data_path) as f:
            data = json.load(f)
        payload = data['value_1']
        result = self.api().get_api_2(payload= payload)
        assert result.status_code == 200
        return result.json()

    @pytest.mark.parametrize("iteration", range(10))
    def test_postapi_3(self, iteration):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, 'data', 'api_data.json')
        with open(data_path) as f:
            data = json.load(f)
        payload = data['value']
        result = self.api().get_api_3(endpoint=None)
        assert result.status_code == 200
        return result.json()
