import os
import argparse

if __name__ == "__main__":
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument('--x', type=int, default=0, help='Enter value of X')
    # Read arguments from command line
    args = parser.parse_args()
    print(args.x)
