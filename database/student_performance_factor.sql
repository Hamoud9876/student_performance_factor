CREATE TABLE "student_performance_fact" (
  "student_record_id" SERIAL PRIMARY KEY,
  "hours_studied" int,
  "attendance" int,
  "tutoring_sessions" int,
  "sleep_hours" int,
  "previous_score" int,
  "exam_score" int,
  "gender_id" int,
  "parental_involvement_id" int,
  "motivation_level_id" int,
  "internet_access_id" int,
  "learning_disabilities_id" int,
  "access_to_resources_id" int,
  "peer_influence_id" int,
  "family_details_id" int,
  "extracurricular_activities_id" int
);

CREATE TABLE "school_type_performance_fact" (
  "school_record_id" SERIAL PRIMARY KEY,
  "school_type" varchar(50),
  "average_students_score" decimal,
  "teacher_quality_id" int
);

CREATE TABLE "dim_parental_involvement" (
  "parental_involvement_id" SERIAL PRIMARY KEY,
  "involvement_level" varchar(30)
);

CREATE TABLE "dim_access_to_resources" (
  "access_to_resources_id" SERIAL PRIMARY KEY,
  "access_to_resources" varchar(30)
);

CREATE TABLE "dim_extracurricular_activities" (
  "extracurricular_activities_id" SERIAL PRIMARY KEY,
  "enrolled" varchar(20)
);

CREATE TABLE "dim_motivation_level" (
  "motivation_level_id" SERIAL PRIMARY KEY,
  "motivation_level" varchar(30)
);

CREATE TABLE "dim_internet_access" (
  "internet_access_id" SERIAL PRIMARY KEY,
  "internet_access" varchar(30)
);

CREATE TABLE "dim_teacher_quality" (
  "teacher_quality_id" SERIAL PRIMARY KEY,
  "teacher_quality" varchar(30)
);

CREATE TABLE "dim_school_type" (
  "school_Type_id" SERIAL PRIMARY KEY,
  "school_type" varchar(30)
);

CREATE TABLE "dim_peer_influence" (
  "peer_influence_id" SERIAL PRIMARY KEY,
  "peer_influence" varchar(30)
);

CREATE TABLE "dim_learning_disabilities" (
  "learning_disabilities_id" SERIAL PRIMARY KEY,
  "learning_disabilities" varchar(20)
);

CREATE TABLE "dim_family_details" (
  "family_details_id" SERIAL PRIMARY KEY,
  "parental_education_level" varchar(50),
  "family_income" varchar(30)
);

CREATE TABLE "dim_gender" (
  "gender_id" SERIAL PRIMARY KEY,
  "gender" varchar(20)
);

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("gender_id") REFERENCES "dim_gender" ("gender_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("parental_involvement_id") REFERENCES "dim_parental_involvement" ("parental_involvement_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("motivation_level_id") REFERENCES "dim_motivation_level" ("motivation_level_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("internet_access_id") REFERENCES "dim_internet_access" ("internet_access_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("learning_disabilities_id") REFERENCES "dim_learning_disabilities" ("learning_disabilities_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("access_to_resources_id") REFERENCES "dim_access_to_resources" ("access_to_resources_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("peer_influence_id") REFERENCES "dim_peer_influence" ("peer_influence_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("family_details_id") REFERENCES "dim_family_details" ("family_details_id");

ALTER TABLE "student_performance_fact" ADD FOREIGN KEY ("extracurricular_activities_id") REFERENCES "dim_extracurricular_activities" ("extracurricular_activities_id");

ALTER TABLE "school_type_performance_fact" ADD FOREIGN KEY ("teacher_quality_id") REFERENCES "dim_teacher_quality" ("teacher_quality_id");
