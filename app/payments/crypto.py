from app.payments.common.payment_method import PaymentMethod
from app.utils.logger import logger


class CryptoPayment(PaymentMethod):
    def process_payment(self):
        self.random_exception()
        logger.info("Crypto payment success")
