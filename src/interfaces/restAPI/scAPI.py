import requests

class StarCitizenAPI:
    BASE_URL = "https://api.robertsspaceindustries.com"

    @staticmethod
    def get_user(handle):
        url = f"{StarCitizenAPI.BASE_URL}/users/{handle}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def get_organization(sid):
        url = f"{StarCitizenAPI.BASE_URL}/organizations/{sid}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def get_star_citizen_stats():
        url = f"{StarCitizenAPI.BASE_URL}/stats"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
