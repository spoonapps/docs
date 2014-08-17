"""A script for dealing with name changes to topics and/or 
sections of the docs

USAGE: python migrate.py --type [section/topic] --current [current name] --to [new name]
"""
import sys, os
from _classes import CommandLineArgs, MissingArgError
from _funcs import make_parser, topic_migration, section_migration

def main():
	script_dir = os.path.dirname(os.path.realpath(__file__))
	doc_dir = os.path.join(script_dir, "doc")
	#parse the command line args
	parser = make_parser()
	args = CommandLineArgs()
	parser.parse_args(namespace=args)
	#check that all were specified
	if args.type is None:
		raise MissingArgError("type")
	if args.current is None:
		raise MissingArgError("current")
	if args.to is None:
		raise MissingArgError("to")
	#split off based on type of migration
	if args.type == "topic":
		topic_migration(doc_dir, args.current, args.to)
	else:
		section_migration(doc_dir, args.current, args.to)
	
if __name__ == "__main__":
	main()