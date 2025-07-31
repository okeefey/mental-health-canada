import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="mental_health_canada",     
    user="postgres",      
    password="owen123",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("SELECT region_id FROM regions WHERE name = 'Canada'")
region_id = cur.fetchone()[0]

cur.execute("SELECT demo_id FROM demographics WHERE age_group = '15+' AND gender = 'Men'")
demo_id_men = cur.fetchone()[0]

cur.execute("SELECT demo_id FROM demographics WHERE age_group = '15+' AND gender = 'Women'")
demo_id_women = cur.fetchone()[0]

def insert_data(file_path, demo_id):
    df = pd.read_csv(file_path)

    for _, row in df.iterrows():
        indicator = row["Indicators"]
        year = int(row["YEAR"])
        value_type = row["UOM"]
        value = row["VALUE"]

        # skip missing values
        if pd.isna(value):
            continue

        cur.execute("""
            INSERT INTO mental_health_statistics (indicator, year, region_id, demo_id, value_type, value)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (indicator, year, region_id, demo_id, value_type, value))

    conn.commit()

insert_data("mentalhealthmen.csv", demo_id_men)
insert_data("mentalhealthwomen.csv", demo_id_women)

cur.close()
conn.close()
