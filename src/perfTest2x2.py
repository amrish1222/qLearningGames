from dotsBoxes import dotsBoxesEnv
from agent import qAgent
from agent import randomAgent
from qLearning import qLearn
from game import game
import numpy as np
import matplotlib.pyplot as plt


def perf_Test(games2Play,
          _game:game,
          _qClass):
    numGame = 0
    x = []
    y = []
    while numGame < games2Play:
        _qClass = _game.playGameQvR(_qClass)
        _game.resetGame()
        numGame+=1
        winPerc = (_game.agent1.wins/(_game.agent1.wins + _game.agent2.wins +_game.agent1.draws))
        print("win%:", winPerc)
        y.append(winPerc)
        x.append(numGame)
    plt.plot(x,y,'r-')
    plt.show()
    return _game.agent1.wins, _game.agent2.wins, _game.agent1.draws, _qClass

def saveQtable(size, iterations, qTable):
    fileName = "qTable/qTable_n"+ str(size)+ "_i" + str(iterations)
    np.save(fileName, qTable)
    
def loadQtable(fileName):
    return np.load(fileName)
 
games2Play = 100    
env = dotsBoxesEnv(2)
agent1 = qAgent()
agent2 = randomAgent()
qClass = qLearn(env.numStates, env.numActions)
game1 = game(env, agent1, agent2)

qClass.qTable = loadQtable('../qTable/qTable_n3_i10000.npy')
agent1Wins, agent2Wins, draws, qClass = perf_Test(games2Play,game1,qClass)
print(agent1Wins, agent2Wins, draws)