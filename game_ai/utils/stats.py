"""Game statistics tracking."""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class GameStats:
    """Statistics for a single game."""
    game_type: str
    agent1_name: str
    agent2_name: str
    winner: int
    total_moves: int
    duration_seconds: float
    
    def to_dict(self) -> Dict:
        """Convert to dictionary.
        
        Returns:
            Dictionary representation
        """
        return {
            'game_type': self.game_type,
            'agent1': self.agent1_name,
            'agent2': self.agent2_name,
            'winner': self.winner,
            'moves': self.total_moves,
            'duration': self.duration_seconds
        }
