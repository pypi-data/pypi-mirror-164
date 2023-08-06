import argparse
import sys

from .ranker import Ranker, SameTeam


def start():
    try:
        games = get_input()
        league = Ranker(games)
        table = league.process_data()
        sys.stdout.write(table)
    except SameTeam:
        sys.stdout.write("One or more teams are playing against themselves (That's not possible). Check your input and try again.")
        sys.exit(1)
    except Exception:
        sys.exit(1)


def get_input(path: str='') -> list[str]:
    """
    Takes the program arguments and input from stdin.

    This function gets the optional argument provided 
    by the user, which is a path to a file. Additionally,
    the path can also be provided as a parameter in the
    function. If no path is provided the function scans
    stdin for input.
    
    After the path is provided or the user inputs
    an empty string or a new line, it processes the 
    file / stind data and returns a list of strings, 
    every string being a line from the file / stdin.

    Parameters
    ----------
    path : str
        Path to a file.

    Returns
    -------
    data : list [str]
        [line1, line2, ...]
    
    Returns a list of strings.
    """
    parser = argparse.ArgumentParser(prog='ranking',
                                        usage='%(prog)s [file_path]',
                                        description='Creates a ranking table from games results',
                                        epilog='Enjoy the program! :)')
    parser.version = '0.0.1'
    parser.add_argument('infile', 
                        nargs='?', 
                        type=argparse.FileType('r'), 
                        default=sys.stdin,
                        help='optional path to file containing game scores')
    args = parser.parse_args()


    # Get stdin / file data
    if path:
        try:
            with open(path, 'r') as f : return f.read().splitlines()
        except(FileNotFoundError, IOError):
            sys.stdout.write("Wrong file path")
            sys.exit(1)
    elif args.infile.name != '<stdin>':
        return args.infile.read().splitlines()

    data = []
    for line in sys.stdin:
        # Stop reading if it finds an empty line or new line character
        if line in ['', '\n']:
            break

        data.append(line.strip())

    return data
