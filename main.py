# %%
from shapely.geometry import Point, Polygon
import geopandas as gpd
import geojsonio

# %%
p1 = Point(0, 0)
print(p1)

polygon = Polygon([(0, 0), (1, 1), (1, 0)])

# %%
auStates = gpd.read_file('/Users/xinyanzhang/geojsonData/countries-large.geojson')
print(auStates.head())

auStatesJson = auStates.to_json()
print(auStatesJson)

# %%

# geojsonio.display(auStatesJson)

# %%




