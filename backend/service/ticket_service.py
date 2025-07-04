from models.ticket import Ticket
from datetime import datetime
from repo.gate_repo import GateRepo
from repo.vehicle_repo import VehicleRepo

class TicketService:
    def __init__(self, GateRepo, VehicleRepo):
        self.GateRepo = GateRepo
        self.VehicleRepo = VehicleRepo

    def issueTicket(self, vehicle_number, owner_name, gate_id, vehicle_type) -> Ticket:

        # create a ticket
        ticket = Ticket(id=-1, ticket_number='', entry_time=datetime.now(), vehicle=None,
                        parking_slot=None, generated_gate=None)
        # set info like gate no
        gate = self.GateRepo.find_gate_by_id(gate_id)

        if gate is None:
            raise Exception('Gate not found')
        
        ticket.generated_gate = gate

        #vehicle info
        vehicle = self.VehicleRepo.find_vehicle_by_number(vehicle_number)
        if vehicle is None:
            raise Exception('vehicle not found ')
        # find a slot
        # update slot
        # update parking counters
        # return ticket