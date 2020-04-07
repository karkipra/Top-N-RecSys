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


### what should we do when the sentiment values are 0???

def senti_in_json(line):
    """
    Apply sentiment analysis in each json dictionary

    Parameters
    ----------
    line: dict
        json dictionary to apply the sentiment analysis

    Returns
    -------
    dict
        a changed dictionary with sentiment scores
    """
    change = line    
    try:
        change['sentiment_review'] = analyser.polarity_scores(change['reviewText'])['compound']
    except:
        change['sentiment_review'] = 0.0
    try:
        change['sentiment_summary'] = analyser.polarity_scores(change['summary'])['compound']
    except:
        change['sentiment_summary'] = 0.0
    return change



def parse(p = path):
    """
    Open a gzipped file and call senti_in_json until a certain line

    This function adds the changed data into the global variable, new_data


    Parameters
    ----------
    p: string
        path to read the gzipped file from
        default value is the global variable path

    Returns
    -------
    None
    """    
    g = gzip.open(p, 'r')
    for num, l in enumerate(g):
        if num == line_number_limit:
            break
        change = senti_in_json(json.loads(l))

        new_data.append(change)



def json_print(json_data, limit):
    """
    Print the json dictionary until the certain limit

    Parameters
    ----------
    json_data: list of dictionary
        the list containing the json data
    limit: int
        the number of how many json data we want to print
    
    Returns
    -------
    None
    """
    print("JSONDATA", type(json_data))

    for each in json_data[:limit]:
        print(each)



def json_write(dest_path = des_path):
    """
    write the data back to the destination path
    
    Parameters
    ----------
    dest_path: string
        the destination path to write our data into
        default value is the global variable des_path
        
    Returns
    -------
    None
    """
    with open(des_path, 'w') as f:
        # cursor to zero to overwrite the file
        f.seek(0)
        for line in new_data:   
            json.dump(line, f)
            f.write('\n')



def metadata_itemID(itemID, m_path = meta_path):
    """
    takes an itemID from the metadata and return the json associated with the item
    
    Parameters
    ----------
    itemID
        a unique item identifier to search within the metadata
    m_path
        the destination to the meta data file
        default value is the global variable meta_path
        
    Returns
    -------
    save_itemID: list
        a list containing the matching json data
    """
    g = gzip.open(m_path, 'r')
    save_itemID = []
    for num, l in enumerate(g):
        if num == line_number_limit:
            break
        if l["asin"] == itemID:
            save_itemID.append(l)
    return save_itemID    



def model(alpha=0.3, beta=0.6, gamma=0.1, m_path = des_path):
    """
    combine percentages of rating score and sentiment score to return a new score

    The new score will be alpha*rating + beta*sentiment score
    
    Parameters
    ----------
    alpha
        the percentage of rating to be used for the new score
        default value is 0.3
    beta
        the percentage of sentiment score to be used for the new score
        default value is 0.6
    gamma
        the percentage of sentiment summary score to be used for the new score
        default value is 0.1   
    m_path
        the path to apply the score from
        default value is the global variable des_path
        
    Returns
    -------
    scores_list: list
        a list with the new scores attached to them
    """    
    scores_list = []

    with open(m_path, 'r') as f:
        for each in f:
            loaded_json = json.loads(each)
            score = alpha*loaded_json["overall"] + beta*loaded_json["sentiment_review"] + gamma*loaded_json["sentiment_summary"]
            loaded_json["new_score"] = score
            scores_list.append(loaded_json)
    for each in scores_list:
        print(each)
        print("\n")
    return scores_list



# # what this does is read the json file from "path", apply the sentiment analysis, and store it to the "des_path"
# parse(path)
# json_write(des_path)

# ### json_print(new_data, line_number_limit)

# # this reads from the des_path and apply the new score and prints it out
# model()


