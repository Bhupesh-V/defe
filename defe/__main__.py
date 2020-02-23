"""
Main CLI
"""

import sys
from feeders import feeder
from . formatter import defy


def print_help():
    print(
        """
A News feed Aggregator for Developers.

Usage:
------

Specify Number of feed story output

    $ defe <integer-value>

Show random feed

    $ defe .

Available options are:

    -h, --help         Show help text


Contact:
--------

- 📧 varshneybhupesh@gmail.com

More information is available at:

- Home : https://pypi.org/project/defe/
- Source : https://github.com/Bhupesh-V/defe
- Documentation : https://defe.readthedocs.io/en/latest/

"""
    )


def print_error():
    print(
        """
Wrong Command 😤, use defe --help for usage

"""
    )


def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == ".":
            for item in feeder.all_feed()[:7]:
                defy(item["title"], item["link"])
        elif sys.argv[1] in ("--help", "-h"):
            print_help()
        else:
            feed_count = int(sys.argv[1])
            for item in feeder.all_feed()[:feed_count]:
                defy(item["title"], item["link"])
        return


if __name__ == "__main__":
    main()
