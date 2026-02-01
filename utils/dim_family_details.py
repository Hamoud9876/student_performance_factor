import pandas as pd
import logging
from utils.setup_logging import setup_logging


logger = logging.getLogger(__name__)

setup_logging()


def dim_family_details(file_df: pd.DataFrame) -> pd.DataFrame:
    """
    transform the family_details column from in the dataset to
    match its expected destination
    Args:
        file_df: contaning the content of the dataset
    
    Returns:
        a datafram contaning the content and stucture of
        dim_family_details table
    """
    #checking that the input recieved us as expected
    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None
    
    #copying the data frame to save the original
    copy_df = file_df.copy()

    #creating the df that matches the dimension table
    fd_df = pd.DataFrame()

    try:
        #taking only unique values
        fd_df["parental_education_level"] = copy_df["Parental_Education_Level"].unique()
    except Exception as e:
        logging.error("error while retrieving parental education")
        return None
    
    try:
        #taking only unique values
        fd_df["family_income"] = copy_df["Family_Income"].unique()
    except Exception as e:
        logging.error("error while retrieving family income")
        return None


    return fd_df