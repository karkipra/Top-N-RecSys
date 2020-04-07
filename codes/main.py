import codes as cod
import sentiment as sent
import json
import gzip
import time
import os
from shutil import copyfile
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

"""your custom path here"""
# path to review file
path = 'C:/Users/Administrator/Desktop/Cell_Phones_and_Accessories.json.gz'
# path to metadata file
meta_path = 'C:/Users/Administrator/Desktop/Cell_Phones_and_Accessories.json.gz'
# path to save the analyzed data
des_path = 'data/sentiment_file.json'

# global variables
line_number_limit = 40
analyser = SentimentIntensityAnalyzer()
new_data = []




# what this does is read the json file from "path", apply the sentiment analysis, and store it to the "des_path"
cod.parse(path)
cod.json_write(des_path)

### json_print(new_data, line_number_limit)

# this reads from the des_path and apply the new score and prints it out
cod.model()

