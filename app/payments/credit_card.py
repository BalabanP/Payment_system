from app.payments.common.payment_method import PaymentMethod
from app.utils.logger import logger


class CreditCardPayment(PaymentMethod):
    def process_payment(self):
        self.random_exception()
        logger.info("Credit Card payment success")
