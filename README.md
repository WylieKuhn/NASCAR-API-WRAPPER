# NASCAR-API-WRAPPER  
## Features  
### Schedule  
- Get schedule information by year, defaulting to the current year. 
- Get schedule information for the whole season, or just the regular season or playoffs.  
- Get the next race's information.
- Get data on finished races.  
  
### Points
- Get driver points standings.  
- Get owner points standings.  
- Get manufacturer points standings.  
  
### Drivers
- Get info on all NASCAR Drivers.  
  
### Additional Features  
- Option to have data returned as a pandas dataframe, making data analysis easier.  
   
### Usage  
You simply define the api object and call the method for the data you want to retrieve.  
  
For example, to get the season schedule for the current season:  
```python
api = NASCAR_Warapper()
schedule = api.get_season_schedule()
```  
  
To get the data returned as a dataframe simple:
```python
api = NASCARWrapper()
schedule = api.get_season_schedule(as_dataframe=True)
```  
  
You can also next methods as building blocks to get information.  
For instance, to get all the pit stop data for the last race:  
```python
api = NASCARWarpper()
pit_stop_data = api.get_pit_data(as_dataframe=True, series=int(api.get_finished_races()[-1]["series_id"]), race_id=api.get_finished_races()[-1]["race_id"]))
```
