# ais2gpd

A Python utility to query the City of Philadelphia's [Address Information System](https://github.com/CityOfPhiladelphia/ais) (AIS).
Additional documentation on the AIS API is [available here](https://github.com/CityOfPhiladelphia/ais/blob/master/docs/APIUSAGE.md).

**Note:** AIS currently requires an API key. City of Philadelphia employees can request a key using [these instructions](https://github.com/CityOfPhiladelphia/ais/blob/master/docs/APIUSAGE.md#authentication)

# Example

```python
import ais2gpd
import os

ais_key = os.environ['AIS_API_KEY']
gdf = ais2gpd.get(['1234 market st', '945 N 5th st'], ais_key, fields=['zip_code', 'police_district'])

gdf.head()
```
