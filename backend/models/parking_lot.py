from base_model import BaseModel
from floor import Floor
from gate import Gate
from enums import *
from typing import List


class parkingLot(BaseModel):
    def __init__(self, id: int, name: str, address: str, parking_floors: List[Floor], 
                 gates: List[Gate], allowed_vehicles: List[VehicleType], capacity: int, 
                 status: ParkingLotStatus, slot_assignment_strategy: SlotAssignmentStrategyEnum):
        
        super().__init__(id)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.status = status
        self.slot_assignment_strategy = slot_assignment_strategy
