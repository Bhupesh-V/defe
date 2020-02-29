"""
Custom Foramatter for skotty
"""
from colorama import Fore, Style, init


def defy(title, link, feeder=None):
    init(autoreset=True)
    if feeder is not None:
        print(Fore.YELLOW + Style.BRIGHT + title, end=" ")
        print(Fore.GREEN + Style.BRIGHT + feeder, end="\n")
    else:
        print(Fore.YELLOW + Style.BRIGHT + title, end="\n")
    print(Fore.BLUE + Style.BRIGHT + link, end="\n\n")
