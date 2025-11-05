
from logger_config import my_logger
from cli import cli
from converter import converter

logger = my_logger()


def main():

    base, target, amount, mock = cli()

    converted = converter(base,target,amount,mock)

    print(f"{amount} {base} = {converted} {target}")

    return converted


if __name__ == "__main__":
    main()
    
