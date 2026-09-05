"""
ComfyUI-CharacterForge Test Package
==================================

Setup per esecuzione test unitari con pytest.

Esecuzione:
    pytest tests/ -v

Esecuzione con coverage:
    pytest tests/ --cov=nodes --cov-report=html
"""

import os
import sys

# Aggiunge path per importazioni
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

__version__ = "2.0.0"