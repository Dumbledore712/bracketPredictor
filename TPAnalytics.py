#################################################
# Term Project
# Your andrewID: rmahtab
# Your section: O

# This Analytics file computes all of the behind-the-scenes statistics
# and runs all of the Monte carlo simulations used in the Animation file
#################################################

import random
from tkinter import *
from TPRecords import *

#################################################
# NHL Playoff Bracket Predictor
#################################################

# Global dictionary of all 31 NHL teams by conference
TEAMSDICT = {0: ["Central", "Chicago Blackhawks", "Colorado Avalanche", \
"Dallas Stars", "Minnesota Wild", "Nashville Predators", "St. Louis Blues", \
"Winnipeg Jets"], 1: ["Pacific", "Anaheim Ducks", "Arizona Coyotes", \
"Calgary Flames", "Edmonton Oilers", "Los Angeles Kings", "San Jose Sharks", \
"Vancouver Canucks", "Vegas Golden Knights"], 2: ["Atlantic", "Boston Bruins", \
"Buffalo Sabres", "Detroit Red Wings", "Florida Panthers", \
"Montreal Canadiens", "Ottawa Senators", "Tampa Bay Lightning", \
"Toronto Maple Leafs"], 3: ["Metropolitan", "Carolina Hurricanes", \
"Columbus Blue Jackets", "New Jersey Devils", "New York Islanders", \
"New York Rangers", "Philadelphia Flyers", "Pittsburgh Penguins", \
"Washington Capitals"]}

# Dictionary of each team with their respective season stats
# (PDO, GPG (average goals/game), GAA (average goals against/game))
# PDO, GPG, and GAA taken from hockey-refernce.com (CITATION)
TEAMSTATS = {"Anaheim Ducks": [101.2, 2.866, 2.634], "Arizona Coyotes": [99.5, 2.537, 3.122], \
"Boston Bruins": [100.2, 3.293, 2.610], "Buffalo Sabres": [98.0, 2.427, 3.415], \
"Calgary Flames": [98.9, 2.659, 3.024], "Carolina Hurricanes": [98.2,2.780, 3.122], \
"Chicago Blackhawks": [99.1, 2.793, 3.122], "Colorado Avalanche": [101.3, 3.134, 2.890], \
"Columbus Blue Jackets": [100.2, 2.951, 2.805], "Dallas Stars": [100.3, 2.866, 2.744], \
"Detroit Red Wings": [99.5, 2.646, 3.110], "Edmonton Oilers": [99.4, 2.854, 3.207], \
"Florida Panthers": [100.0, 3.024, 3.0], "Los Angeles Kings": [101.0, 2.915, 2.476], \
"Minnesota Wild": [100.7, 3.085, 2.829], "Montreal Canadiens": [98.7, 2.549, 3.220], \
"Nashville Predators": [101.6, 3.256, 2.573], "New Jersey Devils": [99.7, 3.024, 2.976], \
"New York Islanders": [100.4, 3.220, 3.610], "New York Rangers": [99.8, 2.817, 3.268], \
"Ottawa Senators": [98.8, 2.695, 3.549], "Philadelphia Flyers": [100.3, 3.061, 2.963], \
"Pittsburgh Penguins": [98.5, 3.317, 3.049], "San Jose Sharks": [99.3, 3.073, 2.793], \
"St. Louis Blues": [100.0, 2.756, 2.707], "Tampa Bay Lightning": [102.0, 3.610, 2.878], \
"Toronto Maple Leafs": [101.6, 3.378, 2.829], "Vancouver Canucks": [99.4, 2.659, 3.220], \
"Vegas Golden Knights": [100.5, 3.317, 2.780], "Washington Capitals": [101.4, 3.159, 2.915], \
"Winnipeg Jets": [101.0, 3.378, 2.659]}

### KRACH Method of gettings odds using win/loss records
# KRACH rating system used from collegehockeynews.com (CITATION)
def getKrachOdds(t1, t2):
    # Calculate initial odds from win/loss record
    index1 = list(TEAMSTATS.keys()).index(t1)
    index2 = list(TEAMSTATS.keys()).index(t2)
    winLoss = RECORDS[index1][index2]
    oddsT1 = int(winLoss[0]*100/(sum(winLoss)))
    oddsT2 = 100 - oddsT1
    return (oddsT1, oddsT2)

# Takes two team names and returns the expected winner based off KRACH odds
def getWinner(t1, t2):
    odds = getKrachOdds(t1, t2)
    
    # Generate random number from 1-100 to decide winner based on which odds
    # range the number lands in
    randIndex = random.randint(1,100)
    if randIndex <= odds[0]:
        return t1
    else:
        return t2

# Recursively gets overall winner of single instance of bracket
def getOverallWinner(lst):
    # Base case when list has size 2^n
    if len(lst) == 2:
        return getWinner(lst[0], lst[1])
    # Additional base case when list does not have size 2^n
    elif len(lst) == 1:
        return lst[0]
    # Recursive case
    return getWinner(getOverallWinner(lst[:len(lst)//2]), \
    getOverallWinner(lst[len(lst)//2:]))

# Simulates bracket and makes dictionary of winning teams and # of times they win
def simulateOverallWinner(lst, trials):
    d = {}
    
    # Simulation
    for trial in range(trials):
        winner = getOverallWinner(lst)
        if winner in d:
            d[winner] += 1
        else:
            d[winner] = 1
    
    # Add teams to dictionary that never win in the simulation
    for team in lst:
        if team not in d:
            d[team] = 0
    
    # Determine team that wins most # of times, this will be
    # the predicted winner of the bracket
    max = 0
    for team in d:
        if d[team] > max:
            max = d[team]
            champ = team
    
    return (champ, d)

### Monte Carlo Simulation to get odds using season stats
# Calculate standard deviations of GPG and GAA stats using formula
def calculateGPGStandardDev():
    # Calculate mean (mu)
    mu = 0
    for team in TEAMSTATS:
        mu += TEAMSTATS[team][1]
    mu /= len(TEAMSTATS)
    # Calculate sum separately since mu is needed first
    sum = 0
    for team in TEAMSTATS:
        sum += (TEAMSTATS[team][1] - mu)**2
    # Calculate standard deviation (sigma)
    sigma = (sum/len(TEAMSTATS))**0.5
    return sigma

def calculateGAAStandardDev():
    # Calculate mean (mu)
    mu = 0
    for team in TEAMSTATS:
        mu += TEAMSTATS[team][2]
    mu /= len(TEAMSTATS)
    # Calculate sum separately since mu is needed first
    sum = 0
    for team in TEAMSTATS:
        sum += (TEAMSTATS[team][2] - mu)**2
    # Calculate standard deviation (sigma)
    sigma = (sum/len(TEAMSTATS))**0.5
    return sigma

# Use Monte Carlo simulation to determine odds
# GPG and GAA will determine the outcomes of the simulated games
def simulatedOdds(t1, t2, trials):
    t1wins = 0
    t2wins = 0
    gpgSigma = calculateGPGStandardDev()
    gaaSigma = calculateGAAStandardDev()
    
    # Simulation
    for trial in range(trials):
        # Generate random GPG and GAA within 2 standard deviations of team avg
        gpg1 = random.uniform(TEAMSTATS[t1][1]-2*gpgSigma, TEAMSTATS[t1][1]+2*gpgSigma)
        gpg2 = random.uniform(TEAMSTATS[t2][1]-2*gpgSigma, TEAMSTATS[t2][1]+2*gpgSigma)
        gaa1 = random.uniform(TEAMSTATS[t1][2]-2*gaaSigma, TEAMSTATS[t1][2]+2*gaaSigma)
        gaa2 = random.uniform(TEAMSTATS[t2][2]-2*gaaSigma, TEAMSTATS[t2][2]+2*gaaSigma)
        
        # Estimate number of goals for each team in the trial game 
        # by taking average of one team's GPG and the other team's GAA
        t1goals = (gpg1 + gaa2) / 2
        t2goals = (gpg2 + gaa1) / 2
        
        # Determine winner of game by comparing estimated goals scored
        if t1goals > t2goals:
            t1wins += 1
        else:
            t2wins += 1
    
    return (t1wins*100/trials, t2wins*100/trials)

# Predict score based on GPG, GAA, and PDO stats
def predictScore(t1, t2):
    # Get simulated odds over 10000 trial games
    sims = 10000
    oddsTuple = simulatedOdds(t1, t2, sims)
    
    gpg1 = TEAMSTATS[t1][1]
    gpg2 = TEAMSTATS[t2][1]
    gaa1 = TEAMSTATS[t1][2]
    gaa2 = TEAMSTATS[t2][2]
    
    # Calculated expected total goals scored in the game
    total = (gpg1+gaa2)/2 + (gpg2+gaa1)/2

    # Use odds to determine the % of the total goals scored by each team
    t1goals = round(total*oddsTuple[0]/100)
    t2goals = round(total*oddsTuple[1]/100)
    
    # If predicted score is a tie, give 1 extra goal to team with higher PDO
    if t1goals == t2goals:
        if TEAMSTATS[t1][0] > TEAMSTATS[t2][0]:
            t1goals += 1
        else:
            t2goals += 1
    
    return str(t1goals) + " - " + str(t2goals)

# Get playoff advancement percentages by simulating each round
def getPercentages(lst):
    # Dictionary with teams as keys and list of %'s as values
    percentageDict = {}
    sims = 1000
    
    # Populate percentageDict with empty lists
    for t in lst:
        percentageDict[t] = []
    
    # Each team should end up with four percentages total
    # QF%
    for t in range(0, len(lst), 2):
        qfDict = simulateOverallWinner(lst[t:t+2], sims)[1]
        for j in range(2):
            percentageDict[lst[t+j]].append(qfDict[lst[t+j]]/10)
    # SF%
    for t in range(0, len(lst), 4):
        sfDict = simulateOverallWinner(lst[t:t+4], sims)[1]
        for j in range(4):
            percentageDict[lst[t+j]].append(sfDict[lst[t+j]]/10)
    # F%
    for t in range(0, len(lst), 8):
        fDict = simulateOverallWinner(lst[t:t+8], sims)[1]
        for j in range(8):
            percentageDict[lst[t+j]].append(fDict[lst[t+j]]/10)
    # C%
    cDict = simulateOverallWinner(lst, sims)[1]
    for j in lst:
        percentageDict[j].append(cDict[j]/10)
    
    return percentageDict