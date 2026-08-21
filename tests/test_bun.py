import pytest

from bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        'name, price',
        [
            ('black bun', 100),
            ('white bun', 200.5),
            ('red bun', 0),
        ],
    )
    def test_getters_return_values_passed_to_constructor(self, name, price):
        bun = Bun(name, price)

        assert (bun.get_name(), bun.get_price()) == (name, price)
