import util
from util import Stack, Queue, PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
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
    Returns a sequence of moves that solves tinyMaze. For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = Stack()
    frontier.push((startState, []))
    explored = set()

    while not frontier.isEmpty():
        currentState, path = frontier.pop()

        if problem.isGoalState(currentState):
            return path

        if currentState not in explored:
            explored.add(currentState)
            for successor, action, stepCost in problem.getSuccessors(currentState):
                if successor not in explored:
                    frontier.push((successor, path + [action]))

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = Queue()
    frontier.push((startState, []))
    explored = set()

    while not frontier.isEmpty():
        currentState, path = frontier.pop()

        if problem.isGoalState(currentState):
            return path

        if currentState not in explored:
            explored.add(currentState)
            for successor, action, stepCost in problem.getSuccessors(currentState):
                if successor not in explored:
                    frontier.push((successor, path + [action]))

    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = PriorityQueue()
    frontier.push((startState, [], 0), 0)
    explored = set()

    while not frontier.isEmpty():
        currentState, path, cost = frontier.pop()

        if problem.isGoalState(currentState):
            return path

        if currentState not in explored:
            explored.add(currentState)
            for successor, action, stepCost in problem.getSuccessors(currentState):
                newCost = cost + stepCost
                if successor not in explored:
                    frontier.push((successor, path + [action], newCost), newCost)

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    startState = problem.getStartState()
    if problem.isGoalState(startState):
        return []

    frontier = PriorityQueue()
    frontier.push((startState, [], 0), heuristic(startState, problem))
    explored = set()

    while not frontier.isEmpty():
        currentState, path, cost = frontier.pop()

        if problem.isGoalState(currentState):
            return path

        if currentState not in explored:
            explored.add(currentState)
            for successor, action, stepCost in problem.getSuccessors(currentState):
                newCost = cost + stepCost
                fCost = newCost + heuristic(successor, problem)
                if successor not in explored:
                    frontier.push((successor, path + [action], newCost), fCost)

    return []


# Example heuristic for A* (Manhattan Distance)
def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic for a PositionSearchProblem.
    """
    xy1 = state
    xy2 = problem.goal
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
