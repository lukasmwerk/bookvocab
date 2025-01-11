import argparse
import sys
from typing import List

def main(args: List[str] = sys.argv[1:]) -> None:
    parsed_args = parse_args(args)


def parse_args(args: List[str]) -> argparse.Namespace:
    pass