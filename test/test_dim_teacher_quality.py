from utils.dim_teacher_quality import dim_teacher_quality
import pytest
import pandas as pd
from io import StringIO

@pytest.fixture(scope="function")
def create_df():
    csv_data = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score
23,84,Low,High,No,7,73,Low,Yes,0,Low,Medium,Public,Positive,3,No,High School,Near,Male,67
19,64,Low,Medium,No,8,59,Low,Yes,2,Medium,High,Public,Negative,4,No,College,Moderate,Female,61
19,64,Low,Medium,No,8,59,Low,Yes,2,Medium,Low,Public,Negative,4,No,College,Moderate,Female,61"""
    return pd.read_csv(StringIO(csv_data))


class TestIntigration:
    def test_handle_wrong_input(self, create_df, caplog):
        response = dim_teacher_quality("hello")

        assert response is None
        assert "Wrong df input" in caplog.text


    def test_return_new_df(self, create_df):
        response = dim_teacher_quality(create_df)

        assert response is not create_df

    
    def test_missing_tq_column(self, create_df,caplog):
        df = pd.DataFrame({"SomeColumn": [1, 2, 3]})
        response = dim_teacher_quality(df)

        assert response is None
        assert "gender column was not found" in caplog.text

        df = pd.DataFrame({})
        response = dim_teacher_quality(df)

        assert response is None
        assert "gender column was not found" in caplog.text


    def test_return_unique_values(self, create_df):
        response = dim_teacher_quality(create_df)

        assert response.shape[0] == 3


    def test_return_correct_values(self,create_df ):
        response = dim_teacher_quality(create_df)

        assert set(response["teacher_quality"]) == {"High", "Low","Medium"}


    def test_output_column_name(self, create_df):
        result = dim_teacher_quality(create_df)

        assert list(result.columns) == ["teacher_quality"]