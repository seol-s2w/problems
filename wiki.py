import re
from concurrent import futures

import requests
from bs4 import BeautifulSoup

START_PAGE = "/wiki/X"
MAX_WORKERS = 32
PAGE_MAP = dict()


def get_links(url, visited):
    res = requests.get(
        "http://en.wikipedia.org{}".format(url),
        proxies={"http": "http://10.0.40.81:8118", "https": "http://10.0.40.81:8118"},
    )
    bs = BeautifulSoup(res.text, "html.parser")

    pages = set()
    for link in bs.findAll("a", href=re.compile("^(/wiki/X)")):
        if "href" in link.attrs:
            newpage = link.attrs["href"].split("#")[0]
            if "(" not in newpage and newpage not in visited:
                pages.add(newpage)
    return pages


def get_all_links(top_level_link, max_level) -> dict:
    level_to_links = {0: {top_level_link}}

    prev_level_links = set()
    for level in range(max_level):
        curr_level_links = level_to_links[level]
        prev_level_links.update(curr_level_links)

        next_level_links = set()
        for link in curr_level_links:
            next_level_links.update(get_links(link, prev_level_links))

        level_to_links[level + 1] = next_level_links

    return level_to_links


def get_all_links_with_multithread(top_level_link, max_level) -> dict:
    level_to_links = {0: {top_level_link}}

    prev_level_links = set()
    for level in range(max_level):
        curr_level_links = level_to_links[level]
        print(f"d={level} {len(curr_level_links)}")

        prev_level_links.update(curr_level_links)
        max_workers = min(MAX_WORKERS, len(curr_level_links))
        fn = lambda x: get_links(x, prev_level_links)
        with futures.ThreadPoolExecutor(max_workers) as executor:
            results = executor.map(fn, curr_level_links)

        next_level_links = set()
        for result in results:
            next_level_links.update(result)

        level_to_links[level + 1] = next_level_links

    return level_to_links


def get_shortest_paths(page, level_to_nodes: dict):
    shortest_paths = []
    for nodes in level_to_nodes.values():
        for node in nodes:
            if node.data == page:
                wooddogi = node
                stack = []
                while wooddogi is not None:
                    stack.append(wooddogi.data)
                    wooddogi = wooddogi.prev

                while stack:
                    shortest_paths.append(stack.pop())

                return shortest_paths


if __name__ == "__main__":
    max_level = 3
    all_links = get_all_links_with_multithread(START_PAGE, max_level)
    print(get_shortest_paths("/wiki/X", all_links))
