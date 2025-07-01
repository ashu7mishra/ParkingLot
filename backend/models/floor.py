from base_model import BaseModel
from enums import *
from typing import List


class Floor(BaseModel):
    def __init__(self, id: str, slots: List[Slot], floor_number: int, 
                 vehicle_Type: VehicleType, floor_status: FloorStatus):
        
        super().__init__(id)