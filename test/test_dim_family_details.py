from utils.dim_family_details import dim_family_details
import pytest
import pandas as pd
from io import StringIO

@pytest.fixture(scope="function")
def create_df():
    csv_data = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score
23,84,Low,High,No,7,73,Low,Yes,0,Low,Medium,Public,Positive,3,No,High School,Near,Male,67
19,64,Medium,Medium,Yes,8,59,Low,No,2,Medium,Medium,Private,Negative,4,Yes,College,Moderate,Female,61"""
    return pd.read_csv(StringIO(csv_data))


class TestUnit:
    def test_handle_wrong_input(self, create_df, caplog):
        response = dim_family_details("hello")

        assert response is None
        assert "Wrong df input" in caplog.text


    def test_return_new_df(self, create_df):
        response = dim_family_details(create_df)

        assert response is not create_df
    
    def test_logs_error(self, create_df,caplog):
        #parental education level
        df = pd.DataFrame({"family_income": ["Low", "Medium"]})
        response = dim_family_details(df)

        assert response is None
        assert "error while retrieving parental education" in caplog.text

        df = pd.DataFrame({"Parental_Education_Level": ["High School", "College"]})
        response = dim_family_details(df)

        assert response is None
        assert "error while retrieving family income" in caplog.text


        


    def test_return_unique_values(self, create_df):
        response = dim_family_details(create_df)

        assert response.shape[0] == 2


    def test_return_correct_values(self,create_df ):
        response = dim_family_details(create_df)
        
        assert set(response["parental_education_level"]).issubset({"High School","College"})
        assert set(response["family_income"]).issubset({"Low","Medium"})


    def test_output_column_name(self, create_df):
        result = dim_family_details(create_df)

        assert list(result.columns) == ["parental_education_level","family_income"]

