"""
Test per CharacterForgeWeightedConditioning.
"""

import pytest
import torch
from nodes.weighted_conditioning import CharacterForgeWeightedConditioning


class TestWeightedConditioningInit:
    """Test inizializzazione."""
    
    def test_controller_exists(self):
        assert CharacterForgeWeightedConditioning is not None
    
    def test_input_types_structure(self):
        input_types = CharacterForgeWeightedConditioning.INPUT_TYPES()
        
        assert "required" in input_types
        assert "base_conditioning" in input_types["required"]
        assert "conditioning_1" in input_types["required"]
        assert "conditioning_2" in input_types["required"]
        assert "conditioning_3" in input_types["required"]
    
    def test_combination_methods_options(self):
        input_types = CharacterForgeWeightedConditioning.INPUT_TYPES()
        methods = input_types["required"]["combination_method"][0]
        
        assert "weighted_sum" in methods
        assert "average" in methods
        assert "concat" in methods
        assert "max" in methods
        assert "blend" in methods
    
    def test_return_types(self):
        assert CharacterForgeWeightedConditioning.RETURN_TYPES == ("CONDITIONING", "STRING")
    
    def test_category(self):
        assert CharacterForgeWeightedConditioning.CATEGORY == "CharacterForge/Advanced"


class TestWeightedConditioningValidation:
    """Test validazione input."""
    
    def test_invalid_base_conditioning(self, invalid_conditioning):
        controller = CharacterForgeWeightedConditioning()
        
        with pytest.raises(ValueError):
            controller.combine_weighted(
                invalid_conditioning, 
                [mock_conditioning], 1.0,
                [mock_conditioning], 0.8,
                [mock_conditioning], 0.6,
                "weighted_sum", True
            )
    
    def test_invalid_combination_method(self, mock_conditioning):
        controller = CharacterForgeWeightedConditioning()
        
        with pytest.raises(ValueError, match="non riconosciuto"):
            controller.combine_weighted(
                mock_conditioning,
                mock_conditioning, 1.0,
                mock_conditioning, 0.8,
                mock_conditioning, 0.6,
                "invalid_method", True
            )
    
    def test_zero_total_weights(self, mock_conditioning):
        controller = CharacterForgeWeightedConditioning()
        
        # Dovrebbe restituire base conditioning senza errore
        result = controller.combine_weighted(
            mock_conditioning,
            mock_conditioning, 0.0,
            mock_conditioning, 0.0,
            mock_conditioning, 0.0,
            "weighted_sum", True
        )
        
        assert result is not None


class TestWeightedConditioningExecution:
    """Test esecuzione con tutti i metodi."""
    
    @pytest.fixture
    def controller(self):
        return CharacterForgeWeightedConditioning()
    
    @pytest.mark.parametrize("method", [
        "weighted_sum", "average", "concat", "max", "blend"
    ])
    def test_all_methods_execution(self, controller, mock_conditioning, method):
        result = controller.combine_weighted(
            mock_conditioning,
            mock_conditioning, 0.8,
            mock_conditioning, 0.6,
            mock_conditioning, 0.7,
            method, True, 0.3
        )
        
        assert result is not None
        conditioning, info = result
        assert conditioning is not None
        assert isinstance(info, str)
    
    def test_preserve_structure_false(self, controller, mock_conditioning):
        result = controller.combine_weighted(
            mock_conditioning,
            mock_conditioning, 0.8,
            mock_conditioning, 0.6,
            mock_conditioning, 0.7,
            "weighted_sum", False
        )
        
        assert result is not None
    
    def test_structure_strength_variation(self, controller, mock_conditioning):
        """Test con diversi structure_strength."""
        for strength in [0.1, 0.3, 0.5, 0.7, 0.9]:
            result = controller.combine_weighted(
                mock_conditioning,
                mock_conditioning, 0.8,
                mock_conditioning, 0.6,
                mock_conditioning, 0.7,
                "blend", True, strength
            )
            
            assert result is not None


class TestWeightedConditioningInfo:
    """Test output info string."""
    
    def test_info_contains_method(self, mock_conditioning):
        controller = CharacterForgeWeightedConditioning()
        result = controller.combine_weighted(
            mock_conditioning,
            mock_conditioning, 0.8,
            mock_conditioning, 0.6,
            mock_conditioning, 0.7,
            "weighted_sum", True
        )
        
        _, info = result
        assert "weighted_sum" in info
        assert "WeightedConditioning" in info
    
    def test_info_contains_weights(self, mock_conditioning):
        controller = CharacterForgeWeightedConditioning()
        result = controller.combine_weighted(
            mock_conditioning,
            mock_conditioning, 0.8,
            mock_conditioning, 0.6,
            mock_conditioning, 0.7,
            "weighted_sum", True
        )
        
        _, info = result
        assert "0.8" in info or "0.267" in info  # Peso normalizzato