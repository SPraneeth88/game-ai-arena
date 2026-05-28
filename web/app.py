"""Streamlit web interface for Game AI Arena."""

import streamlit as st
import numpy as np
from datetime import datetime

# Import game and agent classes
import sys
sys.path.insert(0, '..')

from game_ai.games import TicTacToe, ConnectFour
from game_ai.agents import RandomAgent, MinimaxAgent


def render_board_tictactoe(board):
    """Render Tic-Tac-Toe board."""
    col1, col2, col3 = st.columns(3)
    symbols = {0: "⬜", 1: "❌", 2: "⭕"}
    
    cells = []
    for i in range(9):
        cells.append(symbols[board.flatten()[i]])
    
    with col1:
        st.text(f"{cells[0]} {cells[1]} {cells[2]}")
    with col2:
        st.text("")
    with col3:
        st.text(f"{cells[3]} {cells[4]} {cells[5]}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(f"{cells[6]} {cells[7]} {cells[8]}")


def render_board_connect4(board):
    """Render Connect Four board."""
    symbols = {0: "⬜", 1: "🟡", 2: "🔴"}
    
    for row in board:
        st.text(" ".join(symbols[cell] for cell in row))


def main():
    """Main Streamlit app."""
    st.set_page_config(page_title="Game AI Arena", layout="wide")
    st.title("🎮 Game AI Arena")
    st.markdown("Watch AI agents compete in classic games!")
    
    # Sidebar
    with st.sidebar:
        st.header("Configuration")
        game_type = st.selectbox("Select Game", ["Tic-Tac-Toe", "Connect Four"])
        agent1_type = st.selectbox("Agent 1", ["Random", "Minimax"], key="agent1")
        agent2_type = st.selectbox("Agent 2", ["Random", "Minimax"], key="agent2")
        
        if st.button("Start Game"):
            st.session_state.game_started = True
            st.session_state.game_log = []
    
    # Main area
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Game Board")
        
        # Initialize game
        if 'game' not in st.session_state or st.session_state.get('game_type') != game_type:
            if game_type == "Tic-Tac-Toe":
                st.session_state.game = TicTacToe()
            else:
                st.session_state.game = ConnectFour()
            st.session_state.game_type = game_type
        
        # Initialize agents
        if 'agent1' not in st.session_state or not st.session_state.get('game_started'):
            if agent1_type == "Random":
                st.session_state.agent1 = RandomAgent(1)
            else:
                st.session_state.agent1 = MinimaxAgent(1, depth=6)
            
            if agent2_type == "Random":
                st.session_state.agent2 = RandomAgent(2)
            else:
                st.session_state.agent2 = MinimaxAgent(2, depth=6)
        
        game = st.session_state.game
        
        # Render board
        if game_type == "Tic-Tac-Toe":
            render_board_tictactoe(game.board)
        else:
            render_board_connect4(game.board)
        
        # Play game automatically
        if st.session_state.get('game_started', False) and not game.is_done():
            agent = st.session_state.agent1 if game.current_player == 1 else st.session_state.agent2
            move = agent.get_move(game)
            game.make_move(move)
            st.rerun()
        
        # Show result
        if game.is_done():
            if game.winner == 0:
                st.success("🤝 Draw!")
            else:
                winner_agent = st.session_state.agent1 if game.winner == 1 else st.session_state.agent2
                st.success(f"🎉 {winner_agent.name} wins!")
    
    with col2:
        st.subheader("Game Info")
        col2a, col2b = st.columns(2)
        
        with col2a:
            st.metric("Current Player", "Agent 1" if game.current_player == 1 else "Agent 2")
            st.metric("Valid Moves", len(game.get_valid_moves()))
        
        with col2b:
            st.metric("Agent 1", st.session_state.agent1.name)
            st.metric("Agent 2", st.session_state.agent2.name)
        
        if st.button("Reset Game"):
            st.session_state.game.reset()
            st.session_state.game_started = False
            st.rerun()


if __name__ == "__main__":
    main()
