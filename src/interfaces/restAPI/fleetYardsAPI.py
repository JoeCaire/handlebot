import requests

class FleetYardsAPI:
    BASE_URL = "https://api.fleetyards.net/v1"

    @staticmethod
    def get_ship(ship_name):
        url = f"{FleetYardsAPI.BASE_URL}/models/{ship_name.lower().replace(' ', '-')}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    @staticmethod
    def get_all_ships_name():
        url = f"{FleetYardsAPI.BASE_URL}/models/slugs"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
