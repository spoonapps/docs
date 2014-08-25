"""A script for dealing with name changes to topics and/or 
sections of the docs

USAGE: python migrate.py --topic [topic name] --section [section name] --to [new name]
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
	#dispatch based on what was specified
	if args.topic is None:
		raise MissingArgError("topic must be specified!")
	if args.to is None:
		raise MissingArgError("must specify a name to migrate to (--to)")
	if args.section is None:
		#need to migrate topics
		topic_migration(doc_dir, args.topic, args.to)
	else:
		section_migration(doc_dir, args.topic, args.section, args.to)

if __name__ == "__main__":
	main()