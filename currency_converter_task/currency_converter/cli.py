"""
This should handle command line arguments
"""

import argparse

def cli():
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
                        required= True, type= float,
                        help = 'Amount that should be exchanged')
    parser.add_argument('--mock', '-mk',
                        action = 'store_true',
                        # nargs = '?',
                        # default= True,
                        help = 'If true run Mock json file')

    args = parser.parse_args()

    # Access argument values
    base = args.base
    target = args.target
    amount = args.amount
    mock = args.mock
    #print(f'base currency: {base} \ntarget currency: {target} ,\n {amount}, \n {mock}')

    return base, target, amount, mock

if __name__ == '__main__':
    cli()
   # print(f'base currency: {base_c} \ntarget currency: {target_c}')