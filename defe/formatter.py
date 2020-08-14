"""
Custom Formatter for defe
"""
from colorama import Fore, Style, init
import webbrowser
import sys


def defy(src, title, link, summary):
    init(autoreset=True)
    print(Style.BRIGHT + src, end="\n")
    print(Fore.YELLOW + Style.BRIGHT + title, end=" ")
    print(Fore.BLUE + Style.BRIGHT + link, end="\n\n")
    print(" ".join(summary))
    print()
    print()


def defy_prompt(feed):
    init(autoreset=True)
    while 1:
        try:
            if len(feed) == 0:
                print(
                    Style.BRIGHT + "\nOh no!!, Looks like you are offline 🌏", end="\n\n"
                )
                sys.exit()
            else:
                feed_to_open = str(
                    input(Fore.GREEN + Style.BRIGHT + "Enter Feed Index to open : ")
                )
                print(Style.RESET_ALL)
                print(Style.BRIGHT + "Opening Link in your default browser ...")
                webbrowser.open(feed[int(feed_to_open) - 1].link)
        except ValueError:
            print(Style.BRIGHT + "Enter Valid Index 😟")
        except KeyboardInterrupt:
            # Oh no!, come back again :(
            sys.exit()
