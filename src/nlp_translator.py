import pandas as pd
from thefuzz import process

def load_database(csv_path):
    # read the medicine csv file into a pandas dataframe
    df = pd.read_csv(csv_path)
    # return the medicine names as a python list so it's easy to search
    return df['medicine_name'].tolist()

def translate_prescription(raw_ocr_text, db_list):
    # if the ocr didn't find anything, just return nothing
    if not raw_ocr_text or len(raw_ocr_text) < 2:
        return "Could not read text", 0
        
    # use fuzzy matching to find the closest drug name in our list.
    # it compares the raw OCR string with every word in our database
    # and returns the best match and a confidence score out of 100
    best_match, score = process.extractOne(raw_ocr_text, db_list)
    
    # if the score is super low, it means it's probably not a drug we know
    if score < 40:
        return "Unknown Drug", score
        
    return best_match, score
