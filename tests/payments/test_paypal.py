from app.payments.paypal import PayPalPayment
import pytest
from logging import INFO


@pytest.fixture(scope="function")
def paypal_payment():
    return PayPalPayment()


def test_process_payment(paypal_payment, caplog, mocker):
    caplog.set_level(INFO, logger="payment-system")
    mock_payment= mocker.patch.object(paypal_payment, "random_exception", return_value=None)
    result = paypal_payment.process_payment()
    assert result is None
    mock_payment.assert_called_once_with()
    assert caplog.messages == ['PayPal payment success']
