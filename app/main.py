from app.payments.crypto import CryptoPayment
from app.payments.paypal import PayPalPayment
from app.payments.credit_card import CreditCardPayment
from enums import PaymentTypes
from app.utils.logger import logger
from app.services.payment_service import PaymentService


def app():
    # Simulate user selecting a payment method
    payment_method = input("Select a payment method (creditcard, paypal, crypto): ").lower()
    payment_mapping = {
        PaymentTypes.crypto.value: CryptoPayment,
        PaymentTypes.paypal.value: PayPalPayment,
        PaymentTypes.creditcard.value: CreditCardPayment,
    }
    method = payment_mapping.get(payment_method)
    if not method:
        logger.error("Invalid payment method selected")
        return
    payment_method = method()
    # Create the PaymentService instance
    service = PaymentService(payment_method)
    # Execute the payment
    service.execute_payment()


if __name__ == "__main__":
    app()
