from praktikum.ingredient_types import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

NAMES = [("название", "название"), (" blabla ", " blabla "), ("500", "500"), ("", ""), ("!№;%", "!№;%")]

PRICES = [(125.50, 125.50), (500, 500), (-1000, -1000), (0, 0)]

INGREDIENTS = [(INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE), (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING), ("sauce", "sauce"), (" filling ", " filling "), ("", ""), ("!№;%", "!№;%")]

BUN_NAME_NEW = "булочка новая"

BUN_PRICE_NEW = 100.00

BUN_NAME_OLD = "булочка старенькая"

BUN_PRICE_OLD = 50.00

INGREDIENT_ONE = [(INGREDIENT_TYPE_SAUCE, "соус", 10.00), (INGREDIENT_TYPE_FILLING, "начинка", 50.00)]

INGREDIENT_MANY = [((INGREDIENT_TYPE_SAUCE, "соус", 10.00), (INGREDIENT_TYPE_SAUCE, "соус", 10.00)), ((INGREDIENT_TYPE_FILLING, "начинка", 50.00), (INGREDIENT_TYPE_FILLING, "начинка", 50.00)), ((INGREDIENT_TYPE_SAUCE, "соус", 10.00), (INGREDIENT_TYPE_FILLING, "начинка", 50.00))]

INGREDIENT_1 = (INGREDIENT_TYPE_SAUCE, "соус", 10.00)

INGREDIENT_2 = (INGREDIENT_TYPE_FILLING, "начинка", 50.00)

INGREDIENT_3 = (INGREDIENT_TYPE_SAUCE, "кетчуп", 30.00)

PRICE = 130.50

RECEIPT = (
        "(==== Булочка ====)\n"
        "= sauce соус =\n"
        "(==== Булочка ====)\n\n"
        "Price: 130.5"
        )

DATABASE_BUNS = [
    (0, "black bun", 100),
    (1, "white bun", 200),
    (2, "red bun", 300)
    ]

DATABASE_INGREDIENTS = [
    (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (5, INGREDIENT_TYPE_FILLING, "sausage", 300)
    ]

BUN_TEST_PRICE = 50.50

BUN_TEST_NAME = "булочка"

INGREDIENT_TEST_NAME = "ингредиент"

INGREDIENT_TEST_PRICE = 50.50

INGREDIENT_TEST_TYPE = "SAUCE"
