"""
Custom Foramatter for skotty
"""
from colorama import Fore, Style, init
import webbrowser
import sys


def defy(title, link, feeder=None):
    init(autoreset=True)
    if feeder is not None:
        print(Fore.YELLOW + Style.BRIGHT + title, end=" ")
        print(Fore.GREEN + Style.BRIGHT + feeder, end="\n")
    else:
        print(Fore.YELLOW + Style.BRIGHT + title, end="\n")
    print(Fore.BLUE + Style.BRIGHT + link, end="\n\n")


def defy_prompt(feed):
    init(autoreset=True)
    try:
        while 1:
            feed_to_open = str(
                input(Fore.GREEN + Style.BRIGHT + "Enter Feed ID to open : "))
            print(Style.BRIGHT + "Opening Link in your default browser ...")
            webbrowser.open(feed[int(feed_to_open) - 1].link)
    except ValueError:
        pass
        # add code to reiterate input prompt
    except KeyboardInterrupt:
        sys.exit()
