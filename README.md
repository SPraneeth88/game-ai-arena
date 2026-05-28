
# 🎮 Game AI Arena

A sophisticated Python platform for developing, training, and competing AI agents in classic games. Demonstrates advanced software engineering practices including game theory, machine learning, and scalable architecture.

## Features

### Games
- **Tic-Tac-Toe**: Classic 3x3 game with optimal play achievable
- **Connect Four**: Strategic 7x6 game with complex decision space

### AI Agents
- **Random Agent**: Baseline random move selection
- **Minimax Agent**: Game-tree search with alpha-beta pruning for optimal play
- **Neural Agent**: Deep learning-based agent (requires TensorFlow)

### Platform Capabilities
- Tournament system for agent competitions
- Statistical tracking and leaderboards
- Interactive Streamlit web interface
- Comprehensive test suite
- Production-ready code structure

## Architecture

```
game_ai/
├── games/          # Game implementations (base, Tic-Tac-Toe, Connect Four)
├── agents/         # AI agent implementations
├── utils/          # Tournament and statistics utilities
web/                # Streamlit web interface
tests/              # Comprehensive test suite
```

## Installation

### Basic Setup
```bash
git clone https://github.com/yourusername/game-ai-arena.git
cd game-ai-arena
pip install -r requirements.txt
```

### With ML Support
```bash
pip install -r requirements.txt
pip install tensorflow>=2.10.0
```

### Development Setup
```bash
pip install -e ".[dev,ml]"
```

## Usage

### Interactive Web Interface
```bash
cd web
streamlit run app.py
```

### Programmatic Usage
```python
from game_ai.games import TicTacToe, ConnectFour
from game_ai.agents import RandomAgent, MinimaxAgent

# Create game and agents
game = TicTacToe()
agent1 = MinimaxAgent(player_id=1)
agent2 = RandomAgent(player_id=2)

# Play game
while not game.is_done():
    if game.current_player == 1:
        move = agent1.get_move(game)
    else:
        move = agent2.get_move(game)
    
    game.make_move(move)

print(f"Winner: {game.get_winner()}")
```

### Running Tournaments
```python
from game_ai.games import TicTacToe
from game_ai.agents import MinimaxAgent, RandomAgent
from game_ai.utils import Tournament, GameResult

tournament = Tournament()
game = TicTacToe()
agent1 = MinimaxAgent(1)
agent2 = RandomAgent(2)

# Play multiple games
for _ in range(10):
    game.reset()
    while not game.is_done():
        move = agent1.get_move(game) if game.current_player == 1 else agent2.get_move(game)
        game.make_move(move)
    
    result = GameResult(
        agent1_name=agent1.name,
        agent2_name=agent2.name,
        winner=game.get_winner(),
        moves=sum(1 for m in game.board.flatten() if m != 0),
        game_type="TicTacToe"
    )
    tournament.add_result(result)

print(tournament.summary())
```

## Testing

```bash
pytest tests/ -v
pytest tests/ --cov=game_ai  # With coverage
```

## Performance

### Tic-Tac-Toe
- Minimax finds optimal play in ~100ms
- Perfect play leads to draws

### Connect Four
- Minimax with depth limit plays strategically
- Typical decision time: 50-500ms depending on depth

## Development

### Code Style
```bash
black game_ai/
flake8 game_ai/
```

### Architecture Decisions

1. **Modular Design**: Games and agents are independent, allowing easy extension
2. **Type Hints**: Full type annotations for better IDE support
3. **Scalability**: Designed to add new games and agents without modifying core
4. **Testing**: Comprehensive test suite ensures reliability

## Future Enhancements

- [ ] Monte Carlo Tree Search (MCTS) agent
- [ ] Reinforcement learning agent with Q-learning
- [ ] More games (Chess, Checkers, Poker)
- [ ] Web-based tournament viewer
- [ ] Agent training pipeline
- [ ] Performance profiling tools
- [ ] Docker containerization

## Contributing

Contributions welcome! Areas for enhancement:
- New game implementations
- Improved AI algorithms
- Web interface enhancements
- Performance optimization
- Documentation improvements

## License

MIT License - see LICENSE file for details

## Author

Your Name - [GitHub Profile](https://github.com/yourusername)

---

**Built with Python** • **AI** • **Game Theory** • **Software Engineering Best Practices**
