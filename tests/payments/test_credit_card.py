from app.payments.credit_card import CreditCardPayment
import pytest
from logging import INFO


@pytest.fixture(scope="function")
def credit_card_payment():
    return CreditCardPayment()


def test_process_payment(credit_card_payment, caplog, mocker):
    caplog.set_level(INFO, logger="payment-system")
    mock_payment= mocker.patch.object(credit_card_payment, "random_exception", return_value=None)
    result = credit_card_payment.process_payment()
    assert result is None
    mock_payment.assert_called_once_with()
    assert caplog.messages == ['Credit Card payment success']
