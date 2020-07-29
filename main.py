import yaml
import sys
import argparse
import requests
from bs4 import BeautifulSoup


def _begin_crawl(url, steps):
    print(steps)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
    for step in steps:
        print(soup.findAll(step["element"]))


def _get_arguments(sys_args):
    parser = argparse.ArgumentParser(
        description="Crawling website with yaml configs."
    )

    parser.add_argument(
        "--config",
        required=True,
    )

    return parser.parse_args(sys_args)


def cmd_line_entry():
    args = _get_arguments(sys.argv[1:])
    print("Running with args: ", args)
    with open(args.config) as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
        _begin_crawl(config["url"], config["steps"])


if __name__ == "__main__":
    cmd_line_entry()
