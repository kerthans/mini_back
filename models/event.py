from .base import BaseModel

class Event(BaseModel):
    def __init__(self, id, name, date):
        super().__init__(id)
        self.name = name
        self.date = date
