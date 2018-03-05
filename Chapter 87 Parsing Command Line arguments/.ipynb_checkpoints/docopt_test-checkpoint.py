"""
Usage:
    docopt_test.py [-a] [-b] <path>
    
Options:
    -a  Print all the things.
    -b  Get more bees into the path.
"""
from docopt import docopt
if __name__ == "__main__":
    args = docopt(__doc__)
    import pprint; pprint.pprint(args)