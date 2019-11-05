# %% gallery

# sphinx_gallery_thumbnail_number = 3
import geopandas
import matplotlib.pyplot as plt
import pandas as pd

df = geopandas.read_file(geopandas.datasets.get_path('nybb'))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

# %% plot

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.head()
world.to_file("worldTest.geojson", driver='GeoJSON')

world.plot()
world.geometry.name  # follow the name
world.geometry
world = world.rename(columns={'geometry': 'borders'})
world = world.set_geometry('borders')

world['centroid_column'] = world.centroid  # default work on geometry column
world = world.set_geometry('centroid_column')
continents = world.dissolve(by='continent')
world.plot()
continents.plot()

continents = world.dissolve(by='continent', aggfunc='sum')
continents.plot(column='pop_est', scheme='quantiles', cmap='YlOrRd')

# %%
from shapely.geometry import Point, Polygon
import geopandas
import geojsonio

p1 = Point(0, 0)
print(p1)

polygon = Polygon([(0, 0), (1, 1), (1, 0)])

auStates = geopandas.read_file('/Users/xinyanzhang/geojsonData/australian-suburbs-large.geojson')
print(auStates.head())
ax = auStates.plot()

auStatesJson = auStates.to_json()
print(auStatesJson)

auStatesT = auStates[['loc_pid','lc_ply_pid','geometry']]
auStatesT.geometry.isna().sum()
auStatesT.geometry.is_empty.sum()

aud = pd.DataFrame(auStatesT)

auStatesT['province'] = auStatesT['loc_pid'].str.slice(0,2)

province = auStatesT[~(auStatesT.geometry.is_empty | auStatesT.geometry.isna())]
province['geometry'] = province.buffer(0.01)  # self intersecting

grouped = province.dissolve(by='province',aggfunc='sum')
grouped.plot()
grouped.plot(column='lc_ply_pid', scheme='quantiles', cmap='YlOrRd')

# %%

# geojsonio.display(auStatesJson)

# %%

plt.show()
