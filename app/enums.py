from enum import Enum


class PaymentTypes(Enum):
    creditcard = "creditcard"
    paypal = "paypal"
    crypto = "crypto"
