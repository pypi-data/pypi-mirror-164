from .google_play_scraper import reviews_all, Sort
from typing import Optional
from datetime import datetime, timedelta
import json


class GetReviews:
    def __init__(self) -> None:
        pass

    def today(self, app_name):
        tday = datetime.today().strftime("%d%m%Y")
        resp = reviews_all(app_id=app_name, today=True)

        with open(f"{app_name}_{tday}_data.json", "w") as json_file:
            json.dump(resp, json_file)
        return resp

    def yesterday(self, app_name):
        tday = datetime.today()
        yday = (tday - timedelta(days=1)).strftime("%d%m%Y")
        resp = reviews_all(app_id=app_name, yesterday=True)

        with open(f"{app_name}_{yday}_data.json", "w") as json_file:
            json.dump(resp, json_file)
        return resp

    def hourly(self, app_name):
        hstr = datetime.today().strftime("%d%m%Y_%H%M%S")
        resp = reviews_all(app_id=app_name, hour=True)

        with open(f"{app_name}_{hstr}_data.json", "w") as json_file:
            json.dump(resp, json_file)
        return resp
