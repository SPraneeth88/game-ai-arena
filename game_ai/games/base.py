"""Base game class defining the interface for all games."""

from abc import ABC, abstractmethod
from typing import List, Tuple, Any


class BaseGame(ABC):
    """Abstract base class for all games in the arena.
    
    Attributes:
        board: Current game board state
        players: List of player IDs (typically [1, 2])
        current_player: Player whose turn it is
        done: Whether game is finished
    """
    
    def __init__(self):
        """Initialize the game."""
        self.board = None
        self.players = [1, 2]
        self.current_player = 1
        self.done = False
        self.winner = None
    
    @abstractmethod
    def reset(self) -> None:
        """Reset the game to initial state."""
        pass
    
    @abstractmethod
    def get_valid_moves(self) -> List[int]:
        """Get list of valid moves for current player.
        
        Returns:
            List of valid move indices
        """
        pass
    
    @abstractmethod
    def make_move(self, move: int) -> bool:
        """Execute a move in the game.
        
        Args:
            move: Move to make
            
        Returns:
            True if move was valid, False otherwise
        """
        pass
    
    @abstractmethod
    def get_state(self) -> Any:
        """Get current game state representation.
        
        Returns:
            State representation (typically numpy array or tensor)
        """
        pass
    
    @abstractmethod
    def get_winner(self) -> int:
        """Get winner of the game.
        
        Returns:
            Player ID of winner, 0 for draw, None if game ongoing
        """
        pass
    
    def switch_player(self) -> None:
        """Switch to the other player."""
        self.current_player = 3 - self.current_player  # Toggles between 1 and 2
    
    def is_done(self) -> bool:
        """Check if game is finished."""
        return self.done
