from unittest.mock import create_autospec

import pytest

from bun import Bun
from burger import Burger
from ingredient import Ingredient


class TestBurger:
    def test_set_buns_sets_selected_bun(self):
        burger = Burger()
        bun = create_autospec(Bun, instance=True)

        burger.set_buns(bun)

        assert burger.bun is bun

    def test_add_ingredient_adds_ingredient_to_end(self):
        burger = Burger()
        first_ingredient = create_autospec(Ingredient, instance=True)
        added_ingredient = create_autospec(Ingredient, instance=True)
        burger.ingredients = [first_ingredient]

        burger.add_ingredient(added_ingredient)

        assert burger.ingredients == [first_ingredient, added_ingredient]

    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        ingredients = [
            create_autospec(Ingredient, instance=True) for _ in range(3)
        ]
        burger.ingredients = ingredients.copy()

        burger.remove_ingredient(1)

        assert burger.ingredients == [ingredients[0], ingredients[2]]

    @pytest.mark.parametrize(
        'index, new_index, expected_order',
        [
            (0, 2, [1, 2, 0]),
            (2, 0, [2, 0, 1]),
            (1, 1, [0, 1, 2]),
        ],
    )
    def test_move_ingredient_changes_ingredient_order(
        self, index, new_index, expected_order
    ):
        burger = Burger()
        ingredients = [
            create_autospec(Ingredient, instance=True) for _ in range(3)
        ]
        burger.ingredients = ingredients.copy()

        burger.move_ingredient(index, new_index)

        assert burger.ingredients == [ingredients[i] for i in expected_order]

    def test_get_price_returns_double_bun_price_plus_ingredient_prices(self):
        burger = Burger()
        bun = create_autospec(Bun, instance=True)
        bun.get_price.return_value = 100
        first_ingredient = create_autospec(Ingredient, instance=True)
        first_ingredient.get_price.return_value = 50.5
        second_ingredient = create_autospec(Ingredient, instance=True)
        second_ingredient.get_price.return_value = 300
        burger.set_buns(bun)
        burger.ingredients = [first_ingredient, second_ingredient]

        actual_price = burger.get_price()

        bun.get_price.assert_called_once_with()
        first_ingredient.get_price.assert_called_once_with()
        second_ingredient.get_price.assert_called_once_with()
        assert actual_price == 550.5

    def test_get_receipt_returns_formatted_burger_receipt(self):
        burger = Burger()
        bun = create_autospec(Bun, instance=True)
        bun.get_name.return_value = 'sesame bun'
        bun.get_price.return_value = 100
        sauce = create_autospec(Ingredient, instance=True)
        sauce.get_type.return_value = 'SAUCE'
        sauce.get_name.return_value = 'hot sauce'
        sauce.get_price.return_value = 50
        filling = create_autospec(Ingredient, instance=True)
        filling.get_type.return_value = 'FILLING'
        filling.get_name.return_value = 'cutlet'
        filling.get_price.return_value = 300
        burger.set_buns(bun)
        burger.ingredients = [sauce, filling]
        expected_receipt = (
            '(==== sesame bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== sesame bun ====)\n\n'
            'Price: 550'
        )

        actual_receipt = burger.get_receipt()

        assert actual_receipt == expected_receipt
