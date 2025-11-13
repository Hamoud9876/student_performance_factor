from utils.validation import validation
import pandas as pd
from io import StringIO
import pytest


@pytest.fixture(scope="function")
def create_df():
    csv_data = """Hours_Studied,Attendance,Parental_Involvement,Access_to_Resources,Extracurricular_Activities,Sleep_Hours,Previous_Scores,Motivation_Level,Internet_Access,Tutoring_Sessions,Family_Income,Teacher_Quality,School_Type,Peer_Influence,Physical_Activity,Learning_Disabilities,Parental_Education_Level,Distance_from_Home,Gender,Exam_Score
23,84,Low,High,No,7,73,Low,Yes,0,Low,Medium,Public,Positive,3,No,High School,Near,Male,67
19,64,Low,Medium,No,8,59,Low,Yes,2,Medium,Medium,Public,Negative,4,No,College,Moderate,Female,61"""
    return pd.read_csv(StringIO(csv_data))
    

class TestIntigration:
    def test_return_new_df(self, create_df):
        response = validation(create_df)

        assert response is not create_df


    def test_handle_wrong_input(self, create_df, caplog):
        response = validation("hello")

        assert response is None
        assert "Wrong df input" in caplog.text

    
    def test_validate_schema(self, create_df, caplog):
        validation(create_df)

        assert "Valid rows: 2" in caplog.text
        assert "Invalid rows: 0" in caplog.text


