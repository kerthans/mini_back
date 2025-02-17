from .base import BaseModel

class Games(BaseModel):
    def __init__(self, id, game_name, participants):
        super().__init__(id)
        self.game_name = game_name
        self.participants = participants
