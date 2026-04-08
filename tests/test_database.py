import pytest
import data

class TestDatabase:

    @pytest.mark.parametrize("index, expected_name, expected_price", data.DATABASE_BUNS)
    def test_available_buns_details(self, database, index, expected_name, expected_price):
        buns = database.available_buns()   
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    @pytest.mark.parametrize("index, expected_type, expected_name, expected_price", data.DATABASE_INGREDIENTS)
    def test_available_ingredients_details(self, database, index, expected_type, expected_name, expected_price):
        ingredients = database.available_ingredients()
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name
        assert ingredients[index].get_price() == expected_price
