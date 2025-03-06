import requests

class XHRRequest:
    @staticmethod
    def get(url, params=None, headers=None):
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def post(url, data=None, json=None, headers=None):
        response = requests.post(url, data=data, json=json, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def put(url, data=None, json=None, headers=None):
        response = requests.put(url, data=data, json=json, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def delete(url, headers=None):
        response = requests.delete(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
