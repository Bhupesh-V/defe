"""
Custom Formatter for defe
"""
from colorama import Fore, Style, init
import webbrowser
import sys
import vlc  ##


def defy(src, title, link):
    init(autoreset=True)
    print(Style.BRIGHT + src, end="\n")
    print(Fore.YELLOW + Style.BRIGHT + title, end=" ")
    print(Fore.BLUE + Style.BRIGHT + link, end="\n\n")


def defy_prompt(feed, podcasts=False):
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
                if podcasts:
                    player = vlc.MediaPlayer(
                        feed[int(feed_to_open) - 1]["links"][0]["href"]
                    )
                    print(
                        Fore.GREEN
                        + Style.BRIGHT
                        + "Now playing: "
                        + Fore.YELLOW
                        + Style.BRIGHT
                        + feed[int(feed_to_open) - 1]["title"]
                    )
                    player.play()
                    while 1:
                        action = str(
                            input(Fore.GREEN + Style.BRIGHT + "pause/stop [p/s] : ")
                        ).lower()
                        if action == "p":
                            player.pause()
                            input(
                                Fore.GREEN + Style.BRIGHT + "Press enter to continue : "
                            )
                            player.play()
                        elif action == "s":
                            player.stop()
                            break
                        else:
                            print(
                                Style.BRIGHT
                                + "Please type 'p' to pause or 's' to stop the podcast"
                            )
                else:
                    print(Style.BRIGHT + "Opening Link in your default browser ...")
                    webbrowser.open(feed[int(feed_to_open) - 1].link)
        except ValueError:
            print(Style.BRIGHT + "Enter Valid Index 😟")
        except KeyboardInterrupt:
            # Oh no!, come back again :(
            sys.exit()
