import pandas as pd
from utils.setup_logging import setup_logging
import logging

logger = logging.getLogger(__name__)

setup_logging()



def dim_access_to_resources(file_df: pd.DataFrame)-> pd.DataFrame:
    """
    transform the access to resources column in the dataset to
    match its expected destination
    Args:
        file_df: contaning the content of the dataset
    
    Returns:
        a datafram contaning the content and stucture of
        dim_access_to_resources table
    """
    #checking that the input recieved us as expected
    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None
    
    #copying the data frame to save the original
    copy_df = file_df.copy()

    #creating the df that matches the dimension table
    as_df = pd.DataFrame()

    try:
        #taking only unique values
        as_df["access_to_resources"] = copy_df["Access_to_Resources"].unique()
    except Exception as e:
        logging.error("error while transforming unique access to resources")
        return None

    return as_df