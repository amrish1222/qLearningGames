import numpy as np
import random
import copy

class qLearn:
    def __init__(self,
                 _numOfStates,
                 _numOfActions,
                 _learningFactor = 0.01,
                 _discountFactor = 0.8,
                 _epsilon = 0.6):
        self.qTable = np.zeros((_numOfStates, _numOfActions))
        self.alpha = _learningFactor
        self.gamma = _discountFactor
        self.epsilon = _epsilon
    
    def updateTable(self,
                    stateIndexPrev,
                    actionIndexPrev,
                    stateIndexCurr,
                    reward):
        qPrev = self.qTable[stateIndexPrev,actionIndexPrev]
        qMax  = np.max(self.qTable[stateIndexCurr,:])
        qNew = qPrev + self.alpha * (reward + self.gamma* qMax - qPrev)
        self.qTable[stateIndexPrev,actionIndexPrev] = qNew
        
    def eGreedyPolicy(self, 
                      currStateIndex,
                      possibleActions):
        pA = copy.deepcopy(possibleActions)
        values = self.qTable[currStateIndex,pA]
        indices = np.where(values == values.max())[0]
        allMaxActions = pA[indices]
        maxAction = random.choice(allMaxActions)
        output = 0
        if random.random() >= self.epsilon or values.shape[0] - indices.shape[0] <= 1:
            output = maxAction
        else:
            np.delete(pA,indices)
            output = random.choice(pA)
        return output
    
    def greedyPolicy(self, 
                      currStateIndex,
                      possibleActions):
        pA = copy.deepcopy(possibleActions)
        values = self.qTable[currStateIndex,pA]
        indices = np.where(values == values.max())[0]
        allMaxActions = pA[indices]
        maxAction = random.choice(allMaxActions)
        output = 0
        output = maxAction
        return output
        