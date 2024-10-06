"""
This command line application displays the name and the moment of the last
modification of each item in the specified directory.
"""


from datetime import datetime
from pathlib import Path
from argparse import ArgumentParser
from sys import exit


_DOT = "."


class LastModifOutput:
	def __init__(self, name, moment):
		self._name = name
		self._moment = moment

	@property
	def name(self):
		return self._name

	@property
	def moment(self):
		return self._moment


def _make_arg_parser():
	parser = ArgumentParser(description=__doc__)
	parser.add_argument("-d", "--directory", type=Path, required=True,
		help="The path to a directory")
	parser.add_argument("-p", "--parents", type=int, required=False, default=0,
		help="The number of parent directories to display before the file names")
	return parser


def _rel_path_with_nb_parents(some_path, nb_parents):
	if nb_parents <= 0:
		return some_path.name

	some_path = some_path.resolve()
	some_path_parents = some_path.parents

	if nb_parents < len(some_path_parents):
		return some_path.relative_to(some_path_parents[nb_parents])

	return some_path


arg_parser = _make_arg_parser()
args = arg_parser.parse_args()
directory = args.directory
nb_parents = args.parents

if not directory.is_dir():
	print("-d/--direcotry: A direcotry is expected.")
	exit(1)

outputs = list()
greatest_length = 0
for item in directory.glob("*"):
	last_modif_timestamp = item.stat().st_mtime
	last_modif_moment = datetime.fromtimestamp(last_modif_timestamp)
	last_modif_strf = last_modif_moment.isoformat()

	item = _rel_path_with_nb_parents(item, nb_parents)
	item_str = str(item)
	name_length = len(item_str)
	outputs.append(LastModifOutput(item_str, last_modif_strf))

	if name_length > greatest_length:
		greatest_length = name_length

greatest_length += 4
for output in outputs:
	name = output.name
	name_length = len(name)
	nb_dots = greatest_length - name_length

	print(f"{name}{_DOT * nb_dots}{output.moment}")
