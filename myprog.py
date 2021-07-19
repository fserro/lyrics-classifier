import sys
print(sys.argv)

import argparse

parser = argparse.ArgumentParser(description='my first program')

parser.add_argument("message", help="displays the string you use here")
parser.add_argument("-s", "--square", help="display the square of a given number", type=int, default=7)

parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")



print(args.message)
print(args.square ** 2)
