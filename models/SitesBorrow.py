from .base import BaseModel

class SitesBorrow(BaseModel):
    def __init__(self, id, site_name, borrow_date):
        super().__init__(id)
        self.site_name = site_name
        self.borrow_date = borrow_date
