import sys
import geopandas as gpd
import fiona
import os
import pandas as pd

fiona.supported_drivers['KML'] = 'rw'
my_db_file = r"c:\Users\Robert\Desktop\small.sqlite"

def main():
    gdf = gpd.read_file(sys.argv[1])
    file_name = os.path.basename(sys.argv[1]).split('.')[0]
    print(file_name)
    if sys.argv[3] == "csv":
        gdf.to_csv(f"c:\\Users\\Robert\\Desktop\\Geo_data\\{file_name}.csv")
    elif sys.argv[3] == 'kml':
        gdf.to_file(f"c:\\Users\\Robert\\Desktop\\Geo_data\\{file_name}.kml", driver = 'KML', CRS = 'EPSG:4326')
    elif sys.argv[3] == 'xlsx':
        df = pd.DataFrame(gdf)
        df.to_excel(f"c:\\Users\\Robert\\Desktop\\Geo_data\\{file_name}.xlsx")
    else:
        return "doesnt support this extention"
if __name__ == '__main__':
    main()

