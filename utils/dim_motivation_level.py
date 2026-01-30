import pandas as pd
from utils.setup_logging import setup_logging
import logging

logger = logging.getLogger(__name__)

setup_logging()


def dim_motivation_level(file_df: pd.DataFrame)-> pd.DataFrame:
    """
    transform the motivation level column in the dataset to
    match its expected destination
    Args:
        file_df: contaning the content of the dataset
    
    Returns:
        a datafram contaning the content and stucture of
        dim_motivation_level table
    """
    #checking that the input recieved us as expected
    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None
    
    #taking a copy to save the original
    copy_df = file_df.copy()
    
    #the ml df that matches the distenation
    ml_df = pd.DataFrame()
    try:
        #retrieving only unique values
        ml_df["Motivation_Level"] = copy_df["Motivation_Level"].unique()
    except Exception as e:
        logging.error("error while transforming unique motivattion level")
        return None
    return ml_df