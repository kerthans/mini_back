from .base import BaseModel

class Printer3D(BaseModel):
    def __init__(self, id, model, status):
        super().__init__(id)
        self.model = model
        self.status = status
