import pandas as pd
from datetime import datetime
import requests
import json



class NASCARWarpper:
    def __init__(self):
        self.data = None

    def get_season_schedule(self, year=datetime.now().year, series=1, as_dataframe=False):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{year}/race_list_basic.json")

            if as_dataframe:
                schedule = pd.json_normalize(response.json()[f"series_{series}"])
                return schedule
            else:
                data = response.json()
                return data[f"series_{series}"]

        except Exception as e:
            return e

    def get_next_race(self, as_dataframe=False):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{datetime.now().year}/race_list_basic.json")
            response = response.json()

            next_races = []

            for race in response["series_3"]:
                if datetime.fromisoformat(race["race_date"]) > datetime.now():
                    next_races.append(race)
                    break

            for race in response["series_2"]:
                if datetime.fromisoformat(race["race_date"]) > datetime.now():
                    next_races.append(race)
                    break

            for race in response["series_1"]:
                if datetime.fromisoformat(race["race_date"]) > datetime.now():
                    next_races.append(race)
                    break

            next_race = sorted(next_races, key=lambda entry: datetime.fromisoformat(entry['race_date']))
            return next_race[0]

        except Exception as e:
            return e

    def get_finished_races(self, as_dataframe=False, year=datetime.now().year, series=1):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{year}/race_list_basic.json")
            response = response.json()
            past_races = []

            for race in response[f"series_{series}"]:
                if datetime.fromisoformat(race["race_date"]) < datetime.now():
                    past_races.append(race)

            if as_dataframe:
                return pd.DataFrame(past_races)
            else:
                return past_races

        except Exception as e:
            return e

    def get_regular_season_races(self, as_dataframe=False, year=datetime.now().year, series=1):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{year}/race_list_basic.json")
            response = response.json()

            races = []

            for race in response[f"series_{series}"]:
                if race["playoff_round"] == 0:
                    races.append(race)

            if as_dataframe:
                return pd.DataFrame(races)
            else:
                return races

        except Exception as e:
            return e

    def get_playoff_races(self, as_dataframe=False, year=datetime.now().year, series=1):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{year}/race_list_basic.json")
            response = response.json()

            races = []

            for race in response[f"series_{series}"]:
                if race["playoff_round"] > 0:
                    races.append(race)

            if as_dataframe:
                return pd.DataFrame(races)
            else:
                return races

        except Exception as e:
            return e

    def get_race_results(self, race_id, as_dataframe=False, year=datetime.now().year, series=1):
        try:
            response = requests.get(f"https://cf.nascar.com/data/cacher/production/{year}/{series}/{race_id}/raceResults.json")
            response = response.json()

            if as_dataframe:
                return pd.DataFrame(response)
            else:
                return response

        except Exception as e:
            return e

    def get_points_standings(self, as_dataframe=False, year=datetime.now().year, series=1):
        try:
            response = requests.get(f"https://cf.nascar.com/data/cacher/production/{year}/{series}/racinginsights-points-feed.json")
            response = response.json()
            if as_dataframe:
                return pd.DataFrame(response)
            else:
                return response

        except Exception as e:
            return e

    def all_drivers_info(self, as_dataframe=False):
        try:
            response = requests.get("https://cf.nascar.com/cacher/drivers.json")
            response = response.json()

            if as_dataframe:
                return pd.DataFrame(response)

            else:
                return response
        except Exception as e:
            return e

    def get_owners_points(self, as_dataframe=False, year=datetime.now().year, series=1):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{year}/{series}/final/{series}-owners-points.json")
            response = response.json()

            if as_dataframe:
                return pd.DataFrame(response)
            else:
                return response

        except Exception as e:
            return e

    def get_manufacturer_points(self, as_dataframe=False, year=datetime.now().year, series=1):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{year}/{series}/final/{series}-manufacturer-points.json")
            response = response.json()

            if as_dataframe:
                return pd.DataFrame(response)
            else:
                return response

        except Exception as e:
            return e

#In progress
    def get_current_race(self):
        try:
            response = requests.get(f"https://cf.nascar.com/cacher/{datetime.now().year}/race_list_basic.json")
            response = response.json()

            current_time = datetime.now()
            current_race = None

            for series_name in ["series_1", "series_2", "series_3"]:
                if series_name in response:
                    for race in response[series_name]:
                        if datetime.fromisoformat(race["race_date"]) < current_time and race["winner_driver_id"] == None:
                            current_race = race
                            return current_race
                if current_race is None:
                    next_race = self.get_next_race()
                    return f"No current race, the next race is the {next_race['race_name']} on {datetime.fromisoformat(next_race['race_date'])}"

        except Exception as e:
            return e


