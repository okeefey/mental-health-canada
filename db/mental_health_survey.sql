DROP TABLE IF EXISTS mental_health_survey;


CREATE TABLE mental_health_survey (
    id SERIAL PRIMARY KEY,
    age INTEGER,
    gender VARCHAR(20),
    employment_status VARCHAR(50),
    work_environment VARCHAR(100),
    mental_health_history VARCHAR(100),
    seeks_treatment BOOLEAN,
    stress_level INTEGER,
    sleep_hours INTEGER,
    physical_activity_days INTEGER,
    depression_score INTEGER,
    anxiety_score INTEGER,
    social_support_score INTEGER,
    productivity_score INTEGER,
    mental_health_risk VARCHAR(20)
);

SELECT gender, AVG(depression_score) AS avg_depression, AVG(anxiety_score) AS avg_anxiety
FROM mental_health_survey
GROUP BY gender;

SELECT seeks_treatment, COUNT(*) AS count
FROM mental_health_survey
GROUP BY seeks_treatment;

