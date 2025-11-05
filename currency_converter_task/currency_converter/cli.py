"""
This should handle command line arguments
"""

import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument('--base', '-bc',
                    nargs = 1,
                    help='Base currency')
parser.add_argument('--target', '-tc',
                    nargs = 1,
                    help='Target currency')
parser.add_argument('--amount', '-a',
                    nargs = '?',
                    default = 1,
                    help = 'Amount that should be exchanged')
# parser.add_argument('--mock', '-mk',
#                     nargs = '?',
#                     default = 1,
#                     help = 'Mock')

args = parser.parse_args()

# Access argument values
base_c = args.base
target_c = args.target
amount = args.amount




if __name__ == '__main__':
    print(f'base currency: {base_c} \ntarget currency: {target_c}')