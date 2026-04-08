import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
import data
from unittest.mock import Mock

@pytest.fixture(scope='function')
def burger():
    new_burger = Burger()
    return new_burger

@pytest.fixture(scope='function')
def burger_and_ingredients(burger):
    ingredients = [
        Ingredient(*data.INGREDIENT_1),
        Ingredient(*data.INGREDIENT_2),
        Ingredient(*data.INGREDIENT_3)
    ]
    for ing in ingredients:
        burger.add_ingredient(ing)
    return burger, ingredients

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Булочка'
    mock_bun.get_price.return_value = 50.00
    return mock_bun

@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = 'sauce'
    mock_ingredient.get_name.return_value = 'соус'
    mock_ingredient.get_price.return_value = 30.50
    return mock_ingredient

@pytest.fixture(scope='function')
def database():
    new_database = Database()
    return new_database
