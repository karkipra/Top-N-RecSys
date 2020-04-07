

"""your custom path here"""
# path to review file
path = 'C:/Users/Administrator/Desktop/Cell_Phones_and_Accessories.json.gz'
# path to metadata file
meta_path = 'C:/Users/Administrator/Desktop/Cell_Phones_and_Accessories.json.gz'
# path to save the analyzed data
des_path = 'data/sentiment_file.json'


def partition_reviewer_words(p=des_path, n=3):
    """
    Partition reviews of the reviewerID by their rating scores.

    This function will create a new file where each line has the key as the reviewerID, and value as a dictionary of rating-text pairs.
    Here, the text will not contain neither summary nor the entire review.
    It will rather contain meaningful words, selected by n-gram selectors in the nltk package. 

    e.g.
    {
        reviewerID: {
            1: [meaningful words, meaningful words, ...],
            2: [meaningful words, meaningful words, ...],
            3: [meaningful words, meaningful words, ...],
            4: [meaningful words, meaningful words, ...],
            5: [meaningful words, meaningful words, ...]
            }
        ...
    }

    Parameters
    ----------
    p: string
        file that contains the json lines to partition the reviews from.
        default value is the des_path that contains the score of sentiments.
    n: integer
        the number of meaningful words to return for each rating.
        the default is set to 3.
    Returns
    -------
    None
    """
    return

def metadata_words(mp = meta_path):
    """
    Find meaningful words in the productID of the metadata file 

    This function will create a new file where each line has dictionary where the key as the productID (asin), and value as a list of meaningful words

    e.g.
    {
        productID: [meaningful words, meaningful words, ...]
        }
    {
        productID: [meaningful words, meaningful words, ...]
        }
        ...
    }

    Parameters
    ----------
    mp: string
        file that contains the metadata json lines to find meaningful words from.
        default value is the meta_path that contains the metadata.
    Returns
    -------
    None
    """
    return

def tf_idf(p=des_path):
    return