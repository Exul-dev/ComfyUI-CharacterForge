"""
Fixtures condivise per test CharacterForge.
"""

import pytest
import torch


@pytest.fixture
def mock_conditioning():
    """
    Crea un conditioning mock valido per i test.
    
    Returns:
        list: Conditioning nel formato ComfyUI [tensor, metadata_dict]
    """
    # Crea tensor conditioning simulato
    cond_tensor = torch.randn(1, 77, 768)  # Formato tipico CLIP
    
    # Crea metadata dict
    cond_dict = {
        "pooled_output": torch.randn(1, 768),
        "clip_weights": None
    }
    
    return [[cond_tensor, cond_dict]]


@pytest.fixture
def mock_conditioning_batch():
    """
    Crea un batch di conditioning mock (3 elementi).
    """
    batch = []
    for _ in range(3):
        cond_tensor = torch.randn(1, 77, 768)
        cond_dict = {"pooled_output": torch.randn(1, 768)}
        batch.append([cond_tensor, cond_dict])
    
    return batch


@pytest.fixture
def mock_latent():
    """
    Crea un latent mock nel formato ComfyUI.
    """
    return {"samples": torch.randn(1, 4, 128, 256)}


@pytest.fixture
def mock_latent_tensor():
    """
    Crea un latent mock come tensor puro.
    """
    return torch.randn(1, 4, 128, 256)


@pytest.fixture
def mock_image():
    """
    Crea un'immagine mock.
    """
    return torch.rand(1, 512, 512, 3)


@pytest.fixture
def invalid_conditioning():
    """
    Conditioning invalido per test errori.
    """
    return None


@pytest.fixture
def empty_conditioning():
    """
    Conditioning vuoto per test errori.
    """
    return []