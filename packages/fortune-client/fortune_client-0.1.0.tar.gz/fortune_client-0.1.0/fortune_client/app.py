import argparse

from simple_value_object import ValueObject, invariant
from .arguments import parse_args
from .parameters import Parameters, sources
from .get_data import get_data
from .output import text_format


DEFAULT_API_URL = 'https://api.fortune.luka.sh'


def main():
    args = parse_args(url=DEFAULT_API_URL)

    parameters = Parameters(args.url, args.explore, args.recursive, args.path, args.index)

    if args.verbose:
        print(parameters)

    for output in get_data(parameters):
        text_format(output, args.headers, args.no_directories, args.decode_off_fortunes, args.json)


if __name__ == '__main__':
    main()


