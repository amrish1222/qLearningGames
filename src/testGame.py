from dotsBoxes import dotsBoxesEnv
from agent import qAgent
from qLearning import qLearn
from game import game

env = dotsBoxesEnv(3)
agent1 = qAgent()
agent2 = qAgent()
qClass = qLearn(env.numStates, env.numActions)
game1 = game(env, agent1, agent2)
#%%
qClass = game1.playGameAndLearn(qClass)
game1.resetGame()
