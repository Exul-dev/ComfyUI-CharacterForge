"""
Test per CharacterForgeHybridLatentSwitch.
"""

import pytest
import torch
from nodes.hybrid_switch import CharacterForgeHybridLatentSwitch


class TestHybridSwitchInit:
    """Test inizializzazione."""
    
    def test_controller_exists(self):
        assert CharacterForgeHybridLatentSwitch is not None
    
    def test_input_types_structure(self):
        input_types = CharacterForgeHybridLatentSwitch.INPUT_TYPES()
        
        assert "required" in input_types
        assert "mode" in input_types["required"]
        assert "text_latent" in input_types["required"]
        assert "image_latent" in input_types["required"]
    
    def test_mode_options(self):
        input_types = CharacterForgeHybridLatentSwitch.INPUT_TYPES()
        modes = input_types["required"]["mode"][0]
        
        assert "text_to_sheet" in modes
        assert "image_to_sheet" in modes
    
    def test_return_types(self):
        expected = ("LATENT", "STRING", "IMAGE")
        assert CharacterForgeHybridLatentSwitch.RETURN_TYPES == expected
    
    def test_category(self):
        assert CharacterForgeHybridLatentSwitch.CATEGORY == "CharacterForge/Hybrid"


class TestHybridSwitchValidation:
    """Test validazione."""
    
    def test_invalid_mode_raises_error(self, mock_latent):
        controller = CharacterForgeHybridLatentSwitch()
        
        with pytest.raises(ValueError, match="non riconosciuta"):
            controller.switch_latent("invalid_mode", mock_latent, mock_latent)
    
    def test_invalid_text_latent(self, mock_latent):
        controller = CharacterForgeHybridLatentSwitch()
        
        with pytest.raises(ValueError, match="text_latent non valido"):
            controller.switch_latent("text_to_sheet", None, mock_latent, auto_validate=True)
    
    def test_invalid_image_latent(self, mock_latent):
        controller = CharacterForgeHybridLatentSwitch()
        
        with pytest.raises(ValueError, match="image_latent non valido"):
            controller.switch_latent("image_to_sheet", mock_latent, None, auto_validate=True)


class TestHybridSwitchExecution:
    """Test esecuzione switch."""
    
    @pytest.fixture
    def controller(self):
        return CharacterForgeHybridLatentSwitch()
    
    def test_text_mode_execution(self, controller, mock_latent):
        result = controller.switch_latent("text_to_sheet", mock_latent, mock_latent)
        
        assert result is not None
        assert len(result) == 3
        
        selected_latent, mode_info, reference = result
        assert selected_latent is not None
        assert isinstance(mode_info, str)
    
    def test_image_mode_execution(self, controller, mock_latent):
        result = controller.switch_latent("image_to_sheet", mock_latent, mock_latent)
        
        assert result is not None
        selected_latent, mode_info, reference = result
        assert selected_latent is not None
    
    def test_with_image_reference(self, controller, mock_latent, mock_image):
        result = controller.switch_latent(
            "image_to_sheet", mock_latent, mock_latent, 
            image_reference=mock_image
        )
        
        assert result is not None
        selected_latent, mode_info, reference = result
        assert reference is not None
    
    def test_auto_validate_disabled(self, controller, mock_latent):
        """Test con auto_validate disabilitato (latent None)."""
        # Con auto_validate=False, None latent non genera errore
        result = controller.switch_latent(
            "text_to_sheet", None, mock_latent, auto_validate=False
        )
        
        # Dovrebbe comunque usare None come latent selected
        assert result is not None


class TestHybridSwitchLatentValidation:
    """Test validazione latent."""
    
    def test_valid_dict_latent(self, mock_latent):
        controller = CharacterForgeHybridLatentSwitch()
        is_valid, error = controller._validate_latent(mock_latent, "test")
        
        assert is_valid == True
        assert error is None
    
    def test_invalid_none_latent(self):
        controller = CharacterForgeHybridLatentSwitch()
        is_valid, error = controller._validate_latent(None, "test")
        
        assert is_valid == False
        assert "None" in error
    
    def test_invalid_empty_tensor_latent(self):
        controller = CharacterForgeHybridLatentSwitch()
        empty_latent = {"samples": torch.empty(0)}
        
        is_valid, error = controller._validate_latent(empty_latent, "test")
        
        assert is_valid == False
    
    def test_invalid_low_dim_tensor(self):
        controller = CharacterForgeHybridLatentSwitch()
        low_dim_latent = {"samples": torch.randn(10)}
        
        is_valid, error = controller._validate_latent(low_dim_latent, "test")
        
        assert is_valid == False
        assert "dimensioni" in error.lower() or "dimensions" in error.lower()


class TestHybridSwitchModeConfigs:
    """Test configurazioni modalità."""
    
    def test_mode_configs_exist(self):
        assert hasattr(CharacterForgeHybridLatentSwitch, 'MODE_CONFIGS')
        assert "text_to_sheet" in CharacterForgeHybridLatentSwitch.MODE_CONFIGS
        assert "image_to_sheet" in CharacterForgeHybridLatentSwitch.MODE_CONFIGS
    
    def test_text_mode_config(self):
        config = CharacterForgeHybridLatentSwitch.MODE_CONFIGS["text_to_sheet"]
        
        assert "description" in config
        assert "denoise_suggestion" in config
        assert config["denoise_suggestion"] == 1.0
    
    def test_image_mode_config(self):
        config = CharacterForgeHybridLatentSwitch.MODE_CONFIGS["image_to_sheet"]
        
        assert "description" in config
        assert "denoise_suggestion" in config
        assert config["denoise_suggestion"] == 0.6
    
    def test_mode_info_content(self, mock_latent):
        controller = CharacterForgeHybridLatentSwitch()
        result = controller.switch_latent("text_to_sheet", mock_latent, mock_latent)
        
        _, mode_info, _ = result
        assert "text_to_sheet" in mode_info
        assert "TEXT_TO_SHEET" in mode_info