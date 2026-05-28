"""Neural network agent - uses trained neural network for move selection."""

import numpy as np
from typing import Any, Optional
import os

try:
    from tensorflow import keras
    HAS_TENSORFLOW = True
except ImportError:
    HAS_TENSORFLOW = False

from .base import BaseAgent


class NeuralAgent(BaseAgent):
    """Agent using neural network for move selection.
    
    The network learns to evaluate positions and select strong moves.
    """
    
    def __init__(self, player_id: int, model: Optional[Any] = None, model_path: Optional[str] = None):
        """Initialize neural agent.
        
        Args:
            player_id: Player ID (1 or 2)
            model: Keras model instance
            model_path: Path to saved model
        """
        super().__init__(player_id, name="Neural")
        
        if model is not None:
            self.model = model
        elif model_path and os.path.exists(model_path):
            if HAS_TENSORFLOW:
                self.model = keras.models.load_model(model_path)
            else:
                raise ImportError("TensorFlow required to load model")
        else:
            self.model = self._build_default_model()
    
    def get_move(self, game: Any) -> int:
        """Select move using neural network.
        
        Args:
            game: Game instance
            
        Returns:
            Selected move
        """
        valid_moves = game.get_valid_moves()
        
        if not HAS_TENSORFLOW or self.model is None:
            # Fallback to random if model unavailable
            return valid_moves[np.random.randint(len(valid_moves))]
        
        # Evaluate each valid move
        best_move = None
        best_score = float('-inf')
        
        for move in valid_moves:
            # Create state after move
            game.make_move(move)
            state = game.get_state().reshape(1, -1)
            
            try:
                score = self.model.predict(state, verbose=0)[0][0]
            except Exception:
                score = np.random.random()
            
            self._undo_last_move(game)
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _build_default_model(self) -> Optional[Any]:
        """Build a default neural network model.
        
        Returns:
            Keras model or None if TensorFlow unavailable
        """
        if not HAS_TENSORFLOW:
            return None
        
        model = keras.Sequential([
            keras.layers.Dense(128, activation='relu', input_dim=9),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(1, activation='tanh')
        ])
        
        model.compile(optimizer='adam', loss='mse')
        return model
    
    def _undo_last_move(self, game: Any) -> None:
        """Undo the last move made.
        
        Args:
            game: Game instance
        """
        # Simplified undo - would need proper move history for production
        pass
    
    def save(self, path: str) -> None:
        """Save model to file.
        
        Args:
            path: Path to save model
        """
        if self.model and HAS_TENSORFLOW:
            self.model.save(path)
