import argparse
import sys
def check():
    print("status")
    return 0
parser = argparse.ArgumentParser(prog="sub", add_help=False)
subparser = parser.add_subparsers(dest="cmd")
subparser.add_parser('status', help='show status')
subparser.add_parser('list', help='print list')
# hack to show help when no arguments supplied
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)
args = parser.parse_args()
if args.cmd == 'list':
    print('list')
elif args.cmd == 'status':
    sys.exit(check())