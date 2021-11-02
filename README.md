# ais2gpd

A Python utility to query the City of Philadelphia's [Address Information System](https://github.com/CityOfPhiladelphia/ais) (AIS).
Additional documentation on the AIS API is [available here](https://github.com/CityOfPhiladelphia/ais/blob/master/docs/APIUSAGE.md).

## Notes

- AIS currently requires an API key. City of Philadelphia employees can request a key using [these instructions](https://github.com/CityOfPhiladelphia/ais/blob/master/docs/APIUSAGE.md#authentication)
- AIS will only successfully geocode addresses in Philadelphia

## Installation

Via PyPi:

```
pip install ais2gpd
```
# Example

```python
import ais2gpd
import os

# Assuming your AIS API key is stored in an environment variable called `AIS_API_KEY`
ais_key = os.environ['AIS_API_KEY']

# Get the geocoded addresses
gdf = ais2gpd.get(['1234 market st', '945 N 5th st'], ais_key, fields=['zip_code', 'police_district'])

gdf.head()
```
