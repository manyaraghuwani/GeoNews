import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(database="GeoNews", 
                        user="postgres", 
                        host="localhost", 
                        password="namami", 
                        port=5432)

cur = conn.cursor()

def select_clusters():
    
    cur.execute('SELECT * FROM clusters;')
    rows = cur.fetchall()

    # Print all clusters from the database
    for row in rows:
        cluster_id, created_date, place_name, latitude, longitude = row
        formatted_date = created_date.strftime('%Y-%m-%d %H:%M:%S')  # Format datetime to 'YYYY-MM-DD HH:MM:SS'
        print(f"{cluster_id}, {formatted_date}, {place_name}, {latitude}, {longitude}")


def insert_cluster(place_name, latitude, longitude):

    cur.execute("SELECT COUNT(*) FROM clusters WHERE place_name = %s;", (place_name,))
    count = cur.fetchone()[0]

    if count == 0:
        insert_query = """
        INSERT INTO clusters (place_name, latitude, longitude)
        VALUES (%s, %s, %s);
        """
        cur.execute(insert_query, (place_name, latitude, longitude))
        conn.commit()
        print(f"{place_name} cluster inserted successfully.")
    else:
        print(f"{place_name} cluster already exists in the database.")

    # Close the cursor and connection
    cur.close()
    conn.close()


