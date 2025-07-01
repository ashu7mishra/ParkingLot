from base_model import BaseModel
from enums import *
from typing import List
from floor import Floor


class Slot(BaseModel):
    def __init__(self, id: int, slot_number: int, vehicle_type: VehicleType, 
                 parking_slot_status: SlotStatus, parking_floor: Floor):
        super().__init__(id)
        self.vehicle_type = vehicle_type
        self.parking_slot_status = parking_slot_status
        self.slot_number = slot_number
        self.parking_floor = parking_floor