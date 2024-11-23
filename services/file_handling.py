import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int: str] = {}


def _get_part_text(text, start, lenght):
    minLen = min(start+lenght+1, len(text))
    if minLen == len(text):
        return (text[start:], len(text[start:]))
    text = text[start:minLen]
    while text[-1] in '.,?!:;':
        text = text[:-1]
    while not text[-1] in '.,?!:;':
        text = text[:-1]
    return (text, len(text))


def prepare_book(path: str) -> None:
    file = open(path, 'r', encoding='utf-8')
    counter = 0
    number_key = 1
    full_text = file.read()
    while counter < len(full_text) - 1:
        page = _get_part_text(full_text, counter, PAGE_SIZE)
        book[number_key] = page[0].lstrip()
        counter += page[1]
        number_key += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
