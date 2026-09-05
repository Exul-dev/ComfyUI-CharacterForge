"""
Test per CharacterForgeGenderController.
"""

import pytest
import torch
from nodes.gender_controller import CharacterForgeGenderController


class TestGenderControllerInit:
    """Test inizializzazione controller."""
    
    def test_controller_exists(self):
        """Verifica che il controller esista."""
        assert CharacterForgeGenderController is not None
    
    def test_input_types_structure(self):
        """Verifica struttura INPUT_TYPES."""
        input_types = CharacterForgeGenderController.INPUT_TYPES()
        
        assert "required" in input_types
        assert "optional" in input_types
        
        required = input_types["required"]
        assert "conditioning" in required
        assert "gender" in required
        assert "weight" in required
    
    def test_gender_options(self):
        """Verifica opzioni genere disponibili."""
        input_types = CharacterForgeGenderController.INPUT_TYPES()
        gender_options = input_types["required"]["gender"][0]
        
        assert "masculine" in gender_options
        assert "feminine" in gender_options
        assert "androgynous" in gender_options
        assert "custom" in gender_options
    
    def test_return_types(self):
        """Verifica tipi di ritorno."""
        assert CharacterForgeGenderController.RETURN_TYPES == ("CONDITIONING", "STRING")
        assert CharacterForgeGenderController.RETURN_NAMES == ("conditioning", "applied_features")
    
    def test_category(self):
        """Verifica categoria."""
        assert CharacterForgeGenderController.CATEGORY == "CharacterForge/Basic"
    
    def test_function_name(self):
        """Verifica nome funzione."""
        assert CharacterForgeGenderController.FUNCTION == "apply_gender_control"


class TestGenderControllerValidation:
    """Test validazione input."""
    
    def test_invalid_conditioning_raises_error(self, invalid_conditioning):
        """Test conditioning None genera errore."""
        controller = CharacterForgeGenderController()
        
        with pytest.raises(ValueError, match="Conditioning input non valido"):
            controller.apply_gender_control(invalid_conditioning, "masculine", 0.8)
    
    def test_empty_conditioning_raises_error(self, empty_conditioning):
        """Test conditioning vuoto genera errore."""
        controller = CharacterForgeGenderController()
        
        with pytest.raises(ValueError, match="Conditioning input non valido"):
            controller.apply_gender_control(empty_conditioning, "masculine", 0.8)
    
    def test_custom_gender_without_prompt_raises_error(self, mock_conditioning):
        """Test custom senza prompt genera errore."""
        controller = CharacterForgeGenderController()
        
        with pytest.raises(ValueError, match="Prompt custom richiesto"):
            controller.apply_gender_control(mock_conditioning, "custom", 0.8, "")


class TestGenderControllerExecution:
    """Test esecuzione controller."""
    
    @pytest.fixture
    def controller(self):
        return CharacterForgeGenderController()
    
    def test_masculine_execution(self, controller, mock_conditioning):
        """Test esecuzione con genere maschile."""
        result = controller.apply_gender_control(mock_conditioning, "masculine", 0.8)
        
        assert result is not None
        assert len(result) == 2
        
        conditioning, features = result
        assert conditioning is not None
        assert isinstance(features, str)
    
    def test_feminine_execution(self, controller, mock_conditioning):
        """Test esecuzione con genere femminile."""
        result = controller.apply_gender_control(mock_conditioning, "feminine", 0.8)
        
        assert result is not None
        conditioning, features = result
        assert conditioning is not None
    
    def test_androgynous_execution(self, controller, mock_conditioning):
        """Test esecuzione con genere androgino."""
        result = controller.apply_gender_control(mock_conditioning, "androgynous", 0.7)
        
        assert result is not None
        conditioning, features = result
        assert conditioning is not None
    
    def test_custom_with_prompt_execution(self, controller, mock_conditioning):
        """Test esecuzione con custom prompt."""
        custom_prompt = "Adult male, 30 years, Italian features"
        result = controller.apply_gender_control(mock_conditioning, "custom", 0.9, custom_prompt)
        
        assert result is not None
        conditioning, features = result
        assert conditioning is not None
    
    def test_weight_zero_execution(self, controller, mock_conditioning):
        """Test esecuzione con peso zero."""
        result = controller.apply_gender_control(mock_conditioning, "masculine", 0.0)
        
        assert result is not None
        conditioning, features = result
        assert conditioning is not None
    
    def test_weight_max_execution(self, controller, mock_conditioning):
        """Test esecuzione con peso massimo."""
        result = controller.apply_gender_control(mock_conditioning, "masculine", 1.5)
        
        assert result is not None
        conditioning, features = result
        assert conditioning is not None
    
    def test_batch_conditioning(self, controller, mock_conditioning_batch):
        """Test esecuzione con batch conditioning."""
        result = controller.apply_gender_control(mock_conditioning_batch, "masculine", 0.8)
        
        assert result is not None
        conditioning, features = result
        assert len(conditioning) == 3


class TestGenderControllerMetadata:
    """Test metadati conditioning."""
    
    def test_metadata_added(self, mock_conditioning):
        """Test metadati characterforge_gender aggiunti."""
        controller = CharacterForgeGenderController()
        result = controller.apply_gender_control(mock_conditioning, "masculine", 0.8)
        
        conditioning, _ = result
        cond_tensor, cond_dict = conditioning[0]
        
        assert "characterforge_gender" in cond_dict
        assert cond_dict["characterforge_gender"]["type"] == "masculine"
        assert cond_dict["characterforge_gender"]["weight"] == 0.8
    
    def test_features_string_content(self, mock_conditioning):
        """Test contenuto stringa features."""
        controller = CharacterForgeGenderController()
        result = controller.apply_gender_control(mock_conditioning, "feminine", 0.8)
        
        _, features = result
        assert "GenderController" in features
        assert "feminine" in features
        assert "0.8" in features


class TestGenderControllerPresets:
    """Test preset di genere."""
    
    def test_presets_exist(self):
        """Test esistenza preset."""
        assert hasattr(CharacterForgeGenderController, 'GENDER_PRESETS')
        assert len(CharacterForgeGenderController.GENDER_PRESETS) == 4
    
    def test_preset_content(self):
        """Test contenuto preset."""
        presets = CharacterForgeGenderController.GENDER_PRESETS
        
        assert "prompt" in presets["masculine"]
        assert "prompt" in presets["feminine"]
        assert "prompt" in presets["androgynous"]
        assert "weight_suggestion" in presets["masculine"]