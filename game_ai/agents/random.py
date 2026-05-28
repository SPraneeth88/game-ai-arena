"""Random agent - plays random valid moves."""

import random
from typing import Any
from .base import BaseAgent


class RandomAgent(BaseAgent):
    """Agent that plays random valid moves.
    
    Useful as a baseline for comparison.
    """
    
    def __init__(self, player_id: int):
        """Initialize random agent.
        
        Args:
            player_id: Player ID (1 or 2)
        """
        super().__init__(player_id, name="Random")
    
    def get_move(self, game: Any) -> int:
        """Select random valid move.
        
        Args:
            game: Game instance
            
        Returns:
            Random valid move
        """
        valid_moves = game.get_valid_moves()
        return random.choice(valid_moves)
