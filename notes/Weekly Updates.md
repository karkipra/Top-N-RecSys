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

![#1589F0]## Date: Feb 04, 2020

We plan to build user-item rating matrix and run a basic CF on that.
We also want to find the features of products and define a similarity function that can be used later to refine the recommendation list.
We also need to look at the product metadata.
### Tentative Project Goal: 
-- Recommend useful, relevant, and DIVERSE items to users.
