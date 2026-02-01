import pandas as pd
import logging
from utils.setup_logging import setup_logging


logger = logging.getLogger(__name__)

setup_logging()


def dim_extra_activities(file_df: pd.DataFrame) -> pd.DataFrame:
    """
    transform the extra activities column from in the dataset to
    match its expected destination
    Args:
        file_df: contaning the content of the dataset
    
    Returns:
        a datafram contaning the content and stucture of
        dim_extra_activities table
    """
    #checking that the input recieved us as expected
    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None
    
    #copying the data frame to save the original
    copy_df = file_df.copy()

    #creating the df that matches the dimension table
    ea_df = pd.DataFrame()

    try:
        #taking only unique values
        ea_df["extracurricular_activities"] = copy_df["Extracurricular_Activities"].unique()
    except Exception as e:
        logging.error("error while transforming unique extracurricular activities")
        return None


    return ea_df

