import pandas as pd
import logging
from pydantic import BaseModel, Field, ValidationError
from typing import Literal

class StudentRecord(BaseModel):
    Hours_Studied: int = Field(0, ge=0, le=24)
    Attendance: int = Field(0, ge=0, le=100)
    Parental_Involvement: Literal["Low", "Medium", "High"] = "Medium"
    Access_to_Resources: Literal["Low", "Medium", "High"] = "Medium"
    Extracurricular_Activities: Literal["Yes", "No"] = "No"
    Sleep_Hours: int = Field(8, ge=0, le=24)
    Previous_Scores: int = Field(0, ge=0, le=100)
    Motivation_Level: Literal["Low", "Medium", "High"] = "Medium"
    Internet_Access: Literal["Yes", "No"] = "Yes"
    Tutoring_Sessions: int = Field(0, ge=0)
    Family_Income: Literal["Low", "Medium", "High"] = "Medium"
    Teacher_Quality: Literal["Low", "Medium", "High"] = "Medium"
    School_Type: Literal["Public", "Private"] = "Public"
    Peer_Influence: Literal["Positive", "Negative"] = "Positive"
    Physical_Activity: int = Field(0, ge=0)
    Learning_Disabilities: Literal["Yes", "No"] = "No"
    Parental_Education_Level: str = "Unknown"
    Distance_from_Home: Literal["Near", "Moderate", "Far"] = "Moderate"
    Gender: Literal["Male", "Female"] = "Male"
    Exam_Score: int = Field(0, ge=0, le=100)


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
    
    Returns:
        A new df with the validated fields and any
        new datatype changes
    """

    #checking that the input recieved us as expected
    if not isinstance(file_df, pd.DataFrame):
        logging.error("Wrong df input")
        return None
    
    #2 lists to hold valid and not valid records
    nt_valid =[]
    valid = []

    #taking a copy of the original df to preserve it 
    Copy_df = file_df.copy()


    #looping through each row of the df
    for i, row in enumerate(Copy_df.to_dict(orient="records")):
        try:
            #validating the rows
            record = StudentRecord(**row)
            valid.append(record)
        except ValidationError as e:
            nt_valid.append((i, e.errors()))
            
    #logging the number of records
    logger.info(f"Valid rows: {len(valid)}")
    logger.error(f"Invalid rows: {len(nt_valid)}")


    #returnging the valid records into df
    validated_df = pd.DataFrame([r.model_dump() for r in valid])


    return validated_df
