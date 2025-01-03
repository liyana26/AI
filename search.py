
import util
from util import*
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
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
   
    """Search the deepest nodes in the search tree first."""
    currPath = []           # The path that is popped from the frontier in each loop
    currState = problem.getStartState()    # The state(position) that is popped for the frontier in each loop
    print(f"currState: {currState}")
    
    if problem.isGoalState(currState):     # Checking if the start state is also a goal state
        return currPath

    frontier = Stack()  # A stack is used for DFS
    frontier.push((currState, currPath))  # Insert just the start state, in order to pop it first
    explored = set()    # To keep track of visited nodes

    while not frontier.isEmpty():
        currState, currPath = frontier.pop()    # Popping a state and the corresponding path

        # Check if the current state is a goal state
        if problem.isGoalState(currState):
            return currPath

        explored.add(currState)

        # Get all the successors of the current state
        for s in problem.getSuccessors(currState):
            if s[0] not in explored:
                # Push the successor and the path to the frontier stack
                frontier.push((s[0], currPath + [s[1]]))

    return []  # If this point is reached, a solution could not be found.

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    """ Search the shallowest nodes in the search tree first. """
    currPath = []           # The path that is popped from the frontier in each loop
    currState =  problem.getStartState()    # The state(position) that is popped for the frontier in each loop
    print(f"currState: {currState}")
    if problem.isGoalState(currState):     # Checking if the start state is also a goal state
        return currPath

    frontier = Queue()
    frontier.push( (currState, currPath) )     # Insert just the start state, in order to pop it first
    explored = set()
    while not frontier.isEmpty():
        currState, currPath = frontier.pop()    # Popping a state and the corresponding path
        # To pass autograder.py question2:
        if problem.isGoalState(currState):
            return currPath
        explored.add(currState)
        frontierStates = [ t[0] for t in frontier.list ]
        for s in problem.getSuccessors(currState):
            if s[0] not in explored and s[0] not in frontierStates:
                # Lecture code:
                # if problem.isGoalState(s[0]):
                #     return currPath + [s[1]]
                frontier.push( (s[0], currPath + [s[1]]) )      # Adding the successor and its path to the frontier

    return []       # If this point is reached, a solution could not be found.

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
   # util.raiseNotDefined()
    """Search the node with the lowest path cost first."""
    # Initialize the start state and path
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    # Initialize the frontier (priority queue) and explored set
    frontier = util.PriorityQueue()
    frontier.push((startState, []), 0)  # The second value in the tuple is the path, the third is the cost
    explored = set()  # To keep track of explored states

    while not frontier.isEmpty():
        currState, currPath = frontier.pop()  # Pop the node with the lowest cost
        
        # If this state is the goal state, return the path
        if problem.isGoalState(currState):
            return currPath

        # Mark the state as explored
        if currState not in explored:
            explored.add(currState)

            # Get the successors of the current state
            for successor, action, cost in problem.getSuccessors(currState):
                if successor not in explored:
                    newCost = problem.getCostOfActions(currPath + [action])
                    newPath = currPath + [action]
                    frontier.push((successor, newPath), newCost)  # Add the successor to the frontier with the updated cost

    return []  # If this point is reached, a solution could not be found.


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    """Search the node that has the lowest combined cost and heuristic first."""
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    # Initialize the frontier (priority queue) and explored set
    frontier = util.PriorityQueue()
    # The priority queue stores tuples: (f(n), node, path)
    frontier.push((startState, [], 0), heuristic(startState, problem))  # (state, path, g(n))
    explored = set()  # To keep track of explored states

    while not frontier.isEmpty():
        currState, currPath, currCost = frontier.pop()  # Pop the node with the lowest f(n)

        # If this state is the goal state, return the path
        if problem.isGoalState(currState):
            return currPath

        # Mark the state as explored
        if currState not in explored:
            explored.add(currState)

            # Get the successors of the current state
            for successor, action, stepCost in problem.getSuccessors(currState):
                newCost = currCost + stepCost  # g(n) for the successor
                newHeuristic = heuristic(successor, problem)  # h(n) for the successor
                fCost = newCost + newHeuristic  # f(n) = g(n) + h(n)
                
                # Push the successor into the frontier with its updated path cost
                if successor not in explored:
                    newPath = currPath + [action]
                    frontier.push((successor, newPath, newCost), fCost)  # Push with f(n)

    return []  # If this point is reached, a solution could not be found.



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
