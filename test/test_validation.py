from utils.validation import validation
import pandas as pd
import pytest


@pytest.fixture(scope="function")
def create_df():
    return pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
    

class TestIntigration:
    def test_return_new_df(self, create_df):
        response = validation(create_df)

        assert response is not create_df


    def test_handle_wrong_input(self, create_df, caplog):
        response = validation("hello")

        assert response is None
        assert "Wrong df input" in caplog.text


