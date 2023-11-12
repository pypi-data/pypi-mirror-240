import argparse


def parse_args(url: str) -> argparse.Namespace:

    arg_parser = argparse.ArgumentParser(description='Fortune Api client')

    arg_parser.add_argument('-u', 
                            '--url', 
                            type=str, 
                            default=url, 
                            help='Api url (default: {})'.format(url)
                            )

    arg_parser.add_argument('-e',
                            '--explore',
                            action='store_true',
                            )

    arg_parser.add_argument('-r',
                            '--recursive',
                            action='store_true',
                            )

    arg_parser.add_argument('-i',
                            '--index',
                            default=None,
                            )

    arg_parser.add_argument('path',
                            type=str,
                            nargs='*',
                            default=None,
                            help='Path'
                            )
    arg_parser.add_argument('-v',
                            '--verbose',
                            action='store_true',
                            )
    arg_parser.add_argument('-H',
                            '--headers',
                            action='store_true',
                            )

    arg_parser.add_argument('--no-directories',
                            action='store_false',
                            )
    arg_parser.add_argument('-d',
                            '--decode-off-fortunes',
                            action='store_true',
                            )
    arg_parser.add_argument('-j',
                            '--json',
                            action='store_true',
                            )

    return arg_parser.parse_args()
