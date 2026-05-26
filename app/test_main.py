from unittest import mock
from unittest.mock import MagicMock
from app.main import cryptocurrency_action


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_buy(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 120
    expected = "Buy more cryptocurrency"
    result = cryptocurrency_action(100)

    assert result == expected


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_sell(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 80
    expected = "Sell more cryptocurrency"
    result = cryptocurrency_action(100)

    assert result == expected


@mock.patch("app.main.get_exchange_rate_prediction")
def test_get_exchange_rate_prediction_to_do_nothing(
        mock_exchange: MagicMock
) -> None:
    mock_exchange.return_value = 101
    expected = "Do nothing"
    result = cryptocurrency_action(100)

    assert result == expected
