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
            }
        ]
    },
    "sex_on_the_beach": {
        "pour_time": 85,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.VODKA,
                "pour_time": 30
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.ORANGE_JUICE,
                "pour_time": 45
            }, {
                "wait_before_pour": 40,
                "name": Ingredient.CRANBERRY_NECTAR,
                "pour_time": 45
            }
        ]
    },
    "screwdriver": {
        "pour_time": 90,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.VODKA,
                "pour_time": 30
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.ORANGE_JUICE,
                "pour_time": 90
            }
        ]
    },
    "cosmopolitan": {
        "pour_time": 30,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.VODKA,
                "pour_time": 30
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.LIME_JUICE,
                "pour_time": 15
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.CRANBERRY_NECTAR,
                "pour_time": 15
            }, {
                "wait_before_pour": 15,
                "name": Ingredient.GRENADINE,
                "pour_time": 8
            }
        ]
    },
    "rum_sour": {
        "pour_time": 38,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.RUM,
                "pour_time": 38
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.LIME_JUICE,
                "pour_time": 15
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.SUGAR_SYRUP,
                "pour_time": 8
            }
        ]
    },
    "mai_tai": {
        "pour_time": 45,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.RUM,
                "pour_time": 45
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.LIME_JUICE,
                "pour_time": 23
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.SUGAR_SYRUP,
                "pour_time": 8
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.GRENADINE,
                "pour_time": 8
            }
        ]
    },
    "daiquiri": {
        "pour_time": 45,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.RUM,
                "pour_time": 45
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.LIME_JUICE,
                "pour_time": 23
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.SUGAR_SYRUP,
                "pour_time": 12
            }
        ]
    },
    "hurricane": {
        "pour_time": 105,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.GRENADINE,
                "pour_time": 15
            }, {
                "wait_before_pour": 15,
                "name": Ingredient.RUM,
                "pour_time": 90
            }, {
                "wait_before_pour": 15,
                "name": Ingredient.LIME_JUICE,
                "pour_time": 23
            }, {
                "wait_before_pour": 15,
                "name": Ingredient.ORANGE_JUICE,
                "pour_time": 23
            }, {
                "wait_before_pour": 15,
                "name": Ingredient.SUGAR_SYRUP,
                "pour_time": 12
            }
        ]
    },
    "mojito": {
        "pour_time": 56,
        "ingredients": [{
                "wait_before_pour": 0,
                "name": Ingredient.SUGAR_SYRUP,
                "pour_time": 15
            }, {
                "wait_before_pour": 0,
                "name": Ingredient.LIME_JUICE,
                "pour_time": 18
            }, {
                "wait_before_pour": 18,
                "name": Ingredient.RUM,
                "pour_time": 38
            }
        ]
    }
}

