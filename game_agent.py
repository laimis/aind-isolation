"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random
import math

class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


INFINITY = float("inf")
NEG_INFINITY = float("-inf")


def custom_score(game, player):
    if game.is_winner(player):
        return INFINITY
    
    if game.is_loser(player):
        return NEG_INFINITY

    pos = game.get_player_location(player)

    heuristic = open_own_vs_opponent(game,player)

    # for the project I ran measurements for heuristics with each of 
    # of the lines separately and together to come up with
    # 3 different heuristics

    # heuristic = heuristic + distance_to_open_score(game,player,pos)

    heuristic = heuristic + position_score(game,player,pos)

    return heuristic

def open_own_vs_opponent(game,player):
    """ heuristic take from the ID_Improved
    """

    own_moves = len(game.get_legal_moves(player))

    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(own_moves - opp_moves)


def position_score(game,player,pos):
    """ this score is used to calculate the score of how close to the
    wall the player's position is. The further away from the wall, the higher the number
    with max being 1 when a player is in the center
    """

    mp = game.width // 2
    
    maxDistance = game.width - 1
    
    delta = abs(pos[0]-mp) + abs(pos[1]-mp)

    return 1 - delta / maxDistance


def distance_to_open_score(game,player,pos):
    """ this score is used to calculate the score of how close to
    the open squares the player's position is. The closer to the open fields,
    the higher the number. The max distance is calculated once on the first
    get_move called for the game
    """

    opens = game.get_blank_spaces()

    distance = sum([math.sqrt((a[0]-pos[0])**2 + (a[1]-pos[1])**2) for a in opens])

    return 1 - distance / player.max_distance


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout
        self.max_distance = 0

    def set_max_distance(self, width):
        """ calculates max distance for a point to all of the squares in a game board
        """
        for r in range(0, width):
            for c in range(0, width):
                self.max_distance += math.sqrt(r**2+c**2)

    def get_move(self, game, legal_moves, time_left):

        if len(legal_moves) == 0:
            return (-1, -1)
        
        self.time_left = time_left
 
        if self.max_distance == 0:
            self.set_max_distance(game.width)

        # by default, we will pick the middle move?
        move = legal_moves[len(legal_moves)//2]

        # check if we are at the start of the game
        # start in the center if that's the case
        totalAvailable = game.height * game.width
        if totalAvailable == len(legal_moves):
            return move
    
        # set lower and upper bounds to search depth
        # in case iterative search is not being used
        lowerBound = self.search_depth
        upperBound = self.search_depth + 1
        
        # just for diagnostics
        currentDepth = 0

        # in case iterative depth is being used, keep track
        # the best move returned by each iteration in case
        # we will need to return what we have from a timeout
        bestScore = NEG_INFINITY
        bestMove = (-1,-1)

        try:
            
            depth = self.search_depth

            if self.iterative:
                lowerBound = 0
                upperBound = 1000 # seems high enough
            
            for i in range(lowerBound, upperBound):
                currentDepth = i
                if self.method == 'minimax':
                    score, move = self.minimax(game, i)
                elif self.method == 'alphabeta':
                    score, move = self.alphabeta(game, i)

                # print("depth:",currentDepth,"score",score,"compared against best",move)
                
                if score > bestScore and currentDepth != 0:
                    bestMove = move
                    bestScore = score

                if score == INFINITY:
                    break

            # print("returning",bestMove,"with score", bestScore,"depth achieved",currentDepth)
            
            return bestMove

        except Timeout:
            # print("timeout",bestMove,"with score",bestScore,"depth achieved",currentDepth-1)
            return bestMove

    def minimax(self, game, depth, maximizing_player=True):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        if (depth == 0):
            return self.score(game, self), (-1,-1)
            
        if maximizing_player:
            v = NEG_INFINITY
            move = (-1, -1)

            for m in game.get_legal_moves():
                t, _ = self.minimax(game.forecast_move(m),depth-1,False)
                if t > v:
                    v = t
                    move = m
            return v, move
        else:
            v = INFINITY
            move = (-1, -1)

            for m in game.get_legal_moves():
                t, _ = self.minimax(game.forecast_move(m),depth-1,True)
                if t < v:
                    v = t
                    move = m
            return v, move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()
            
        if (depth == 0):
            return self.score(game, self), (-1,-1)
            
        if maximizing_player:
            v = NEG_INFINITY
            move = (-1, -1)

            for m in game.get_legal_moves():
                t, _ = self.alphabeta(game.forecast_move(m),depth-1,alpha,beta,False)
                if t > v:
                    v = t
                    move = m
                if v >= beta:
                    return v,move
                alpha = max(alpha,v)

            return v, move
        else:
            v = INFINITY
            move = (-1, -1)

            for m in game.get_legal_moves():
                t, _ = self.alphabeta(game.forecast_move(m),depth-1,alpha,beta,True)
                if t < v:
                    v = t
                    move = m
                if v <= alpha:
                    return v, move
                beta = min(beta,v)

            return v, move