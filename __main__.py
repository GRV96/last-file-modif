from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from sys import exit


def _make_arg_parser():
	parser = ArgumentParser()
	parser.add_argument("-d", "--directory", type=Path, required=True,
		help="The path to a directory")
	parser.add_argument("-p", "--parents", type=int, required=False, default=0,
		help="The number of parent directories to display with the file names")
	return parser


def _rel_path_with_nb_parents(some_path, nb_parents):
	if nb_parents >= 1:
		some_path = some_path.resolve()
		some_path_parents = some_path.parents

		max_nb_parents = len(some_path_parents)
		if nb_parents >= max_nb_parents:
			nb_parents = max_nb_parents - 1

		return some_path.relative_to(some_path_parents[nb_parents])

	else:
		return some_path.name


arg_parser = _make_arg_parser()
args = arg_parser.parse_args()
directory = args.directory
nb_parents = args.parents

if not directory.is_dir():
	print("-d/--direcotry: A direcotry is expected.")
	exit(1)

for item in directory.glob("*"):
	last_modif_timestamp = item.stat().st_mtime
	last_modif_moment = datetime.fromtimestamp(last_modif_timestamp)
	last_modif_strf = last_modif_moment.isoformat()

	item = _rel_path_with_nb_parents(item, nb_parents)
	print(f"{item}....{last_modif_strf}")
