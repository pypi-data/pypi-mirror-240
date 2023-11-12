from .base import BaseMatchParser
from dotalib.core import *
from dotalib.utils import simplify
from html import unescape
import re

team_pattern = re.compile(r'itemProp="name">.+?</span')
hero_pattern = re.compile(r'</b>\n(.+?)\n</div>"><div class="image-wrapper')
winner_pattern = re.compile(r'Силы.+?<.+?loss')
championship_pattern = re.compile(r'"name_alternative":".+?"')


class CyberscoreParser(BaseMatchParser): 
    """
    Not thread-safe in each new thread create new class instead using prebound functions
    """
    def parse_match(self, content: str) -> Match:
        self.content = unescape(content)
        radiant_heroes, dire_heroes = self._find_heroes()
        radiant_heroes = hero_tuple(radiant_heroes)
        dire_heroes = hero_tuple(dire_heroes)
        radiant_name, dire_name = self._find_teams_names()
        is_radiant_won = self._is_radiant_won()
        champname = self._find_championship()
        radiant_team = Team(heroes=radiant_heroes, name=radiant_name)
        dire_team = Team(heroes=dire_heroes, name=dire_name)
        match = Match(
            radiant=radiant_team,
            dire=dire_team,
            is_radiant_winner=is_radiant_won,
            champname=champname,
        )
        return match

    def _find_heroes(self):
        hero_matches = hero_pattern.findall(self.content)[:10]
        heroes = [
            simplify(hero.split('(')[-1].split(')')[0]) 
            for hero in hero_matches
        ]
        radiant_heroes, dire_heroes = heroes[:5], heroes[5:]
        return radiant_heroes, dire_heroes
    
    def _find_teams_names(self):
        team_matches = team_pattern.findall(self.content)
        tm = team_matches[-1]
        title = tm[tm.find(">") + 1:tm.rfind("<")]
        teams_names = title.split(' vs ')
        radiant_name = teams_names[0]
        dire_name = teams_names[1][:-2]
        return radiant_name, dire_name
    
    def _is_radiant_won(self):
        winner_matches = winner_pattern.findall(self.content)
        if not winner_matches:
            return None
        winner_match = winner_matches[0].split("<")[0]
        return "Силы тьмы" in winner_match
    
    def _find_championship(self):
        champ_matches = championship_pattern.findall(self.content)
        champ_name = champ_matches[0].split('"')[-2] if champ_matches else None 
        return champ_name


_cyberscore_parser = CyberscoreParser()
parse_match = _cyberscore_parser.parse_match