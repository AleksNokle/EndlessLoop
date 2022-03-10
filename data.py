#Default minimum stats are a total of 80 - cannot NATURALLY below the initial lowest
#20 points in total is distributed as padding that the player can freely relocate.
#Default total stats will therefore be 100
#Max in one single stat is 100

BASE_CLASS = {
    "Knight": {
        "MIN_STATS": {
            "Constitution": 16,
            "Endurance": 12,
            "Strength": 12,
            "Dexterity": 4,
            "Intelligence": 6,
            "Wisdom": 8,
            "Faith": 10,
            "Charisma": 12
            },
        "DEFAULT_STATS": {
            "Constitution": 20,
            "Endurance": 14,
            "Strength": 14,
            "Dexterity": 8,
            "Intelligence": 7,
            "Wisdom": 10,
            "Faith": 12,
            "Charisma": 15
        }
    },
    "Fighter": {
        "MIN_STATS": {
            "Constitution": 13,
            "Endurance": 10,
            "Strength": 18,
            "Dexterity": 8,
            "Intelligence": 8,
            "Wisdom": 6,
            "Faith": 7,
            "Charisma": 10
        },
        "DEFAULT_STATS": {
            "Constitution": 15,
            "Endurance": 12,
            "Strength": 24,
            "Dexterity": 10,
            "Intelligence": 10,
            "Wisdom": 8,
            "Faith": 9,
            "Charisma": 12
        }
    }



}

EVOLVED_CLASS = {
    "Dragon Knight": {},
    "Gladiator": {},
}

ELITE_CLASS = {
    "Death Knight": {},
    "Necromancer": {}
}