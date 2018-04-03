import sys
if len(sys.argv) != 4: # The script name needs to be accounted for as well.
    raise RuntimeError("expected 3 command line arguments")
f = open(sys.argv[1], 'rb') # Use first command line argument.
start_line = int(sys.argv[2]) # All arguments come as strings, so need to be
end_line = int(sys.argv[3]) # converted explicitly if other types are required.
print(f.readlines(start_line))
print(f.readlines(end_line))