import pandas as pd
from utils.validation import validation

def main():
    df = pd.read_csv("../StudentPerformanceFactors.csv")

    df_validated = validation(df)
    pass
