from .base import BaseModel

class Task(BaseModel):
    def __init__(self, id, title, description):
        super().__init__(id)
        self.title = title
        self.description = description
