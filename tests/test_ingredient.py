import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:
    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 200.5),
        ],
    )
    def test_getters_return_values_passed_to_constructor(
        self, ingredient_type, name, price
    ):
        ingredient = Ingredient(ingredient_type, name, price)

        assert (
            ingredient.get_type(),
            ingredient.get_name(),
            ingredient.get_price(),
        ) == (ingredient_type, name, price)
