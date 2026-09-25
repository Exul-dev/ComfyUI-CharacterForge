from __future__ import annotations
from typing import Any
from .anatomy_component import AnatomyComponent

class Back(AnatomyComponent):
    component_type="back"

    VALID_SHAPES=("straight","defined","athletic","rounded")

    def __init__(self,*,width:float=31.0,length:float=45.0,muscularity:float=0.5,shape:str="straight"):
        super().__init__()
        self.width=float(width)
        self.length=float(length)
        self.muscularity=float(muscularity)
        self.shape=shape
        self.validate()

    def validate(self):
        super().validate()
        if self.width<=0: raise ValueError("Back width must be greater than zero.")
        if self.length<=0: raise ValueError("Back length must be greater than zero.")
        if not 0<=self.muscularity<=1:
            raise ValueError("Back muscularity must be between 0 and 1.")
        if self.shape not in self.VALID_SHAPES:
            raise ValueError(f"Invalid back shape: {self.shape!r}")

    def to_dict(self)->dict[str,Any]:
        return {**super().to_dict(),"width":self.width,"length":self.length,"muscularity":self.muscularity,"shape":self.shape}
