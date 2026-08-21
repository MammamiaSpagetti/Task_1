from database import Database


class TestDatabase:
    def test_available_buns_returns_created_buns(self):
        database = Database()

        available_buns = database.available_buns()
        actual_buns = [(bun.get_name(), bun.get_price()) for bun in available_buns]

        assert available_buns is database.buns
        assert actual_buns == [
            ('black bun', 100),
            ('white bun', 200),
            ('red bun', 300),
        ]

    def test_available_ingredients_returns_created_ingredients(self):
        database = Database()

        available_ingredients = database.available_ingredients()
        actual_ingredients = [
            (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
            for ingredient in available_ingredients
        ]

        assert available_ingredients is database.ingredients
        assert actual_ingredients == [
            ('SAUCE', 'hot sauce', 100),
            ('SAUCE', 'sour cream', 200),
            ('SAUCE', 'chili sauce', 300),
            ('FILLING', 'cutlet', 100),
            ('FILLING', 'dinosaur', 200),
            ('FILLING', 'sausage', 300),
        ]
