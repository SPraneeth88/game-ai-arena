"""Game AI Arena - Advanced ML-powered game platform."""

__version__ = "1.0.0"
__author__ = "Your Name"

from .games import ConnectFour, TicTacToe
from .agents import RandomAgent, MinimaxAgent, NeuralAgent

__all__ = [
    "ConnectFour",
    "TicTacToe",
    "RandomAgent",
    "MinimaxAgent",
    "NeuralAgent",
]
