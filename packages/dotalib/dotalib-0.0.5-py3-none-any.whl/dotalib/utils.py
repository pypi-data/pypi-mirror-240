import re


def simplify(s):
    return re.sub(r"\W", "", s.lower())