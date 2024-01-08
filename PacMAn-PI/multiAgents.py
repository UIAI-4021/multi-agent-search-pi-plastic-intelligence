# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions# PacMan AI agent using minimax with alpha beta prunning
# Implemented by: Mohammad Hassan Heydari, Arian Jafari


# import the necessary libraries
from game import Directions
import random
from util import manhattanDistance, lookup
from game import Agent
from pacman import GameState


def scoreEvaluationFunction(currentGameState: GameState):
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    def __init__(self, evalFn="scoreEvaluationFunction", depth="2", time_limit="6"):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = lookup(evalFn, globals()) # get the evaluation function
        self.depth = int(depth) # get the depth
        self.time_limit = int(time_limit)  # get the time limit

        self.evaluationFunction = lookup(evalFn, globals())
        self.depth = int(depth)
        self.time_limit = int(time_limit)

        # evaluation function for minimax with alpha beta prunning
        # heuristic is based on the distance of the closest food, the distance of the closest ghost and the number of ghosts in 1 distance
        def evaluationFunction(self, game_state, action):
            # get the next game state and the position of pacman
            s_game_state = game_state.generatePacmanSuccessor(action)
            position = s_game_state.getPacmanPosition()

            # get the food ositions
            food = s_game_state.getFood()

            # list of food positions
            foods = food.asList()

            # distance of closest food
            d_foods = -1
            for food in foods:  # for each food calculate the distance
                distance = manhattanDistance(position, food)  # calculate the distance based on manhattan distance
                if d_foods >= distance or d_foods == -1:  # if the distance is smaller than the previous one or if it is the first one
                    d_foods = distance  # update the distance

            # distance of closest ghost
            d_ghosts = 1

            # number of ghosts in 1 distance
            p_ghosts = 0
            for ghost_state in s_game_state.getGhostPositions():  # for each ghost calculate the distance
                distance = manhattanDistance(position, ghost_state)
                d_ghosts += distance
                if distance <= 1:  # if the distance is smaller than 1
                    p_ghosts += 1  # increase the number of ghosts in 1 distance

            # return the score of the game state plus the heuristic
            # heuristic is based on the distance of the closest food, the distance of the closest ghost and the number of ghosts in 1 distance
            # hyperparameters are chosen based on trial and error :)
            score = s_game_state.getScore() + (10000 / float(d_foods)) - (0.01 / float(d_ghosts)) - p_ghosts

            return score


class AIAgent(MultiAgentSearchAgent):

    # get action function for minimax with alpha beta prunning
    def getAction(self, gameState):

        def max_level(agent, depth, game_state, a, b):  # max_level function
            # if the game is won/lost or the defined depth is reached return the utility

            value = -10e12  # set the value to a very small number
            for s in game_state.getLegalActions(agent):  # for each action calculate the value

                prunned = a_b_prunning(1, depth, game_state.generateSuccessor(agent, s), a,
                                       b)  # calculate the value of the next level

                value = max(value, prunned)  # update the value

                if value > b:  # if the value is bigger than beta return the value
                    return value

                a = max(a, value)  # update alpha

            return value

        def min_level(agent, depth, game_state, alpha, beta):  # min_level function

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
            value = 10e12  # set the value to a very big number

            next_agent = agent + 1  # calculate the next agent and increase depth accordingly.
            if game_state.getNumAgents() == next_agent:  # if the next agent is the last one
                next_agent = 0  # set the next agent to pacman
            if next_agent == 0:  # if the next agent is pacman
                depth += 1  # increase the depth

            for s in game_state.getLegalActions(agent):  # for each action calculate the value
                value = min(value, a_b_prunning(next_agent, depth, game_state.generateSuccessor(agent, s), alpha,
                                                beta))  # calculate the value of the next level
                if value < alpha:  # if the value is smaller than alpha return the value
                    return value
                beta = min(beta, value)  # update beta
            return value

        def a_b_prunning(agent, depth, game_state, alpha, beta):  # alpha beta prunning function
            if game_state.isLose() or game_state.isWin() or depth == self.depth:
                # return the utility in case the defined depth is reached or the game is won/lost.
                return self.evaluationFunction(game_state)

            if agent == 0:  # if the agent is pacman
                return max_level(agent, depth, game_state, alpha, beta)  # return the max level

            else:  # if the agent is a ghost
                return min_level(agent, depth, game_state, alpha, beta)  # return the min level

        utility, alpha, beta = -10e12, -10e12, 10e12  # set the utility, alpha and beta to a very small numbers respectievly

        action = Directions.NORTH  # set the action to north

        legal_actions = gameState.getLegalActions(0)  # get the legal actions of pacman
        random.shuffle(legal_actions)  # Shuffle the actions to add randomness

        for s in legal_actions:  # for each action calculate the utility
            ghostValue = a_b_prunning(agent=1, depth=0, game_state=gameState.generateSuccessor(0, s), alpha=alpha,
                                      beta=beta)  # calculate the utility of the next level

            # if the utility is bigger than the previous one update the utility and the action
            if ghostValue > utility:
                utility = ghostValue  # update the utility
                action = s  # update the action
            if utility > beta:  # if the utility is bigger than beta return the utility
                return utility
            alpha = max(alpha, utility)  # update alpha

<<<<<<< Updated upstream
        return action
=======
        return action
>>>>>>> Stashed changes
