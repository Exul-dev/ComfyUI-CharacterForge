"""
Test per CharacterForgeEthnicityController.
"""

import pytest
import torch
from nodes.ethnicity_controller import CharacterForgeEthnicityController


class TestEthnicityControllerInit:
    """Test inizializzazione controller."""
    
    def test_controller_exists(self):
        assert CharacterForgeEthnicityController is not None
    
    def test_input_types_structure(self):
        input_types = CharacterForgeEthnicityController.INPUT_TYPES()
        
        assert "required" in input_types
        assert "optional" in input_types
        assert "conditioning" in input_types["required"]
        assert "primary_ethnicity" in input_types["required"]
        assert "weight" in input_types["required"]
    
    def test_ethnicity_options(self):
        input_types = CharacterForgeEthnicityController.INPUT_TYPES()
        ethnicities = input_types["required"]["primary_ethnicity"][0]
        
        assert "caucasian" in ethnicities
        assert "african" in ethnicities
        assert "asian" in ethnicities
        assert "latin" in ethnicities
        assert "mixed" in ethnicities
    
    def test_secondary_ethnicity_options(self):
        input_types = CharacterForgeEthnicityController.INPUT_TYPES()
        secondary = input_types["optional"]["secondary_ethnicity"][0]
        
        assert "none" in secondary
        assert "caucasian" in secondary
    
    def test_return_types(self):
        assert CharacterForgeEthnicityController.RETURN_TYPES == ("CONDITIONING", "STRING")
    
    def test_category(self):
        assert CharacterForgeEthnicityController.CATEGORY == "CharacterForge/Advanced"


class TestEthnicityControllerValidation:
    """Test validazione input."""
    
    def test_invalid_conditioning(self, invalid_conditioning):
        controller = CharacterForgeEthnicityController()
        
        with pytest.raises(ValueError):
            controller.apply_ethnicity_control(invalid_conditioning, "caucasian", 0.6)
    
    def test_invalid_ethnicity(self, mock_conditioning):
        controller = CharacterForgeEthnicityController()
        
        with pytest.raises(ValueError, match="non riconosciuta"):
            controller.apply_ethnicity_control(mock_conditioning, "invalid_ethnicity", 0.6)
    
    def test_invalid_secondary_ethnicity(self, mock_conditioning):
        controller = CharacterForgeEthnicityController()
        
        with pytest.raises(ValueError):
            controller.apply_ethnicity_control(
                mock_conditioning, "caucasian", 0.6, "invalid_secondary"
            )


class TestEthnicityControllerExecution:
    """Test esecuzione controller."""
    
    @pytest.fixture
    def controller(self):
        return CharacterForgeEthnicityController()
    
    @pytest.mark.parametrize("ethnicity", [
        "caucasian", "african", "asian", "latin", "mixed"
    ])
    def test_all_ethnicities_execution(self, controller, mock_conditioning, ethnicity):
        """Test esecuzione con tutte le etnie."""
        result = controller.apply_ethnicity_control(mock_conditioning, ethnicity, 0.6)
        
        assert result is not None
        conditioning, details = result
        assert conditioning is not None
    
    def test_mixed_ethnicity_execution(self, controller, mock_conditioning):
        """Test esecuzione con etnia mista."""
        result = controller.apply_ethnicity_control(
            mock_conditioning, "caucasian", 0.7, "asian"
        )
        
        assert result is not None
        conditioning, details = result
        assert conditioning is not None
    
    def test_skin_tone_override_execution(self, controller, mock_conditioning):
        """Test esecuzione con override tono pelle."""
        result = controller.apply_ethnicity_control(
            mock_conditioning, "african", 0.8, "none", "deep bronze"
        )
        
        assert result is not None
        conditioning, details = result
        assert conditioning is not None
    
    def test_custom_details_execution(self, controller, mock_conditioning):
        """Test esecuzione con dettagli custom."""
        result = controller.apply_ethnicity_control(
            mock_conditioning, "caucasian", 0.8, "none", "", "Mediterranean features"
        )
        
        assert result is not None
        conditioning, details = result
        assert conditioning is not None


class TestEthnicityControllerDatabase:
    """Test database etnie."""
    
    def test_database_exists(self):
        assert hasattr(CharacterForgeEthnicityController, 'ETHNICITY_DATABASE')
        assert len(CharacterForgeEthnicityController.ETHNICITY_DATABASE) == 5
    
    @pytest.mark.parametrize("ethnicity", [
        "caucasian", "african", "asian", "latin", "mixed"
    ])
    def test_database_structure(self, ethnicity):
        db = CharacterForgeEthnicityController.ETHNICITY_DATABASE
        assert ethnicity in db
        
        entry = db[ethnicity]
        assert "skin" in entry
        assert "facial" in entry
        assert "hair" in entry
        assert "eyes" in entry
        assert "heritage" in entry


class TestEthnicityControllerMetadata:
    """Test metadati."""
    
    def test_metadata_added(self, mock_conditioning):
        controller = CharacterForgeEthnicityController()
        result = controller.apply_ethnicity_control(mock_conditioning, "caucasian", 0.6)
        
        conditioning, _ = result
        cond_tensor, cond_dict = conditioning[0]
        
        assert "characterforge_ethnicity" in cond_dict
        assert cond_dict["characterforge_ethnicity"]["primary"] == "caucasian"
    
    def test_mixed_metadata(self, mock_conditioning):
        controller = CharacterForgeEthnicityController()
        result = controller.apply_ethnicity_control(
            mock_conditioning, "caucasian", 0.7, "asian"
        )
        
        conditioning, _ = result
        cond_tensor, cond_dict = conditioning[0]
        
        assert cond_dict["characterforge_ethnicity"]["is_mixed"] == True