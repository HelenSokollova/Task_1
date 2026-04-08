import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import data


class TestBurger:
    def test_set_buns_with_new_bun(self, burger):
        bun = Bun(data.BUN_NAME_NEW, data.BUN_PRICE_NEW)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_set_buns_with_replace_old_bun(self, burger):
        bun_old = Bun(data.BUN_NAME_OLD, data.BUN_PRICE_OLD)
        bun_new = Bun(data.BUN_NAME_NEW, data.BUN_PRICE_NEW)
        burger.set_buns(bun_old)
        burger.set_buns(bun_new)
        assert burger.bun == bun_new

    @pytest.mark.parametrize('ingredient_data', data.INGREDIENT_ONE)   
    def test_add_ingredient_one(self, burger, ingredient_data):
        ingredient = Ingredient(*ingredient_data)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    @pytest.mark.parametrize('ingredient_data_1, ingredient_data_2', data.INGREDIENT_MANY)   
    def test_add_ingredient_many(self, burger, ingredient_data_1, ingredient_data_2):
        ingredient_1 = Ingredient(*ingredient_data_1)
        ingredient_2 = Ingredient(*ingredient_data_2)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient_1
        assert burger.ingredients[1] == ingredient_2

    def test_remove_ingredient(self, burger):
        ingredient = Ingredient(*data.INGREDIENT_1)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_middle(self, burger_and_ingredients):
        burger, ingredients = burger_and_ingredients
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredients[0]
        assert burger.ingredients[1] == ingredients[2]

    def test_move_ingredient_to_start_of_list(self, burger_and_ingredients):
        burger, ingredients = burger_and_ingredients
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredients[1]
        assert burger.ingredients[1] == ingredients[0]
        assert burger.ingredients[2] == ingredients[2]

    def test_move_ingredient_to_finish_of_list(self, burger_and_ingredients):
        burger, ingredients = burger_and_ingredients
        burger.move_ingredient(1, 2)
        assert burger.ingredients[0] == ingredients[0]
        assert burger.ingredients[1] == ingredients[2]
        assert burger.ingredients[2] == ingredients[1]

    def test_move_ingredient_to_his_position(self, burger_and_ingredients):
        burger, ingredients = burger_and_ingredients
        burger.move_ingredient(1, 1)
        assert burger.ingredients[0] == ingredients[0]
        assert burger.ingredients[1] == ingredients[1]
        assert burger.ingredients[2] == ingredients[2]


    def test_get_price_of_burger(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == data.PRICE

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_receipt = data.RECEIPT
        assert burger.get_receipt() == expected_receipt
