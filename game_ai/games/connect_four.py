"""Connect Four game implementation."""

import numpy as np
from typing import List
from .base import BaseGame


class ConnectFour(BaseGame):
    """Connect Four (7x6) implementation.
    
    Board representation:
        0 = empty
        1 = player 1 (Yellow)
        2 = player 2 (Red)
    """
    
    ROWS = 6
    COLS = 7
    WIN_LENGTH = 4
    
    def __init__(self):
        """Initialize Connect Four game."""
        super().__init__()
        self.reset()
    
    def reset(self) -> None:
        """Reset the game to initial state."""
        self.board = np.zeros((self.ROWS, self.COLS), dtype=np.int8)
        self.current_player = 1
        self.done = False
        self.winner = None
    
    def get_valid_moves(self) -> List[int]:
        """Get list of valid moves (columns not full).
        
        Returns:
            List of valid column indices (0-6)
        """
        return [col for col in range(self.COLS) if self.board[0, col] == 0]
    
    def make_move(self, move: int) -> bool:
        """Execute a move by dropping piece in column.
        
        Args:
            move: Column index (0-6)
            
        Returns:
            True if successful, False if invalid
        """
        if move < 0 or move >= self.COLS or self.board[0, move] != 0:
            return False
        
        # Find lowest empty row in column
        for row in range(self.ROWS - 1, -1, -1):
            if self.board[row, move] == 0:
                self.board[row, move] = self.current_player
                break
        
        # Check if game is over
        winner = self.get_winner()
        if winner is not None:
            self.done = True
            self.winner = winner
        elif len(self.get_valid_moves()) == 0:
            self.done = True
            self.winner = 0  # Draw
        else:
            self.switch_player()
        
        return True
    
    def get_state(self) -> np.ndarray:
        """Get current board state.
        
        Returns:
            Flattened board array (42,)
        """
        return self.board.flatten().copy()
    
    def get_winner(self) -> int:
        """Check for winner.
        
        Returns:
            1 or 2 for winner, 0 for draw, None if ongoing
        """
        # Check horizontal
        for row in range(self.ROWS):
            for col in range(self.COLS - self.WIN_LENGTH + 1):
                window = self.board[row, col:col + self.WIN_LENGTH]
                if np.all(window == 1) or np.all(window == 2):
                    return window[0]
        
        # Check vertical
        for col in range(self.COLS):
            for row in range(self.ROWS - self.WIN_LENGTH + 1):
                window = self.board[row:row + self.WIN_LENGTH, col]
                if np.all(window == 1) or np.all(window == 2):
                    return window[0]
        
        # Check diagonal (bottom-left to top-right)
        for row in range(self.ROWS - self.WIN_LENGTH + 1):
            for col in range(self.COLS - self.WIN_LENGTH + 1):
                window = np.diagonal(self.board[row:row + self.WIN_LENGTH, col:col + self.WIN_LENGTH])
                if np.all(window == 1) or np.all(window == 2):
                    return window[0]
        
        # Check diagonal (top-left to bottom-right)
        for row in range(self.WIN_LENGTH - 1, self.ROWS):
            for col in range(self.COLS - self.WIN_LENGTH + 1):
                window = np.diagonal(np.fliplr(self.board[row - self.WIN_LENGTH + 1:row + 1, col:col + self.WIN_LENGTH]))
                if np.all(window == 1) or np.all(window == 2):
                    return window[0]
        
        # Check if board is full
        if len(self.get_valid_moves()) == 0:
            return 0
        
        return None
    
    def render(self) -> str:
        """Get string representation of the board."""
        symbols = {0: ".", 1: "Y", 2: "R"}
        lines = []
        for row in self.board:
            lines.append(" ".join(symbols[cell] for cell in row))
        return "\n".join(lines)
