"""defe CLI."""

import argparse
import sys

from colorama import Fore, Style, init

from . import __version__
from .formatter import defy, defy_prompt

try:
    from defe.core import feedcore
except ImportError:
    from core import feedcore


contact = """

Available Feed Categories
-------------------------

1. general      [defe general <max_feed_count>]
2. news         [defe news <max_feed_count>]
3. podcasts     [defe podcasts <max_feed_count>]
4. newsletters  [defe newsletters <max_feed_count>]

* By Default defe shows only [7] feed items
* Use [defe feeders] to list available feeders

Contact:
--------

- 📧 varshneybhupesh@gmail.com

More information is available at:

- Home      : https://pypi.org/project/defe/
- Source    : https://github.com/Bhupesh-V/defe
- Support   : https://www.patreon.com/bePatron?u=18082750,
"""


def home():
    init(autoreset=True)
    print(
        Fore.RED
        + Style.BRIGHT
        + """
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
    print(
        Fore.GREEN
        + Style.BRIGHT
        + "A Tech feed Aggregator for Developers & Tech Enthusiasts",
        end="\n",
    )
    print(Fore.LIGHTBLUE_EX + "> ", end="")
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "Tutorials, News, Podcasts & Newsletters all at one place",
        end="\n\n",
    )
    print(Style.BRIGHT + "Welcome to defe 👋", end="\n")
    print("Use" + Style.BRIGHT + " defe --help ", end="")
    print("to see available commands", end="\n\n")


def main():
    init(autoreset=True)
    parser = argparse.ArgumentParser(
        prog="defe",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="A Tech feed Aggregator for Developers & Tech Enthusiasts",
        epilog=contact,
    )
    parser.add_argument(
        "-v", "--version", action="version", version="%(prog)s {0}".format(__version__)
    )
    parser.add_argument("feed", type=str, help="Feed Category")
    parser.add_argument(
        "max_feed_count",
        nargs="?",
        type=int,
        default=7,
        help="No of feed items to show",
    )

    if len(sys.argv) == 1:
        home()
        sys.exit(1)

    args = parser.parse_args()

    if args.feed == "general":
        data = feedcore.all_feed()
        for item in data[: args.max_feed_count]:
            print(Fore.RED + Style.BRIGHT + str(data.index(item) + 1), end=". ")
            defy(item["feed_src"], item["title"], item["link"])
        defy_prompt(data)

    if args.feed == "news":
        data = feedcore.news_feed()
        for item in data[: args.max_feed_count]:
            print(Fore.RED + Style.BRIGHT + str(data.index(item) + 1), end=". ")
            defy(item["feed_src"], item["title"], item["link"])
        defy_prompt(data)
    if args.feed == "newsletters":
        data = feedcore.newsletters_feeds()
        for item in data[: args.max_feed_count]:
            print(Fore.RED + Style.BRIGHT + str(data.index(item) + 1), end=". ")
            defy(item["feed_src"], item["title"], item["link"])
        defy_prompt(data)
    if args.feed == "podcasts":
        data = feedcore.podcasts_feeds()
        for item in data[: args.max_feed_count]:
            print(Fore.RED + Style.BRIGHT + str(data.index(item) + 1), end=". ")
            if item:
                defy(item["feed_src"], item["title"], item["link"])
            else:
                pass
        defy_prompt(data, podcasts=True)
    if args.feed == "feeders":
        feeds = ["general", "news", "podcasts", "newsletters"]
        print(
            Style.BRIGHT + "\ndefe fetches feeds of these sources 😃",
            end="\n\n",
        )
        for f in feeds:
            print("\n" + Fore.BLUE + Style.BRIGHT + f.capitalize(), end=" ")
            print(Style.BRIGHT + "[defe " + f.lower() + "]", end="\n\n")
            data = feedcore.read_data(f)
            for item in data:
                print(Style.BRIGHT + str(data.index(item) + 1), end=". ")
                print(Fore.GREEN + Style.BRIGHT + item["name"])

        print("\n\n" + Style.BRIGHT + "Want to add more ? 🤔")
        print(
            Style.BRIGHT + "Open a PR at https://github.com/Bhupesh-V/defe",
            end="\n\n",
        )


if __name__ == "__main__":
    main()
