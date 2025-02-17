from .base import BaseModel

class User(BaseModel):
    def __init__(self, id, username, email):
        super().__init__(id)
        self.username = username
        self.email = email
