"""Minimax agent - uses minimax algorithm with alpha-beta pruning."""

from typing import Any, Tuple
from .base import BaseAgent


class MinimaxAgent(BaseAgent):
    """Agent using minimax algorithm with alpha-beta pruning.
    
    This provides optimal play for small games like Tic-Tac-Toe.
    For larger games like Connect Four, depth is limited.
    """
    
    def __init__(self, player_id: int, depth: int = 6):
        """Initialize minimax agent.
        
        Args:
            player_id: Player ID (1 or 2)
            depth: Search depth for minimax
        """
        super().__init__(player_id, name="Minimax")
        self.depth = depth
    
    def get_move(self, game: Any) -> int:
        """Select best move using minimax algorithm.
        
        Args:
            game: Game instance
            
        Returns:
            Best move found
        """
        best_move = None
        best_score = float('-inf')
        
        for move in game.get_valid_moves():
            # Make move
            game.make_move(move)
            
            # Evaluate position
            score = self._minimax(game, self.depth - 1, float('-inf'), float('inf'), False)
            
            # Undo move
            self._undo_move(game, move)
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _minimax(self, game: Any, depth: int, alpha: float, beta: float, is_maximizing: bool) -> float:
        """Minimax with alpha-beta pruning.
        
        Args:
            game: Game instance
            depth: Remaining search depth
            alpha: Alpha value for pruning
            beta: Beta value for pruning
            is_maximizing: Whether maximizing player
            
        Returns:
            Score of position
        """
        winner = game.get_winner()
        
        # Terminal state
        if winner is not None:
            if winner == self.player_id:
                return 10 + depth  # Prefer faster wins
            elif winner == 0:
                return 0  # Draw
            else:
                return -10 - depth  # Prefer slower losses
        
        # Depth limit reached
        if depth == 0:
            return self._evaluate(game)
        
        if is_maximizing:
            max_eval = float('-inf')
            for move in game.get_valid_moves():
                game.make_move(move)
                eval_score = self._minimax(game, depth - 1, alpha, beta, False)
                self._undo_move(game, move)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in game.get_valid_moves():
                game.make_move(move)
                eval_score = self._minimax(game, depth - 1, alpha, beta, True)
                self._undo_move(game, move)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval
    
    def _evaluate(self, game: Any) -> float:
        """Heuristic evaluation of position.
        
        Args:
            game: Game instance
            
        Returns:
            Evaluation score
        """
        # Could be enhanced with heuristics
        return 0
    
    def _undo_move(self, game: Any, move: int) -> None:
        """Undo a move by resetting and replaying.
        
        Note: This is inefficient. A better implementation would
        store game state for quick restoration.
        
        Args:
            game: Game instance
            move: Move to undo
        """
        # Save current state
        state = game.get_state().copy()
        player = game.current_player
        
        # Reset and replay all moves except last
        game.reset()
        moves = []
        
        # Find move sequence (simplified - stores externally in real implementation)
        # For now, we'll use a basic approach that works with stateless replay
