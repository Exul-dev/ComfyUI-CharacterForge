"""
Test per CharacterForgeBodyController.
"""

import pytest
import torch
from nodes.body_controller import CharacterForgeBodyController


class TestBodyControllerInit:
    """Test inizializzazione controller."""
    
    def test_controller_exists(self):
        assert CharacterForgeBodyController is not None
    
    def test_input_types_structure(self):
        input_types = CharacterForgeBodyController.INPUT_TYPES()
        
        assert "required" in input_types
        assert "conditioning" in input_types["required"]
        assert "body_type" in input_types["required"]
        assert "height" in input_types["required"]
        assert "weight" in input_types["required"]
        assert "muscle_definition" in input_types["required"]
        assert "body_fat" in input_types["required"]
    
    def test_body_type_options(self):
        input_types = CharacterForgeBodyController.INPUT_TYPES()
        body_types = input_types["required"]["body_type"][0]
        
        assert "athletic" in body_types
        assert "slim" in body_types
        assert "curvy" in body_types
        assert "muscular" in body_types
        assert "average" in body_types
    
    def test_return_types(self):
        assert CharacterForgeBodyController.RETURN_TYPES == ("CONDITIONING", "STRING")
    
    def test_category(self):
        assert CharacterForgeBodyController.CATEGORY == "CharacterForge/Basic"


class TestBodyControllerValidation:
    """Test validazione input."""
    
    def test_invalid_conditioning(self, invalid_conditioning):
        controller = CharacterForgeBodyController()
        
        with pytest.raises(ValueError):
            controller.apply_body_control(
                invalid_conditioning, "athletic", 175.0, 0.7, "medium", "medium"
            )
    
    def test_invalid_body_type(self, mock_conditioning):
        controller = CharacterForgeBodyController()
        
        with pytest.raises(ValueError, match="non riconosciuto"):
            controller.apply_body_control(
                mock_conditioning, "invalid_type", 175.0, 0.7, "medium", "medium"
            )
    
    def test_invalid_muscle_definition(self, mock_conditioning):
        controller = CharacterForgeBodyController()
        
        with pytest.raises(ValueError):
            controller.apply_body_control(
                mock_conditioning, "athletic", 175.0, 0.7, "invalid_muscle", "medium"
            )


class TestBodyControllerExecution:
    """Test esecuzione controller."""
    
    @pytest.fixture
    def controller(self):
        return CharacterForgeBodyController()
    
    @pytest.mark.parametrize("body_type", [
        "athletic", "slim", "curvy", "muscular", "average"
    ])
    def test_all_body_types_execution(self, controller, mock_conditioning, body_type):
        result = controller.apply_body_control(
            mock_conditioning, body_type, 175.0, 0.7, "medium", "medium"
        )
        
        assert result is not None
        conditioning, details = result
        assert conditioning is not None
    
    @pytest.mark.parametrize("height", [150.0, 175.0, 200.0])
    def test_height_range_execution(self, controller, mock_conditioning, height):
        result = controller.apply_body_control(
            mock_conditioning, "average", height, 0.7, "medium", "medium"
        )
        
        assert result is not None
    
    @pytest.mark.parametrize("muscle_def", ["low", "medium", "high"])
    def test_muscle_definitions_execution(self, controller, mock_conditioning, muscle_def):
        result = controller.apply_body_control(
            mock_conditioning, "athletic", 175.0, 0.7, muscle_def, "medium"
        )
        
        assert result is not None
    
    def test_custom_proportions_execution(self, controller, mock_conditioning):
        result = controller.apply_body_control(
            mock_conditioning, "slim", 178.0, 0.6, "low", "medium",
            custom_proportions="extra long legs"
        )
        
        assert result is not None
    
    def test_target_gender_execution(self, controller, mock_conditioning):
        result = controller.apply_body_control(
            mock_conditioning, "athletic", 175.0, 0.7, "medium", "medium",
            target_gender="male"
        )
        
        assert result is not None


class TestBodyControllerDatabase:
    """Test database corporatura."""
    
    def test_database_exists(self):
        assert hasattr(CharacterForgeBodyController, 'BODY_DATABASE')
        assert len(CharacterForgeBodyController.BODY_DATABASE) == 5
    
    @pytest.mark.parametrize("body_type", [
        "athletic", "slim", "curvy", "muscular", "average"
    ])
    def test_database_structure(self, body_type):
        db = CharacterForgeBodyController.BODY_DATABASE
        assert body_type in db
        
        entry = db[body_type]
        assert "description" in entry
        assert "proportions" in entry
        assert "height_range" in entry
    
    def test_height_categorization(self):
        controller = CharacterForgeBodyController()
        
        assert controller._categorize_height(155) == "short"
        assert controller._categorize_height(165) == "medium-short"
        assert controller._categorize_height(175) == "medium"
        assert controller._categorize_height(185) == "tall"
        assert controller._categorize_height(195) == "very tall"


class TestBodyControllerMetadata:
    """Test metadati."""
    
    def test_metadata_added(self, mock_conditioning):
        controller = CharacterForgeBodyController()
        result = controller.apply_body_control(
            mock_conditioning, "athletic", 180.0, 0.8, "high", "low"
        )
        
        conditioning, _ = result
        cond_tensor, cond_dict = conditioning[0]
        
        assert "characterforge_body" in cond_dict
        assert cond_dict["characterforge_body"]["type"] == "athletic"
        assert cond_dict["characterforge_body"]["height_cm"] == 180.0