import pytest
from praktikum.bun import Bun
import data

class TestBun:
    @pytest.mark.parametrize('input_name, expected_name', data.NAMES)
    def test_get_name_of_bun_with_different_values(self, input_name, expected_name):
        bun = Bun(input_name, data.BUN_TEST_PRICE)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize('input_price, expected_price', data.PRICES)
    def test_get_price_of_bun_with_different_values(self, input_price, expected_price):
        bun = Bun(data.BUN_TEST_NAME, input_price)
        assert bun.get_price() == expected_price
