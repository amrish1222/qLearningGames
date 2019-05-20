from dotsBoxes import dotsBoxesEnv
from agent import qAgent
from qLearning import qLearn
from game import game
import numpy as np
import matplotlib.pyplot as plt

def train(games2Play,
          _game,
          _qClass,
          i = [100,1000,10000]):
    numGame = 0
    x = []
    y = []
    while numGame < games2Play:
        _qClass = _game.playGameAndLearn(_qClass)
        _game.resetGame()
        numGame+=1
        if numGame in i:
             saveQtable(_game.env.size, numGame, _qClass.qTable)
             print("saved")
        winPerc = (_game.agent1.wins/(_game.agent1.wins + _game.agent2.wins +_game.agent1.draws))
        print("win%:", winPerc)
        y.append(winPerc)
        x.append(numGame)
    plt.plot(x,y,'r-')
    plt.show()
    return _game.agent1.wins, _game.agent2.wins, _game.agent1.draws, _qClass

def saveQtable(size, iterations, qTable):
    fileName = "../qTable/qTable_n"+ str(size)+ "_i" + str(iterations)
    np.save(fileName, qTable)
    
def loadQtable(fileName):
    return np.load('fileName')
 
games2Play = 10000
env = dotsBoxesEnv(2)
agent1 = qAgent()
agent2 = qAgent()
qClass = qLearn(env.numStates, env.numActions)
game1 = game(env, agent1, agent2)

agent1Wins, agent2Wins, draws, qClass = train(games2Play,game1,qClass)
print(agent1Wins, agent2Wins, draws)