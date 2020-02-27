"""
Custom Foramatter for skotty
"""
from colorama import Fore, Style, init


def defy(title, link, feeder):
    init(autoreset=True)
    print(Fore.YELLOW + Style.BRIGHT + title, end=" ")
    print(Fore.GREEN + Style.BRIGHT + feeder, end="\n")
    print(Fore.BLUE + Style.BRIGHT + link, end="\n\n")
