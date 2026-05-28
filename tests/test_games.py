"""Tests for game implementations."""

import pytest
import sys
sys.path.insert(0, '..')

from game_ai.games import TicTacToe, ConnectFour


class TestTicTacToe:
    """Tests for Tic-Tac-Toe game."""
    
    def test_initialization(self):
        """Test game initializes correctly."""
        game = TicTacToe()
        assert game.current_player == 1
        assert not game.is_done()
        assert len(game.get_valid_moves()) == 9
    
    def test_valid_moves(self):
        """Test valid moves are correct."""
        game = TicTacToe()
        game.make_move(0)
        moves = game.get_valid_moves()
        assert 0 not in moves
        assert len(moves) == 8
    
    def test_horizontal_win(self):
        """Test horizontal win detection."""
        game = TicTacToe()
        # Player 1 wins: top row
        game.make_move(0)  # X
        game.make_move(3)  # O
        game.make_move(1)  # X
        game.make_move(4)  # O
        game.make_move(2)  # X - wins!
        
        assert game.get_winner() == 1
        assert game.is_done()
    
    def test_draw(self):
        """Test draw detection."""
        game = TicTacToe()
        moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for move in moves:
            if not game.is_done():
                game.make_move(move)
        
        assert game.get_winner() == 0
        assert game.is_done()


class TestConnectFour:
    """Tests for Connect Four game."""
    
    def test_initialization(self):
        """Test game initializes correctly."""
        game = ConnectFour()
        assert game.current_player == 1
        assert not game.is_done()
        assert len(game.get_valid_moves()) == 7
    
    def test_gravity(self):
        """Test pieces fall due to gravity."""
        game = ConnectFour()
        game.make_move(0)  # Drop in column 0
        game.make_move(0)  # Drop in column 0 again
        
        board = game.board
        assert board[5, 0] == 1  # Bottom
        assert board[4, 0] == 2  # One above
    
    def test_column_full(self):
        """Test column becomes invalid when full."""
        game = ConnectFour()
        # Fill column 0
        for i in range(12):
            if 0 in game.get_valid_moves():
                game.make_move(0)
        
        assert 0 not in game.get_valid_moves()
    
    def test_horizontal_win(self):
        """Test horizontal win detection."""
        game = ConnectFour()
        # Player 1 wins: row 5, columns 0-3
        for col in range(4):
            game.make_move(col)  # Player 1
            if col < 3:
                game.make_move(4)  # Player 2
        
        assert game.get_winner() == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
