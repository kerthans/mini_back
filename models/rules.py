from .base import BaseModel

class Rules(BaseModel):
    def __init__(self, id, title, content):
        super().__init__(id)
        self.title = title
        self.content = content
