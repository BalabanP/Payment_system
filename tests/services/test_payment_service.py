from app.payments.credit_card import CreditCardPayment
import pytest
from logging import INFO
from app.services.payment_service import PaymentService
from app.exceptions.payment_exception import PaymentException


@pytest.fixture(scope="function")
def payment_service(mocker):
    payment_method = mocker.MagicMock()
    return PaymentService(payment_method)


def test_execute_payment(payment_service):
    payment_service.payment_method.process_payment.return_value = None
    payment_service.execute_payment()
    payment_service.payment_method.process_payment.assert_called_once_with()


def test_execute_payment_exception(payment_service, caplog):
    payment_service.payment_method.process_payment.side_effect = PaymentException("message")
    caplog.set_level(INFO, logger="payment-system")
    payment_service.execute_payment()
    assert caplog.messages == ['PAYMENT_ERROR: message']
    payment_service.payment_method.process_payment.assert_called_once_with()
