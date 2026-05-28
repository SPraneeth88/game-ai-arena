"""Base agent class."""

from abc import ABC, abstractmethod
from typing import Any, List


class BaseAgent(ABC):
    """Abstract base class for game-playing agents.
    
    Attributes:
        player_id: Player ID (1 or 2)
        name: Agent name for display
    """
    
    def __init__(self, player_id: int, name: str = None):
        """Initialize agent.
        
        Args:
            player_id: Player ID (1 or 2)
            name: Agent name
        """
        self.player_id = player_id
        self.name = name or self.__class__.__name__
    
    @abstractmethod
    def get_move(self, game: Any) -> int:
        """Select move for current game state.
        
        Args:
            game: Game instance
            
        Returns:
            Selected move
        """
        pass
    
    def __repr__(self) -> str:
        """String representation."""
        return f"{self.name}(Player {self.player_id})"
