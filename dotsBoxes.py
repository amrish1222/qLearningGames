import numpy as np
import itertools

class dotsBoxesEnv:
    def __init__(self,
                  _size = 2):
        self.size = _size
        self.numActions = ((self.size+1) * self.size) * 2
        self.numStates = 2 ** (self.numActions)
        self.allStates = list(range(self.numStates))        
        self.allActions = list(range(self.numActions))
        self.currState = self.allStates[0]
        self.done = False
        self.boxBinary = self.getNearestBoxBin()
        
    def reset(self):
        self.currState = self.allStates[0]
        self.done = False
    
    def conv2bin(self, val):
        return bin(val)[2:].zfill(self.numActions)
    
    def doAction(self, action):
        prevState = self.currState
#        print("env currState Bfr: ", prevState)
#        print("env action: ", action)
        actionBin = 1 << (action)
        self.currState = self.currState | actionBin
#        print("env currState: ", self.currState)
        numCompBoxes = 0
        if self.currState == 2** self.numActions-1:
            self.done = True
        # number of boxes completed
        if not prevState & actionBin == actionBin:
            numCompBoxes = self.completedBoxes(action)
            
# =============================================================================
#             # to print the array
#             self.printgame()
# =============================================================================
        
        else:
            print("Error Action already completed")
        return numCompBoxes
        
    def possibleActions(self):
        possStates = list(self.conv2bin(self.currState))
        out = [len(possStates) - idx-1 for idx, val in enumerate(possStates) if val == '0']
        out.reverse()
        return np.array(out)
    
    def getNearestBoxBin(self):
        zer = [0 for x in range(1,self.numActions+2)]
        nonZeroActions = [x+1 for x in self.allActions]
        k = list(itertools.chain(*zip(zer, nonZeroActions)))
        k.append(0)
        order = np.array(k).reshape(self.size*2+1,self.size*2+1)
#        print(order)
        nz = order.nonzero()
        
        dMax = self.size*2+1
        
        boxesWithAction = []
        for x,y in zip(nz[0], nz[1]):
            allCombi = []
            if x%2 ==0:
                if x-1 >0 : 
                    # up case
                    temp = 0
                    temp |= 2**(order[x-2,y]-1)
                    temp |= 2**(order[x-1,y-1]-1)
                    temp |= 2**(order[x-1,y+1]-1)
                    temp |= 2**(order[x,y]-1)
                    allCombi.append(temp)
                
                if x+1 < dMax : 
                    # down case
                    temp = 0
                    temp |= 2**(order[x+2,y]-1)
                    temp |= 2**(order[x+1,y-1]-1)
                    temp |= 2**(order[x+1,y+1]-1)
                    temp |= 2**(order[x,y]-1)
                    allCombi.append(temp)
            else: # x%2==1
                if y-1 >0 : 
                    # left case
                    temp = 0
                    temp |= 2**(order[x,y-2]-1)
                    temp |= 2**(order[x-1,y-1]-1)
                    temp |= 2**(order[x+1,y-1]-1)
                    temp |= 2**(order[x,y]-1)
                    allCombi.append(temp)
                
                if y+1 < dMax : 
                    # right case
                    temp = 0
                    temp |= 2**(order[x,y+2]-1)
                    temp |= 2**(order[x-1,y+1]-1)
                    temp |= 2**(order[x+1,y+1]-1)
                    temp |= 2**(order[x,y]-1)
                    allCombi.append(temp)
            boxesWithAction.append(allCombi)
#        print(boxesWithAction)
        return boxesWithAction
    
    def printgame(self):
        zer = [0 for x in range(1,self.numActions+2)]
        view = list(self.conv2bin(self.currState))
        k = list(itertools.chain(*zip(zer, view)))
        k.append(0)
        order = np.array(k).reshape(self.size*2+1,self.size*2+1)
        print(order)
    
    def completedBoxes(self, action):
        options = self.boxBinary[action]
        numCompleted = 0

        for op in options:
            if op & self.currState == op:
                numCompleted += 1
                
        return  numCompleted


class reward:
    def __init__(self,
                 _boxComplete = 1,
                 _winGame = 5):
        self.boxComplete = _boxComplete
        self.winGame = _winGame
    
    def reward4box(self, numBoxes):
        return self.boxComplete * numBoxes
    
    def reward4win(self):
        return self.winGame

class display:
    def __init__(self):
        pass
    
    def genDisplay(self, state):
        pass
        
        