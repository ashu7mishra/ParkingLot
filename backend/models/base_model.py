from datetime import datetime
from typing import List

class BaseModel:
    def __init__(self, id: int):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
