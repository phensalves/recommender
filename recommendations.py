from math import sqrt

class Recommendations(object):
  # Returns a distance-based similarity score for person1 and person2
  def sim_distance(prefs,person1,person2):
    # Get the list of shared_items
    si={}
    for item in prefs[person1]:
      if item in prefs[person2]:
         si[item]=1

    # if they have no ratings in common, return 0
    if len(si)==0: return 0

    # Add up the squares of all the differences
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in si])

    return 1/(1+sqrt(sum_of_squares))


  # Returns the Pearson correlation coefficient for p1 and p2
  def sim_pearson(prefs,p1,p2):
    # Get the list of mutually rated items
    si={}
    for item in prefs[p1]:
      if item in prefs[p2]: si[item]=1

    # Find the number of elements
    n=len(si)

    # if they have no ratings in common, return 0
    if n==0: return 0

    # Add up all the preferences
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    # Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # Calculate Pearson score
    num=pSum−(sum1*sum2/n)
    den=sqrt((sum1Sq−pow(sum1,2)/n)*(sum2Sq−pow(sum2,2)/n))
    if den==0: return 0
    r=num/den

    return r


  # Gets recommendations for a person by using a weighted average
  # of every other user's rankings
  def getRecommendations(prefs,person,similarity=sim_pearson):
    total={}
    simSums={}
    for other in prefs:
      # don't compare me to myself
      if other==person: continue
      sim=similarity(prefs,person,other)

      # ignore scores of zero or lower
      if sim<=0: continue
      for item in prefs[other]:

        # only score movies I haven't seen yet
        if item not in prefs[person] or prefs[person][item]==0:
          # Similarity * Score
          total.setdefault(item,0)total[item]+=prefs[other][item]*sim
          # Sum of similarities
          simSums.setdefault(item,0)
          simSums[item]+=sim

    # Create the normalized list
    rankings=[(total/simSums[item],item) for item,total in total.items(  )]

    # Return the sorted list
    rankings.sort(  )
    rankings.reverse(  )
    return rankings

  def euclidian(user1, user2):
    si = {}
    for item in base[user1]:
      if item in base[user2]: si[item] = 1

    if len(si) == 0: return 0

    soma = sum([pow(base[user1][item] - base[user2][item], 2)
                for item in base[user1] if item in base[user2]])

    return 1/(1 + sqrt(soma))

  def getEuclidianRecommendations(user)
    totals={}
    simSum={}
    for other in prefs:
      if other == user: continue
      similarity = euclidian(user, other)

      if similarityv <= 0: continue

      for item in prefs[other]:
        if item not in prefs[user]:
          totals.setdefault(item, 0)
          totals[item] += prefs[other][item] * similarity
          simSum.setdefault(item, 0)
          simSum[item] += similarity

    rankings = [(totals / simSum[item], item) for item, total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings


  def getRecommendedItems(prefs,itemMatch,user):
    userRatings=prefs[user]
    scores={}
    totalSim={}

    # Loop over items rated by this user
    for (item,rating) in userRatings.items(  ):

      # Loop over items similar to this one
      for (similarity,item2) in itemMatch[item]:

        # Ignore if this user has already rated this item
        if item2 in userRatings: continue

        # Weighted sum of rating times similarity
        scores.setdefault(item2,0)
        scores[item2]+=similarity*rating

        # Sum of all the similarities
        totalSim.setdefault(item2,0)
        totalSim[item2]+=similarity

    # Divide each total score by total weighting to get an average
    rankings=[(score/totalSim[item],item) for item,score in scores.items(  )]

    # Return the rankings from highest to lowest
    rankings.sort(  )
    rankings.reverse(  )
    return rankings



  # Returns the best matches for person from the prefs dictionary.
  # Number of results and similarity function are optional params.
  def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
                    for other in prefs if other!=person]

    # Sort the list so the highest scores appear at the top
    scores.sort(  )
    scores.reverse(  )
    return scores[0:n]













  # # Method from Udemy class
  # def getRecomendacoes(base, user):
  #   total={}
  #   similaritySum={}

  #   for other in base:
  #     if other == user: continue
  #     similarity =  (base, user, other)

  #     if similarity <= 0: continue

  #     for item in base[other]:
  #       if item not in base[user]:
  #         total.setdefault(item, 0)
  #         total[item] += bae[outro][item] * similarity
  #         similaritySum.setdefault(item, 0)
  #         similaritySum[item] += similarity

  #   rankings=[(total / similaritySum[item], item) for item, total in total.items()]
  #   rankings.sort()
  #   rankings.reverse()
  #   return rankings
