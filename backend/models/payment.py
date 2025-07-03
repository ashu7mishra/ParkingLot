from base_model import BaseModel
from enums import *
from datetime import datetime
from bill import Bill


class Payment(BaseModel):
    def __init__(self, id: str, amount: float, payment_mode: PaymentMode, ref_id: str, 
                 bill: Bill, status: PaymentStatus, paid_at: datetime):
        super().__init__(id)
        self.bill = bill
        self.amount = amount
        self.payment_mode = payment_mode
        self.paid_at = paid_at
        self.status = status
        self.ref_id = ref_id
