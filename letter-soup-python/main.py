
import click
import time

from v1 import return_valid_words as v1
from v2 import return_valid_words as v2
from v3 import return_valid_words as v3


letter_map4 = [
    ['M', 'A', 'S', 'C'],
    ['O', 'M', 'D', 'B'],
    ['G', 'Y', 'I', 'R'],
    ['O', 'W', 'R', 'E'],
]

letter_map3 = [
    ['M', 'A', 'B'],
    ['O', 'M', 'C'],
    ['O', 'M', 'C'],
]
words_list = ['MOM', "MO", "AMDBR", "MAS"]


@click.group(chain=True)
def cli():
    pass


@cli.command('v1', short_help='hello')
def run_viewsync_prod():
    print("hey")
    start = time.time()
    valid = v1(letter_map4, words_list)
    print(valid)
    end = time.time()
    print(end - start)


@cli.command('v2', short_help='hello')
def run_viewsync_prod():

    start = time.time()
    valid = v2(letter_map4, words_list)
    print(valid)
    end = time.time()
    print(end - start)


@cli.command('v3', short_help='hello')
def run_viewsync_prod():

    start = time.time()
    valid = v3(letter_map3, words_list)
    print(valid)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    cli()
