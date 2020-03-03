# Literature Review and Ideas

## Date: January 30, 2020
## Venue: RecSys 2018 
## Article: Item Recommendation on Monotonic Behavior Chains

### Summary::

The authors suggest a new recommender system “ChainRec” that aims to model the full 
spectrum of users’ feedback (implicit and explicit) to recommend books. They test their 
method on five different datasets and use interesting evaluation mechanisms.

### Observation::

User’s interaction often exhibit monotonic structure/pattern.

### Major idea that we might be interested in:

   Items have different features: 
      price, brand, special-attention, manufacturing country/region, time, 
      ratings, popularity, interest-group, ease of use, availability, free delivery, 
       free gift items, etc.

<b>For different users, different features are critical.</b> 

### Goal: 

  How to model each user-item interactions along with the basic ratings matrix is one 
  of the preliminary step that we want to complete.

## Date: Feb 04, 2020

We plan to build user-item rating matrix and run a basic CF on that.
We also want to find the features of products and define a similarity function that can be used later to refine the recommendation list.
We also need to look at the product metadata.
### Tentative Project Goal: 
-- Recommend useful, relevant, and DIVERSE items to users.

## Date: Feb 20, 2020

Have run the ALS model and done a basic evaluation. However, this only predicts the potential ratings. We want to incorporate metadata and reviewText. 

### Notes: 
- Sort by prediction for the particular item
- Look at [Julian Mcauley's website](https://cseweb.ucsd.edu/~jmcauley/) to see how the dataset has been used in the past.
- Partition reviews into positive and negative reviews (5,4,3 +ve and 2,1 -ve)
   - Then find top `k` meaningful words in the review and find the relation to the product review. 
      - Positive and negative list of these words
   - Then find the same words in the metadata description of other products and give more weight to those products. 
      - Create a Dictionary of words that have been used (tf-idf concept)
      - x column: top `k` words in the reviewText
      - y column: meaningful words in the metadata
      - multiply x+y with predicted Ratings
      
### Tentative Goals:

- [ ] Dictionary to grouping of words.
- [ ] Write a method that takes reviewerID and returns top-k positive and negative reviews.
- [ ] Read recent papers and understand what JMcauly has done with the dataset. 
- [ ] **If there is time** method given itemID, returns metadata of the item. 

## Date: Mar 3, 2020

Have the sentiments of review and summary done. 

### Notes: 

- Now that we have sentiment score, we can model as below
   - \alpha x rating + \beta x sentiment
   - If this model improves MAP then keep it
- By analysing the reviews, we aim to find the most impactful words or features of products that help buyers make their decision (e.g. strong keywords). This should help people trying to sell items - either bigram or trigram model. 
- **Study on** Factorization Machine Model.
