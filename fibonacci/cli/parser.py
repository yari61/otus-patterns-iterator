from __future__ import annotations
from argparse import ArgumentParser
from pathlib import PurePath

parser = ArgumentParser("fibonacci")
parser.add_argument("-o", "--output", type=PurePath, required=False)
interactive_args = parser.add_argument_group("interactive")
interactive_args.add_argument("--start", type=int, required=False, default=0)
interactive_args.add_argument("--stop", type=int, required=True)
interactive_args.add_argument("--step", type=int, required=False, default=1)
