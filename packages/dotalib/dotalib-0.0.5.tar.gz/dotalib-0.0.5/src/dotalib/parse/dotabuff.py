from .base import BaseMatchParser
from dotalib.core import *
from bs4 import BeautifulSoup


class DotabuffParser(BaseMatchParser):
    """
    Not thread-safe in each new thread create new class instead using prebound functions
    """
    def parse_match(self, content: str) -> Match:
        soup = BeautifulSoup(content, "html.parser")
        self.soup = soup
        radiant_heroes, dire_heroes = self._find_heroes()
        radiant_name, dire_name = self._find_teams_names()
        is_radiant_winner = self._check_radiant_is_winner()
        champname = self._find_championship()
        radiant_team = Team(heroes=radiant_heroes, name=radiant_name)
        dire_team = Team(heroes=dire_heroes, name=dire_name)
        match = Match(
            radiant=radiant_team,
            dire=dire_team,
            is_radiant_winner=is_radiant_winner,
            champname=champname,
        )
        return match
    
    def _find_heroes(self):
        images = self.soup.find_all('img', class_='image-hero image-icon image-overlay')
        hero_names = [img['title'] for img in images]
        heroes = hero_tuple(hero_names)
        radiant_heroes, dire_heroes = heroes[:5], heroes[5:]
        return radiant_heroes, dire_heroes
    
    def _find_teams_names(self):
        div = self.soup.find('div', class_='team-results')
        if div is None:
            return None, None
        radiant_section = div.find('section', class_='radiant')
        dire_section = div.find('section', class_='dire')

        radiant_team = radiant_section.find('span', class_='team-text team-text-full')
        dire_team = dire_section.find('span', class_='team-text team-text-full')

        radiant_team_name = radiant_team.text if radiant_team else None
        dire_team_name = dire_team.text if dire_team else None
        return radiant_team_name, dire_team_name
    
    def _check_radiant_is_winner(self):
        radiant_winner_element = self.soup.find('div', class_='match-result team radiant')
        is_radiant_winner = radiant_winner_element is not None
        return is_radiant_winner
    
    def _find_championship(self):
        champ = self.soup.find('a', class_='esports-link')
        champ_name = champ.text if champ else None
        return champ_name


_dotabuff_parser = DotabuffParser()
parse_match = _dotabuff_parser.parse_match