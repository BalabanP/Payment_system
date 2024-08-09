class PaymentException(Exception):
    def __init__(self, message) -> None:
        super().__init__(f"PAYMENT_ERROR: {message}")
