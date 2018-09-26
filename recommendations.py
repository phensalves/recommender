#!/usr/bin/python
#encoding: UTF-8

from math import sqrt

class Recommendations(object):

  def load_es_data(user_id):
    es_connection = ConnectEs.new('user_preferences', user_id)

    print es_connection


  # Returns the Pearson correlation coefficient for first_person and second_person
  def sim_pearson(preferences,first_person,second_person):
    # Get the list of mutually rated items
    mutual_items={}
    for item in preferences[first_person]:
      if item in preferences[second_person]: mutual_items[item]=1

    # Find the number of elements
    number_of_elements=len(mutual_items)

    # if they have no ratings in common, return 0
    if number_of_elements==0: return 0

    # Add up all the preferences
    sum1 = sum([preferences[first_person][it] for it in mutual_items])
    sum2 = sum([preferences[second_person][it] for it in mutual_items])

    # Sum up the squares
    sum1Sq = sum([pow(preferences[first_person][it],2) for it in mutual_items])
    sum2Sq = sum([pow(preferences[second_person][it],2) for it in mutual_items])

    # Sum up the products
    pSum = sum([preferences[first_person][it]*preferences[second_person][it] for it in mutual_items])

    # Calculate Pearson score
    num = pSum − sum1 * sum2 / number_of_elements
    den = sqrt((sum1Sq−pow(sum1,2)/n) * (sum2Sq−pow(sum2,2) / number_of_elements))
    
    if den==0: return 0
    r=num/den

    return r

  def topMatches(prefs, person, n=5, similarity=sim_pearson):
      '''
      Returns the best matches for person from the prefs dictionary. 
      Number of results and similarity function are optional params.
      '''

      scores = [(similarity(prefs, person, other), other) for other in prefs
                if other != person]
      scores.sort()
      scores.reverse()
      return scores[0:n]


  # Gets recommendations for a person by using a weighted average
  # of every other user's rankings
  def getRecommendations(preferences,person,similarity=sim_pearson):
    total={}
    similarSums={}
    for other in preferences:
      # don't compare me to myself
      if other==person: continue
      sim=similarity(preferences,person,other)

      # ignore scores of zero or lower
      if sim<=0: continue
      for item in preferences[other]:

        # only score movies I haven't seen yet
        if item not in preferences[person] or preferences[person][item]==0:
          # Similarity * Score
          total.setdefault(item,0)total[item]+=preferences[other][item]*sim
          # Sum of similarities
          similarSums.setdefault(item,0)
          similarSums[item]+=sim

    # Create the normalized list
    rankings=[(total/similarSums[item],item) for item,total in total.items(  )]

    # Return the sorted list
    rankings.sort(  )
    rankings.reverse(  )
    return rankings

  def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    # Loop over items rated by this user
    for (item, rating) in userRatings.items():
        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:
            # Ignore if this user has already rated this item
            if item2 in userRatings:
                continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            # Sum of all the similarities
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity
    # Divide each total score by total weighting to get an average
    rankings = [(score / totalSim[item], item) for (item, score) in
                scores.items()]
    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings