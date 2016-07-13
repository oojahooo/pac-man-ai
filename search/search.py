# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import game
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    successorstack = util.Stack()
    successors = (problem.getStartState(), [])
    alreadylist = []
    successorstack.push( successors )
    while True:
        if successorstack.isEmpty() == True:
            print 'We can\'t goal'
            return
        successors = successorstack.pop()
        if problem.isGoalState( successors[0] ):
            return successors[1]
        if not successors[0] in alreadylist:
            alreadylist.append( successors[0] )
            for i in problem.getSuccessors( successors[0] ):
                successorstack.push( (i[0], successors[1] + [i[1]]) )
    util.raiseNotDefined()
            
def breadthFirstSearch(problem):
    successorsqueue = util.Queue()
    successors = (problem.getStartState(), [])
    alreadylist = []
    successorsqueue.push( successors )
    while True:
        if successorsqueue.isEmpty() == True:
            print 'We can\'t goal'
            return
        successors = successorsqueue.pop()
        if problem.isGoalState( successors[0] ):
            return successors[1]
        if not successors[0] in alreadylist:
            alreadylist.append( successors[0] )
            for i in problem.getSuccessors( successors[0] ):
                successorsqueue.push( (i[0], successors[1] + [i[1]]) )

def uniformCostSearch(problem):
    successorspriorityq = util.PriorityQueue()
    successors = (problem.getStartState(), [], 0)
    alreadylist = []
    successorspriorityq.push( successors, 0 )
    while True:
        if successorspriorityq.isEmpty() == True:
            print 'We can\'t goal'
            return
        successors = successorspriorityq.pop()
        if problem.isGoalState( successors[0] ):
            return successors[1]
        if not successors[0] in alreadylist:
            alreadylist.append( successors[0] )
            for i in problem.getSuccessors( successors[0] ):
                successorspriorityq.push( (i[0], successors[1] + [i[1]], successors[2] + i[2]), successors[2] + i[2] )

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    successorspriorityq = util.PriorityQueue()
    successors = (problem.getStartState(), [])
    alreadylist = []
    successorspriorityq.push( successors, 0 )
    while True:
        if successorspriorityq.isEmpty() == True:
            print 'We can\'t goal'
        successors = successorspriorityq.pop()
        if problem.isGoalState( successors[0] ):
            return successors[1]
        if not successors[0] in alreadylist:
            alreadylist.append( successors[0] )
            for i in problem.getSuccessors( successors[0] ):
                successorspriorityq.push( (i[0], successors[1] + [i[1]]), i[2] + heuristic(i[0], problem) )

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
