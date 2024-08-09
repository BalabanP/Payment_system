from abc import ABC, abstractmethod
import random
from app.exceptions.payment_exception import PaymentException


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self):
        ...

    def random_exception(self):
        if random.choice([True, False]):
            raise PaymentException(f"An error occurred with {self.__class__.__name__}!")
