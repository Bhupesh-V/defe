"""
Custom Foramatter for skotty
"""
from colorama import Back, Fore, Style, init


def defy(title, link):
    init(autoreset=True)
    print(Fore.YELLOW + Style.BRIGHT + title, end="\n")
    print(Fore.BLUE + Style.BRIGHT + link, end="\n\n")
