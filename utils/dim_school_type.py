import pandas as pd
from utils.setup_logging import setup_logging
import logging

logger = logging.getLogger(__name__)

setup_logging()



def dim_school_type(file_df: pd.DataFrame)-> pd.DataFrame:
    """
    transform the school_type column in the dataset to
    match its expected destination
    Args:
        file_df: contaning the content of the dataset
    
    Returns:
        a datafram contaning the content and stucture of
        dim_school_type table
    """

    #checking that the input recieved us as expected
    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None
    
    #copying the data frame to save the original
    copy_df = file_df.copy()

    #creating the df that matches the dimension table
    st_df = pd.DataFrame()

    try:
        #taking only unique values
        st_df["school_type"] = copy_df["School_Type"].unique()
    except Exception as e:
        logging.error("error while transforming unique school type")
        return None

    return st_df