import sys
import geopandas as gpd
import fiona
import os
import pandas as pd

fiona.supported_drivers['KML'] = 'rw'
my_db_file = r"c:\Users\Robert\Desktop\small.sqlite"

def main():
    inp_file_path = sys.argv[1]
    exp_file_path = sys.argv[2]
    inp_extention = sys.argv[3]
    gdf = gpd.read_file(inp_file_path)
    file_name = os.path.basename(inp_file_path).split('.')[0]
    print(file_name)
    if inp_extention == "csv":
        gdf.to_csv(exp_file_path + "\\" + file_name + ".csv")
    elif inp_extention == 'kml':
        gdf.to_file(exp_file_path + "\\"+file_name+ ".kml", driver = 'KML', CRS = 'EPSG:4326')
    elif inp_extention == 'xlsx':
        df = pd.DataFrame(gdf)
        df.to_excel(exp_file_path + "\\"+file_name+ ".xlsx")
    else:
        return "doesnt support this extention"
if __name__ == '__main__':
    main()

