import psycopg2
import geopandas as gpd
con_database="postgres",
con_user="postgres",
con_password="masis22016",
con_host="localhost",
con_port = 5432,
conn = None
cur = None 




def main():
    try:
        cur.execute(table_create)
        conn.commit()
        
    except:
        raise Exception("Sorry, you have problem in your code or table already exists")
    finally:
        cur.close()
        conn.close()
    print("hello1")
if __name__ == "__main__":
    conn = psycopg2.connect(database="postgres", user="postgres", password="masis22016", host="localhost", port="5432")
    cur = conn.cursor()

    table_create = "CREATE TABLE locations_table(id INT PRIMARY KEY, x_coordinate DOUBLE PRECISION, y_coordinate DOUBLE PRECISION, geom geometry)"
    main()