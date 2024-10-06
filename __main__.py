from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from sys import exit


def _make_arg_parser():
	parser = ArgumentParser()
	parser.add_argument("-d", "--directory", type=Path, required=True,
		help="The path to a directory")
	return parser


arg_parser = _make_arg_parser()
args = arg_parser.parse_args()
directory = args.directory

if not directory.is_dir():
	print("-d/--direcotry: A direcotry is expected.")
	exit(1)

for item in directory.glob("*"):
	last_modif_timestamp = item.stat().st_mtime
	last_modif_moment = datetime.fromtimestamp(last_modif_timestamp)
	print(f"{item.name} {last_modif_moment}")
