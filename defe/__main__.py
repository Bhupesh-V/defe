"""
Main CLI
"""

import sys
from feeders import feeder
from .formatter import defy
from colorama import Back, Fore, Style, init


def print_help():
    print(
        """
A News feed Aggregator for Developers.

Usage:
------

Show General feed

    $ defe feed

Show Podcasts feed

    $ defe podcasts

Show News feed

    $ defe news

Available options are:

    -h, --help         Show this text


Contact:
--------

- 📧 varshneybhupesh@gmail.com

More information is available at:

- Home : https://pypi.org/project/defe/
- Source : https://github.com/Bhupesh-V/devfeed

"""
    )


def print_error():
    print(
        """
Wrong Command 😤, use defe --help for usage

"""
    )


def home():
    init(autoreset=True)
    print(
        """
     888           .d888
     888          d88P"
     888          888
 .d88888  .d88b.  888888 .d88b.
d88" 888 d8P  Y8b 888   d8P  Y8b
888  888 88888888 888   88888888
Y88b 888 Y8b.     888   Y8b.
 "Y88888  "Y8888  888    "Y8888

"""
        )
    print(Fore.GREEN + Style.BRIGHT + "A News feed Aggregator for Developers.", end="\n\n")
    print(Style.BRIGHT + "Welcome to defe 👋", end="\n")
    print("Use", end="")
    print(Style.BRIGHT + " defe --help ", end="")
    print("to see available commands", end="\n\n")


def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "feed":
            for item in feeder.all_feed()[:7]:
                defy(item["title"], item["link"])
        elif sys.argv[1] == "news":
            for item in feeder.news_feed()[:7]:
                defy(item["title"], item["link"])
        elif sys.argv[1] == "podcasts":
            for item in feeder.podcasts_feeds()[:7]:
                defy(item["title"], item.links[1].href)
        elif sys.argv[1] in ("--help", "-h"):
            print_help()
        else:
            feed_count = int(sys.argv[1])
            for item in feeder.all_feed()[:feed_count]:
                defy(item["title"], item["link"])
        return
    else:
        home()


if __name__ == "__main__":
    main()
