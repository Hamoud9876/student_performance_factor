import pandas as pd
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="""%(asctime)s [%(levelname)s] %(name)s 
    (%(filename)s:%(funcName)s:%(lineno)d): %(message)s""",
    force=True,
)
logger = logging.getLogger(__name__)

def validation(file_df: pd.DataFrame)-> pd.DataFrame:
    """
    Validating the dataframe series to make sure they
    match their expected input

    Args:
        file_df: dataframe containing the 
        content of it source file
    
    Return:
        A new df with the validated fields and any
        new datatype changes
    """

    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None

    Copy_df = file_df.copy()

    return Copy_df
