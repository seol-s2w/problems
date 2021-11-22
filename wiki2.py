import re
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

VISITED_PAGES = set()
PATH_MAP = dict()


def get_subpages(page):
    res = requests.get("http://en.wikipedia.org{}".format(page))
    bs = BeautifulSoup(res.text, "html.parser")

    subpages = set()
    for link in bs.findAll("a", href=re.compile("^(/wiki/X)")):
        if "href" in link.attrs:
            subpage = link.attrs["href"].split("#")[0]
            if "(" not in subpage and subpage not in VISITED_PAGES:
                subpages.add(subpage)
                PATH_MAP[subpage] = page

    return subpages


def print_page_counts_by_distance(start_page, max_distance):
    start = time.time()
    print("d=0 1")

    page_sets = [{start_page}]
    for distance in range(max_distance):
        curr_pages = page_sets[distance]
        VISITED_PAGES.update(curr_pages)

        with ThreadPoolExecutor(max_workers=32) as executor:
            results = executor.map(get_subpages, curr_pages)

        page_sets.append(set())
        for result in results:
            page_sets[-1].update(result)

        print(f"d={distance + 1} {len(page_sets[-1])}")

    end = time.time()
    print("elapsed time: %.3f sec" % (end - start))

    return page_sets


def print_shortest_path(page):
    path = []
    while PATH_MAP.get(page) is not None:
        path.append(page)
        page = PATH_MAP[page]
    print("path:", " -> ".join(list(reversed(path))))


if __name__ == "__main__":
    print_page_counts_by_distance("/wiki/X", 3)
    print_shortest_path("/wiki/Xbox_360")
