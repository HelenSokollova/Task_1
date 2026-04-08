import pytest
from praktikum.ingredient import Ingredient
import data

class TestIngredient:
    @pytest.mark.parametrize('input_ingredient, expected_ingredient', data.INGREDIENTS)
    def test_get_ingredient_of_ingredient_with_different_values(self, input_ingredient, expected_ingredient):
        ingredient = Ingredient(input_ingredient, data.INGREDIENT_TEST_NAME, data.INGREDIENT_TEST_PRICE)
        assert ingredient.get_type() == expected_ingredient

    @pytest.mark.parametrize('input_name, expected_name', data.NAMES)
    def test_get_name_of_ingredient_with_different_values(self, input_name, expected_name):
        ingredient = Ingredient(data.INGREDIENT_TEST_TYPE, input_name, data.INGREDIENT_TEST_PRICE)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize('input_price, expected_price', data.PRICES)
    def test_get_price_of_ingredient_with_different_values(self, input_price, expected_price):
        ingredient = Ingredient(data.INGREDIENT_TEST_TYPE, data.INGREDIENT_TEST_NAME, input_price)
        assert ingredient.get_price() == expected_price
