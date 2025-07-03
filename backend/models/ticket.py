from base_model import BaseModel
from datetime import datetime
from gate import Gate
from slot import Slot
from vehicle import Vehicle


class Ticket(BaseModel):
    def __init__(self, id: str, ticket_number: int, entry_time: datetime, vehicle: Vehicle,
                 parking_slot: Slot, generated_gate: Gate, ):
        super().__init__(id)
        self.ticket_number = ticket_number
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.parking_slot = parking_slot
        self.generated_gate = generated_gate
