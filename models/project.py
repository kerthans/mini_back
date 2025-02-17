from .base import BaseModel

class Project(BaseModel):
    def __init__(self, id, name, description):
        super().__init__(id)
        self.name = name
        self.description = description
