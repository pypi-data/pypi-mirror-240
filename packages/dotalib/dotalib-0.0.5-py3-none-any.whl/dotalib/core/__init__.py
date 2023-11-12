from .entities import (
    Hero,
    HeroTuple,
    Team,
    Match,
)
from dotalib.data.heroes import all_heroes_json

__all__ = (
    "Team",
    "Match",
    "findhero",
    "findhero_in",
    "hero_tuple",
)

# Collect all heroes from json
all_heroes_list = [
    Hero(*hero.values())
    for hero in all_heroes_json
]

# All Dota heroes
all_heroes = HeroTuple(all_heroes_list)

# Prebound API
findhero_in = all_heroes.findhero_in
findhero = all_heroes.findhero

# Shortcut for creating HeroTuple from any values
def hero_tuple(values):
    return HeroTuple(findhero(value) for value in values)