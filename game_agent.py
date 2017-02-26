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

    # TODO: finish this function!
    raise NotImplementedError


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
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        if len(legal_moves) == 0:
            return (-1, -1)
        
        self.time_left = time_left
 
        # by default, we will pick the middle move? maybe do random here?
        defaultMove = legal_moves[len(legal_moves)//2]

        # check if we are at the start of the game
        totalAvailable = game.height * game.width
        if totalAvailable == len(legal_moves):
            return defaultMove
    
        try:
            score, move = self.minimax(game, self.search_depth)
            
            return move

            # if self.method == 'minimax':
            #     return self.minimax(game, 0, game.active_player == self)
            # else:
            #     return self.alphabeta(game, 0, float("-inf"), float("inf"), game.active_player == self)

        except Timeout:
            return defaultMove

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        
        # find the move that results in highest score
        selectedScore = float("-inf")
        bestMove = (-1, -1)

        # print("\nminimax with depth", depth,"active player:",game.active_player)
        # print(game.to_string())
        # input("press enter to continue")

        for m in game.get_legal_moves():
            score = self.__minimize__(game.forecast_move(m), depth)
            # print("evaluating move",m,"at depth",depth,"returned score",score)
            if score > selectedScore:
                selectedScore = score
                bestMove = m
        
        return selectedScore, bestMove

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

    def __minimize__(self, game, depth):
        if (depth == 1):
            return self.score(game, game.inactive_player)

        v = float("inf")

        for m in game.get_legal_moves():
            v = min(v, self.__maximize__(game.forecast_move(m),depth-1))
        
        return v

    def __maximize__(self, game, depth):
        if (depth == 1):
            return self.score(game, game.active_player)

        v = float("-inf")

        for m in game.get_legal_moves():
            v = max(v, self.__minimize__(game.forecast_move(m),depth-1))
        
        return v

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        # find the move that results in highest score
        
        # print("\nalpha beta with depth", depth,"active player:",game.active_player)
        # print(game.to_string())
        # input("press enter to continue")

        selectedScore = float("-inf")
        bestMove = (-1, -1)

        for m in game.get_legal_moves():
            score = self.__maximize_alphabeta__(game.forecast_move(m), depth, alpha, beta)
            # print("evaluating move",m,"at depth",depth,"returned score",score)
            if score > selectedScore:
                selectedScore = score
                bestMove = m
        
        return selectedScore, bestMove

        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

    def __maximize_alphabeta__(self, game, depth, alpha, beta):
        if (depth == 1):
            return self.score(game, game.active_player)

        v = float("-inf")

        for m in game.get_legal_moves():
            v = max(v, self.__minimize_alphabeta__(game.forecast_move(m),depth-1,alpha,beta))
            if v >= beta: 
                return v
            alpha = max(alpha, v)
        return v
    
    def __minimize_alphabeta__(self, game, depth, alpha, beta):
        if (depth == 1):
            return self.score(game, game.inactive_player)

        v = float("inf")

        for m in game.get_legal_moves():
            v = min(v, self.__maximize_alphabeta__(game.forecast_move(m),depth-1,alpha,beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v