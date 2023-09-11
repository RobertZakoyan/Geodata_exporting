import psycopg2
import geopandas as gpd
import pandas as pd 
from sqlalchemy import create_engine
from shapely.geometry import box
from shapely import wkb
import matplotlib.pyplot as plt

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

print(gdf[['x_min', 'y_min', 'x_max', 'y_max']])
fig, ax = plt.subplots(figsize=(10, 10))
gdf.boundary.plot(ax=ax, color='blue', linewidth=2)

# Plot the road data (assuming you have a GeoDataFrame 'road_gdf' containing road geometries)
# road_gdf.plot(ax=ax, color='red', linewidth=1)

# Customize the plot as needed
ax.set_aspect('equal')
ax.set_title('Bounding Boxes and Road Data')
plt.show()
# connection = psycopg2.connect(database="postgres", user="postgres", password="masis22016", host="localhost", port="5432")
# query = "SELECT * FROM road_data"
# df = pd.read_sql_query(query, connection)
# print(df)


# def main():
#     try:
#         cur.execute(table_create)
#         conn.commit()
        
#     except:
#         raise Exception("Sorry, you have problem in your code or table already exists")
#     finally:
#         cur.close()
#         conn.close()
#     print("hello1")
# if __name__ == "__main__":

#     con_database="postgres",
#     con_user="postgres",
#     con_password="masis22016",
#     con_host="localhost",
#     con_port = 5432,
#     conn = None
#     cur = None
#     conn = psycopg2.connect(database="postgres", user="postgres", password="masis22016", host="localhost", port="5432")
#     cur = conn.cursor()

#     table_create = "CREATE TABLE locations_table(id INT PRIMARY KEY, x_coordinate DOUBLE PRECISION, y_coordinate DOUBLE PRECISION, geom geometry)"
#     main()