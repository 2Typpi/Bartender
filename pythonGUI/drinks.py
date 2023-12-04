from enum import IntEnum


class Ingredient(IntEnum):
    VODKA = 17
    RUM = 18
    TEQUILA = 27
    GRENADINE = 22
    SUGAR_SYRUP = 23
    CRANBERRY_NECTAR = 24
    ORANGE_JUICE = 25
    LIME_JUICE = 9


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
    },
    "refuel": {
        "pour_time": 40,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.GRENADINE,
            "pour_time": 10
        }, {
            "wait_before_pour": 0,
            "name": Ingredient.RUM,
            "pour_time": 10
        }, {
            "wait_before_pour": 10,
            "name": Ingredient.LIME_JUICE,
            "pour_time": 10
        }, {
            "wait_before_pour": 10,
            "name": Ingredient.ORANGE_JUICE,
            "pour_time": 10
        }, {
            "wait_before_pour": 20,
            "name": Ingredient.SUGAR_SYRUP,
            "pour_time": 10
        }, {
            "wait_before_pour": 20,
            "name": Ingredient.CRANBERRY_NECTAR,
            "pour_time": 10
        }, {
            "wait_before_pour": 30,
            "name": Ingredient.TEQUILA,
            "pour_time": 10
        }, {
            "wait_before_pour": 30,
            "name": Ingredient.VODKA,
            "pour_time": 10
        }
        ]
    },
    "mop": {
        "pour_time": 120,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.GRENADINE,
            "pour_time": 30
        }, {
            "wait_before_pour": 0,
            "name": Ingredient.RUM,
            "pour_time": 30
        }, {
            "wait_before_pour": 30,
            "name": Ingredient.LIME_JUICE,
            "pour_time": 30
        }, {
            "wait_before_pour": 30,
            "name": Ingredient.ORANGE_JUICE,
            "pour_time": 30
        }, {
            "wait_before_pour": 60,
            "name": Ingredient.SUGAR_SYRUP,
            "pour_time": 30
        }, {
            "wait_before_pour": 60,
            "name": Ingredient.CRANBERRY_NECTAR,
            "pour_time": 30
        }, {
            "wait_before_pour": 90,
            "name": Ingredient.TEQUILA,
            "pour_time": 30
        }, {
            "wait_before_pour": 90,
            "name": Ingredient.VODKA,
            "pour_time": 30
        }
        ]
    },
    "vodka": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.VODKA,
            "pour_time": 15
        }
        ]
    },
    "rum": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.RUM,
            "pour_time": 15
        }
        ]
    },
    "tequila": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.TEQUILA,
            "pour_time": 15
        }
        ]
    },
    "cranberry": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.CRANBERRY_NECTAR,
            "pour_time": 15
        }
        ]
    },
    "grenadine": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.GRENADINE,
            "pour_time": 15
        }
        ]
    },
    "lime": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.LIME_JUICE,
            "pour_time": 15
        }
        ]
    },
    "orange": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.ORANGE_JUICE,
            "pour_time": 15
        }
        ]
    },
    "sugar": {
        "pour_time": 15,
        "ingredients": [{
            "wait_before_pour": 0,
            "name": Ingredient.SUGAR_SYRUP,
            "pour_time": 15
        }
        ]
    },
}
