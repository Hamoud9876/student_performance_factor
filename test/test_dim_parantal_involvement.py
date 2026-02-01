from utils.dim_perental_involvement import dim_parental_involvement
import pytest
import pandas as pd
from io import StringIO

@pytest.fixture(scope="function")
def create_df():
    csv_data = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score
23,84,Low,High,No,7,73,Low,Yes,0,Low,Medium,Public,Positive,3,No,High School,Near,Male,67
19,64,Medium,Medium,No,8,59,Low,Yes,2,Medium,Medium,Public,Negative,4,No,College,Moderate,Female,61"""
    return pd.read_csv(StringIO(csv_data))


class TestUnit:
    def test_handle_wrong_input(self, create_df, caplog):
        response = dim_parental_involvement("hello")

        assert response is None
        assert "Wrong df input" in caplog.text


    def test_return_new_df(self, create_df):
        response = dim_parental_involvement(create_df)

        assert response is not create_df
    
    def test_missing_pi_column(self, create_df,caplog):
        df = pd.DataFrame({"SomeColumn": [1, 2, 3]})
        response = dim_parental_involvement(df)

        assert response is None
        assert "error while transforming unique parental involvement" in caplog.text

        df = pd.DataFrame({})
        response = dim_parental_involvement(df)

        assert response is None
        assert "error while transforming unique parental involvement" in caplog.text


    def test_return_unique_values(self, create_df):
        response = dim_parental_involvement(create_df)

        assert response.shape[0] == 2


    def test_return_correct_values(self,create_df ):
        response = dim_parental_involvement(create_df)

        assert set(response["parental_involvement"]).issubset({"High", "Medium", "Low"})


    def test_output_column_name(self, create_df):
        result = dim_parental_involvement(create_df)

        assert list(result.columns) == ["parental_involvement"]

