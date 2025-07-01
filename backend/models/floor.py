from base_model import BaseModel
from enums import *
from typing import List


class Floor(BaseModel):
    def __init__(self, id: str, parking_slot_list: List, floor_number: int, 
                 floor_status: FloorStatus, allowed_vehicles: List[VehicleType]):
        
        super().__init__(id)
        self.parking_slot_list = parking_slot_list
        self.floor_number = floor_number
        self.allowed_vehicles = allowed_vehicles
        self.floor_status = floor_status