from base_model import BaseModel
from enums import *


class Vehicle(BaseModel):
    def __init__(self, id: str, vehicle_number: str, vehicle_type: VehicleType, owner_name: str):
        super().__init__(id)
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.owner_name = owner_name
