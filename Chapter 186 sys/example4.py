import sys
def main():
    if len(sys.argv) != 4 or '--help' in sys.argv[1:]:
        print('usage: my_program <arg1> <arg2> <arg3>', file=sys.stderr)
        sys.exit(1) # use an exit code to signal the program was unsuccessful
    process_data()
    
main()