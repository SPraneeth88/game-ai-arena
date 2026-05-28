"""Tournament system for agents."""

from typing import List, Dict, Any
from dataclasses import dataclass, field


@dataclass
class GameResult:
    """Result of a single game."""
    agent1_name: str
    agent2_name: str
    winner: int  # 1, 2, or 0 for draw
    moves: int
    game_type: str


@dataclass
class AgentStats:
    """Statistics for an agent."""
    name: str
    wins: int = 0
    losses: int = 0
    draws: int = 0
    
    @property
    def games_played(self) -> int:
        """Total games played."""
        return self.wins + self.losses + self.draws
    
    @property
    def win_rate(self) -> float:
        """Win rate percentage."""
        if self.games_played == 0:
            return 0.0
        return (self.wins / self.games_played) * 100
    
    def __repr__(self) -> str:
        """String representation."""
        return (f"{self.name}: {self.wins}W-{self.losses}L-{self.draws}D "
                f"({self.win_rate:.1f}%)")


class Tournament:
    """Tournament manager for running agent competitions."""
    
    def __init__(self):
        """Initialize tournament."""
        self.results: List[GameResult] = []
        self.stats: Dict[str, AgentStats] = {}
    
    def add_result(self, result: GameResult) -> None:
        """Record game result.
        
        Args:
            result: GameResult instance
        """
        self.results.append(result)
        
        # Update stats
        if result.agent1_name not in self.stats:
            self.stats[result.agent1_name] = AgentStats(result.agent1_name)
        if result.agent2_name not in self.stats:
            self.stats[result.agent2_name] = AgentStats(result.agent2_name)
        
        if result.winner == 1:
            self.stats[result.agent1_name].wins += 1
            self.stats[result.agent2_name].losses += 1
        elif result.winner == 2:
            self.stats[result.agent2_name].wins += 1
            self.stats[result.agent1_name].losses += 1
        else:
            self.stats[result.agent1_name].draws += 1
            self.stats[result.agent2_name].draws += 1
    
    def get_leaderboard(self) -> List[AgentStats]:
        """Get agents sorted by win rate.
        
        Returns:
            List of AgentStats sorted by performance
        """
        return sorted(self.stats.values(), 
                     key=lambda x: (x.win_rate, x.wins), 
                     reverse=True)
    
    def summary(self) -> str:
        """Get tournament summary.
        
        Returns:
            Formatted summary string
        """
        lines = ["Tournament Summary", "=" * 50]
        for stats in self.get_leaderboard():
            lines.append(str(stats))
        return "\n".join(lines)
