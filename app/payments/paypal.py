from app.payments.common.payment_method import PaymentMethod
from app.utils.logger import logger


class PayPalPayment(PaymentMethod):
    def process_payment(self):
        self.random_exception()
        logger.info("PayPal payment success")
