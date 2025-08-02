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

df = pd.read_csv("data/mental_health_dataset.csv")  

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO mental_health_survey (
            age, gender, employment_status, work_environment,
            mental_health_history, seeks_treatment, stress_level,
            sleep_hours, physical_activity_days, depression_score,
            anxiety_score, social_support_score, productivity_score,
            mental_health_risk
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['age'], row['gender'], row['employment_status'], row['work_environment'],
        row['mental_health_history'], row['seeks_treatment'], row['stress_level'],
        row['sleep_hours'], row['physical_activity_days'], row['depression_score'],
        row['anxiety_score'], row['social_support_score'], row['productivity_score'],
        row['mental_health_risk']
    ))

conn.commit()

group_stats = df.groupby('gender')[['depression_score', 'anxiety_score']].mean()
print(group_stats)

treatment_counts = df['seeks_treatment'].value_counts()
print(treatment_counts)


cur.close()
conn.close()
