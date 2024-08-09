from app.payments.common.payment_method import PaymentMethod
from app.exceptions.payment_exception import PaymentException
from app.utils.logger import logger


class PaymentService:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def execute_payment(self):
        try:
            self.payment_method.process_payment()
        except PaymentException as payment_error:
            logger.error(payment_error)
        except Exception as e:
            logger.error(f"Payment failed: {e}")
