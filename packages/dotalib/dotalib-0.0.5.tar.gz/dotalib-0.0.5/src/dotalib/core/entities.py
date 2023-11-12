from dataclasses import dataclass, field
from contextlib import suppress
from dotalib.utils import simplify


@dataclass(slots=True)
class Hero:
    id: int
    codename: str
    fullname: str
    shortname: str = field(default=None, init=False)

    def __post_init__(self):
        self.shortname = simplify(self.fullname)

    # Simple API to get all attrs
    def as_tuple(self):
        return (
            self.id,
            self.codename,
            self.fullname,
            self.shortname,
        )

    def __iter__(self):
        return iter(self.as_tuple())
    

class HeroTuple(tuple):
    """
    Tuple of heroes that acts as python tuples
    """
    def __init__(self, heroes: tuple[Hero]) -> None:
        super().__init__()
        # Init custom tuples of heroes
        self._init_tuples()
    
    def __add__(self, value):
        # return HeroTuple(super().__add__(value))
        return HeroTuple(super().__add__(value))

    def _init_tuples(self):
        # Create init lists
        ids = []
        codenames = []
        fullnames = []
        shortnames = []
        # Enumerate each hero to take it attrs
        for hero in self:
            id, codename, fullname, shortname = hero.as_tuple()
            ids.append(id)
            codenames.append(codename)
            fullnames.append(fullname)
            shortnames.append(shortname)
        # Init attr as tuples to reach frozen effect
        self.ids = tuple(ids)
        self.codenames = tuple(codenames)
        self.fullnames = tuple(fullnames)
        self.shortnames = tuple(shortnames)

    # Source point to get hero in field by value
    def _find_hero_in(self, field, by_value):
        with suppress(ValueError):
            index = field.index(by_value)
            return self[index]
        return None

    # Find Hero object in field by it name and value
    def findhero_in(self, field_name, by_value) -> Hero:
        field = getattr(self, field_name)
        return self._find_hero_in(field, by_value)

    # Find Hero object in all fields by any value
    def findhero(self, by_value) -> Hero:
        for field_name in vars(self):
            hero = self.findhero_in(field_name, by_value)
            if hero is not None:
                return hero
        raise ValueError("Can't find hero by {!r}".format(by_value))


@dataclass(slots=True, kw_only=True)
class Team:
    heroes: HeroTuple
    name: str = None
    shortname: str = field(default=None, init=False)

    def __post_init__(self):
        self.shortname = self.name and simplify(self.name)


@dataclass(slots=True, kw_only=True)
class Match:
    radiant: Team
    dire: Team
    is_radiant_winner: bool = field(default=None)
    champname: str = field(default=None)
    shortname: str = field(default=None, init=False)
    winner: Team = field(default=None, init=False)
    loser: Team = field(default=None, init=False)
    heroes: HeroTuple = field(default=None, init=False)

    def __post_init__(self):
        winner, loser = self._determine_winner_and_loser()
        self.winner = winner
        self.loser = loser
        self.heroes = self.radiant.heroes + self.dire.heroes
        self.shortname = self.champname and simplify(self.champname)

    def _determine_winner_and_loser(self):
        if self.is_radiant_winner is True:
            return self.radiant, self.dire
        if self.is_radiant_winner is False:
            return self.dire, self.radiant
        return None, None
