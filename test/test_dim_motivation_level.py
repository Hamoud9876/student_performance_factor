from utils.dim_motivation_level import dim_motivation_level
import pytest
from io import StringIO
import pandas as pd


@pytest.fixture(scope="function")
def create_df():
    csv_data = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score
23,84,Low,High,No,7,73,Low,Yes,0,Low,Medium,Public,Positive,3,No,High School,Near,Male,67
19,64,Low,Medium,No,8,59,Medium,Yes,2,Medium,High,Public,Negative,4,No,College,Moderate,Female,61
19,64,Low,Medium,No,8,59,High,Yes,2,Medium,Low,Public,Negative,4,No,College,Moderate,Female,61"""
    return pd.read_csv(StringIO(csv_data))

class TestUnit:
    def test_handle_wrong_input(self, caplog):
        response = dim_motivation_level("hello")

        assert response is None
        assert "Wrong df input" in caplog.text

    def test_return_new_df(self, create_df):
        response = dim_motivation_level(create_df)

        assert response is not create_df


    def test_missing_ml_column(self, create_df,caplog):
        df = pd.DataFrame({"SomeColumn": [1, 2, 3]})
        response = dim_motivation_level(df)

        assert response is None
        assert "error while transforming unique motivattion level" in caplog.text

        df = pd.DataFrame({})
        response = dim_motivation_level(df)

        assert response is None
        assert "error while transforming unique motivattion level" in caplog.text

    def test_return_unique_values(self, create_df):
        response = dim_motivation_level(create_df)

        assert response.shape[0] == 3

    def test_return_correct_values(self,create_df ):
        response = dim_motivation_level(create_df)

        assert set(response["Motivation_Level"]) == {"High", "Low","Medium"}

    def test_output_column_name(self, create_df):
        result = dim_motivation_level(create_df)

        assert list(result.columns) == ["Motivation_Level"]


        