import pandas as pd
import logging
from utils.setup_logging import setup_logging


logger = logging.getLogger(__name__)

setup_logging()


def dim_gender(file_df: pd.DataFrame) -> pd.DataFrame:
    """
    transform the gender column from in the dataset to
    match its expected destination
    Args:
        file_df: contaning the content of the dataset
    
    Returns:
        a datafram contaning the content and stucture of
        the dimension table
    """
    #checking that the input recieved us as expected
    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None
    
    #copying the data frame to save the original
    copy_df = file_df.copy()

    #creating the df that matches the dimension table
    gender_df = pd.DataFrame()

    try:
        #taking only unique values
        gender_df["gender"] = copy_df["Gender"].unique()
    except Exception as e:
        logging.error("gender column was not found")
        return None


    return gender_df

