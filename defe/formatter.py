"""
Custom Formatter for defe
"""
from colorama import Fore, Style, init
import webbrowser
import sys


def defy(src, title, link):
    init(autoreset=True)
    print(Style.BRIGHT + src, end="\n")
    print(Fore.YELLOW + Style.BRIGHT + title, end=" ")
    print(Fore.BLUE + Style.BRIGHT + link, end="\n\n")


def defy_prompt(feed, feed_type, max_feed_count):
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
                if "REFRESH" not in feed_to_open:
                    print(Style.BRIGHT + "Opening Link in your default browser ...")
                    webbrowser.open(feed[int(feed_to_open) - 1].link)
                else:
                    print(chr(27) + "[2J")  # clear the output
                    feed = set_feed(feed_type, max_feed_count, True)
        except ValueError:
            print(Style.BRIGHT + "Enter Valid Index 😟")
        except KeyboardInterrupt:
            # Oh no!, come back again :(
            sys.exit()


from defe.__main__ import set_feed
