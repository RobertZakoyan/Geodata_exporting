import psycopg2
import geopandas as gpd
import pandas as pd 
from sqlalchemy import create_engine
from shapely.geometry import box
from shapely import wkb
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from shapely.geometry import Polygon

db_path = r"c:\Users\Robert\Desktop\road_data.sql"
engine = create_engine('postgresql://postgres:masis22016@localhost:5432/postgres')
query = 'SELECT * FROM road_data'
df = pd.read_sql(query, engine)
df['geometry'] = df['geom'].apply(lambda wkb_data: wkb.loads(bytes.fromhex(wkb_data)) if wkb_data else None)
gdf = gpd.GeoDataFrame(df, geometry='geometry')

gdf['bounding_box'] = gdf['geometry'].envelope

# Extract x and y coordinates of the bounding boxes
gdf['x_min'] = gdf['bounding_box'].apply(lambda box: box.bounds[0] if box else None)
gdf['y_min'] = gdf['bounding_box'].apply(lambda box: box.bounds[1] if box else None)
gdf['x_max'] = gdf['bounding_box'].apply(lambda box: box.bounds[2] if box else None)
gdf['y_max'] = gdf['bounding_box'].apply(lambda box: box.bounds[3] if box else None)

fig, ax = plt.subplots(figsize=(8, 8))


gdf.boundary.plot(ax=ax, color="red", linewidth=2)


ax.set_aspect('equal')


ax.set_xlim(gdf['x_min'].min() - 1000, gdf['x_max'].max() + 1000)
ax.set_ylim(gdf['y_min'].min() - 1000, gdf['y_max'].max() + 1000)


plt.show()


