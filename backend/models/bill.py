from base_model import BaseModel
from enums import *
from datetime import datetime
from ticket import Ticket
from gate import Gate
from typing import List


class Bill(BaseModel):
    def __init__(self, id: str, exit_time: datetime, token: Ticket, exited_at: Gate,
                 payments: List, total_amount: int, bill_status: BillStatus):
        super().__init__(id)
        self.exit_time = exit_time
        self.token = token
        self.exited_at = exited_at
        self.payments = payments
        self.total_amount = total_amount
        self.bill_status = bill_status