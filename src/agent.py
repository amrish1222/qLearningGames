from qLearning import qLearn
import random

class qAgent:
    def __init__(self):
        self.wins = 0
        self.draws = 0
    
    def getAction(self, 
                  qClass : qLearn,
                  currStateIndex,
                  possibleActions):
        return qClass.eGreedyPolicy(currStateIndex,possibleActions)
    
    def getBestAction(self, 
                  qClass : qLearn,
                  currStateIndex,
                  possibleActions):
        return qClass.greedyPolicy(currStateIndex,possibleActions)
    
class randomAgent:
    def __init__(self):
        self.wins = 0
        self.draws = 0
    
    def getAction(self,
                  possibleActions):
        return random.choice(possibleActions)