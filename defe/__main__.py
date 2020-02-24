"""
Main CLI
"""

import sys
from feeders import feeder
from .formatter import defy
from colorama import Back, Fore, Style, init
import argparse


contact = """

Feed Type
---------

1. general  [defe general <max_feed_count>]
2. news     [defe news <max_feed_count>]
3. podcasts [defe podcasts <max_feed_count>]

Contact:
--------

- 📧 varshneybhupesh@gmail.com

More information is available at:

- Home : https://pypi.org/project/defe/
- Source : https://github.com/Bhupesh-V/devfeed

"""


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
    parser = argparse.ArgumentParser(
        prog='defe',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='A News feed aggregator for developers',
        epilog=contact
        )
    parser.add_argument("feed", type=str, help="Category of feed")
    parser.add_argument("max_feed_count", nargs='?', type=int, default=7, help="No of feed items to show")

    if len(sys.argv) == 1:
        home()
        sys.exit(1)

    args = parser.parse_args()

    if args.feed == "general":
        for item in feeder.all_feed()[:args.max_feed_count]:
            defy(item["title"], item["link"])
    if args.feed == "news":
        for item in feeder.news_feed()[:args.max_feed_count]:
            defy(item["title"], item["link"])
    if args.feed == "podcasts":
        for item in feeder.podcasts_feeds()[:args.max_feed_count]:
            defy(item["title"], item.links[1].href)
    else:
        home()


if __name__ == "__main__":
    main()
