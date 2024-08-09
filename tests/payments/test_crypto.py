from app.payments.crypto import CryptoPayment
import pytest
from logging import INFO


@pytest.fixture(scope="function")
def crypto_payment():
    return CryptoPayment()


def test_process_payment(crypto_payment, caplog, mocker):
    caplog.set_level(INFO, logger="payment-system")
    mock_payment= mocker.patch.object(crypto_payment, "random_exception", return_value=None)
    result = crypto_payment.process_payment()
    assert result is None
    mock_payment.assert_called_once_with()
    assert caplog.messages == ['Crypto payment success']
