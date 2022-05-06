import sys

if len(sys.argv) <=2:
    sys.exit("Usage: extract_vocab.py <input_filename> <output_filename> but we got "+str(sys.argv))

with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'w+') as of:
    for e in set(f.read().split()):
        of.write(e + '\n')