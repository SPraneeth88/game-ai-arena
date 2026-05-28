"""Example: Running a tournament between AI agents."""

import time
from game_ai.games import TicTacToe, ConnectFour
from game_ai.agents import RandomAgent, MinimaxAgent
from game_ai.utils import Tournament, GameResult


def play_tournament(game_class, num_games=5):
    """Run a tournament between agents.
    
    Args:
        game_class: Game class to use
        num_games: Number of games to play
    """
    tournament = Tournament()
    
    # Create agents
    random1 = RandomAgent(1)
    random2 = RandomAgent(2)
    minimax1 = MinimaxAgent(1, depth=4)
    minimax2 = MinimaxAgent(2, depth=4)
    
    matchups = [
        (minimax1, random2, "Minimax vs Random"),
        (random1, minimax2, "Random vs Minimax"),
    ]
    
    for agent1, agent2, description in matchups:
        print(f"\n{'='*50}")
        print(f"Tournament: {description}")
        print(f"{'='*50}")
        
        for game_num in range(num_games):
            game = game_class()
            start_time = time.time()
            
            while not game.is_done():
                if game.current_player == 1:
                    move = agent1.get_move(game)
                else:
                    move = agent2.get_move(game)
                
                game.make_move(move)
            
            duration = time.time() - start_time
            winner = game.get_winner()
            moves = sum(1 for x in game.get_state() if x != 0)
            
            result = GameResult(
                agent1_name=agent1.name,
                agent2_name=agent2.name,
                winner=winner,
                moves=moves,
                game_type=game_class.__name__
            )
            
            tournament.add_result(result)
            
            result_str = "Draw" if winner == 0 else f"{agent1.name if winner == 1 else agent2.name} wins"
            print(f"Game {game_num + 1}: {result_str} ({moves} moves in {duration:.2f}s)")
    
    print(f"\n{'='*50}")
    print("Final Leaderboard")
    print(f"{'='*50}")
    print(tournament.summary())


if __name__ == "__main__":
    print("🎮 Game AI Arena - Tournament Demo")
    print("="*50)
    
    # Run Tic-Tac-Toe tournament
    print("\n📍 Tic-Tac-Toe Tournament")
    play_tournament(TicTacToe, num_games=3)
    
    # Run Connect Four tournament
    print("\n📍 Connect Four Tournament")
    play_tournament(ConnectFour, num_games=2)
