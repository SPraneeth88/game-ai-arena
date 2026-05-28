"""Tic-Tac-Toe game implementation."""

import numpy as np
from typing import List, Tuple
from .base import BaseGame


class TicTacToe(BaseGame):
    """Classic Tic-Tac-Toe (3x3) implementation.
    
    Board representation:
        0 = empty
        1 = player 1 (X)
        2 = player 2 (O)
    """
    
    SIZE = 3
    
    def __init__(self):
        """Initialize Tic-Tac-Toe game."""
        super().__init__()
        self.reset()
    
    def reset(self) -> None:
        """Reset the game to initial state."""
        self.board = np.zeros((self.SIZE, self.SIZE), dtype=np.int8)
        self.current_player = 1
        self.done = False
        self.winner = None
    
    def get_valid_moves(self) -> List[int]:
        """Get list of valid moves (empty positions).
        
        Returns:
            List of flat indices (0-8) of empty cells
        """
        return list(np.where(self.board.flatten() == 0)[0])
    
    def make_move(self, move: int) -> bool:
        """Execute a move.
        
        Args:
            move: Flat index (0-8) where to place mark
            
        Returns:
            True if successful, False if invalid
        """
        if move < 0 or move >= 9:
            return False
        
        row, col = divmod(move, self.SIZE)
        if self.board[row, col] != 0:
            return False
        
        self.board[row, col] = self.current_player
        
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
            Flattened board array (9,)
        """
        return self.board.flatten().copy()
    
    def get_winner(self) -> int:
        """Get winner of the game.
        
        Returns:
            1 or 2 for winner, 0 for draw, None if ongoing
        """
        # Check rows
        for row in self.board:
            if np.all(row == 1):
                return 1
            if np.all(row == 2):
                return 2
        
        # Check columns
        for col in self.board.T:
            if np.all(col == 1):
                return 1
            if np.all(col == 2):
                return 2
        
        # Check diagonals
        if np.all(np.diag(self.board) == 1) or np.all(np.diag(np.fliplr(self.board)) == 1):
            return 1
        if np.all(np.diag(self.board) == 2) or np.all(np.diag(np.fliplr(self.board)) == 2):
            return 2
        
        # Check if board is full (draw)
        if len(self.get_valid_moves()) == 0:
            return 0
        
        return None
    
    def render(self) -> str:
        """Get string representation of the board."""
        symbols = {0: " ", 1: "X", 2: "O"}
        lines = []
        for i, row in enumerate(self.board):
            line = " | ".join(symbols[cell] for cell in row)
            lines.append(line)
            if i < 2:
                lines.append("-----------")
        return "\n".join(lines)
