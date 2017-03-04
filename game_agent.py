"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_winner(player):
        return float("inf")
    
    if game.is_loser(player):
        return float("-inf")

    return number_of_legal_moves(game, player)

def number_of_legal_moves(game, player):
    return float(len(game.get_legal_moves(player)))

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

    def get_move(self, game, legal_moves, time_left):

        if len(legal_moves) == 0:
            return (-1, -1)
        
        self.time_left = time_left
 
        # by default, we will pick the middle move?
        move = legal_moves[len(legal_moves)//2]

        # check if we are at the start of the game
        totalAvailable = game.height * game.width
        if totalAvailable == len(legal_moves):
            return move
    
        try:
            
            depth = self.search_depth

            if self.iterative:
                lowerBound = 0
                upperBound = 2000 # what should this bound be?
            else:
                lowerBound = self.search_depth
                upperBound = self.search_depth + 1

            for i in range(lowerBound, upperBound):
                
                if self.method == 'minimax':
                    score, move = self.minimax(game, i)
                elif self.method == 'alphabeta':
                    score, move = self.alphabeta(game, i)

            return move

        except Timeout:
            return move

    def minimax(self, game, depth, maximizing_player=True):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        if (depth == 0):
            return self.score(game, self), (-1,-1)
            
        if maximizing_player:
            v = float("-inf")
            move = (-1, -1)

            for m in game.get_legal_moves():
                t, _ = self.minimax(game.forecast_move(m),depth-1,False)
                if t > v:
                    v = t
                    move = m
            return v, move
        else:
            v = float("inf")
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
            v = float("-inf")
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
            v = float("inf")
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