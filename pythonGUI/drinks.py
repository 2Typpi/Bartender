from enum import IntEnum


class Ingredient(IntEnum):
    VODKA = 0
    RUM = 1
    TEQUILA = 17
    GRENADINE = 3
    SUGAR_SYRUP = 4
    CRANBERRY_NECTAR = 5
    ORANGE_JUICE = 6
    LIME_JUICE = 7


drinks = {
    "tequila_sunrise": {
        "pour_time": 77,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.TEQUILA,
            "pour_time": 34
        }, {
            "wait_before_pour": 0,
            "name": Ingredient.ORANGE_JUICE,
            "pour_time": 68
        }, {
            "wait_before_pour": 40,
            "name": Ingredient.GRENADINE,
            "pour_time": 37
        }]
    },
}
