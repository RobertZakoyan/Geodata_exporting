import psycopg2
print("hello1")
con_database="postgres",
con_user="postgres",
con_password="masis22016",
con_host="localhost",
con_port = 5432,
conn = None
cur = None  
table_read = "SELECT * FROM road_data"
table_create = "CREATE TABLE locations_table(id INT PRIMARY KEY, x_coordinate DOUBLE PRECISION, y_coordinate DOUBLE PRECISION, geom GEOMETRY)"
try:
    conn = psycopg2.connect(database=con_database, user="postgres", password="masis22016", host="localhost", port="5432")

    cur = conn.cursor()

    cur.execute(table_create)
    conn.commit()
    
except:
    raise Exception("Sorry, you have problem in your code")
finally:
    cur.close()
    conn.close()
print("hello1")
# if __name__ == "__main__":
#     table_create = "CREATE TABLE public.locations_table(id INT PRIMARY KEY, x_coordinate DOUBLE PRECISION, y_coordinate DOUBLE PRECISION, geom GEOMERTY)"
    
    
#     main()
