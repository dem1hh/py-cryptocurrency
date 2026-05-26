from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_buy(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 120

    assert cryptocurrency_action(100) == "Buy more cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_sell(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 80

    assert cryptocurrency_action(100) == "Sell all your cryptocurrency"


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_do_nothing(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 101

    assert cryptocurrency_action(100) == "Do nothing"
