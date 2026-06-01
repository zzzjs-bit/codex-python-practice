import argparse
import math


def parse_positive_number(value, name):
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{name} must be a number.")

    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError(f"{name} must be greater than 0.")

    return number


def format_jpy_amount(amount):
    if amount.is_integer():
        return str(int(amount))
    return f"{amount:.2f}"


def build_parser():
    parser = argparse.ArgumentParser(
        description="Convert Japanese yen (JPY) to Chinese yuan (CNY)."
    )
    parser.add_argument(
        "--jpy",
        required=True,
        type=lambda value: parse_positive_number(value, "--jpy"),
        help="Amount in Japanese yen. Must be greater than 0.",
    )
    parser.add_argument(
        "--rate",
        required=True,
        type=lambda value: parse_positive_number(value, "--rate"),
        help="JPY to CNY exchange rate. Must be greater than 0.",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    cny = args.jpy * args.rate
    print(f"{format_jpy_amount(args.jpy)} JPY ≈ {cny:.2f} CNY")


if __name__ == "__main__":
    main()
