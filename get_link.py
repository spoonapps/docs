import sys, os
from argparse import ArgumentParser
from _classes import CommandLineArgs
from _funcs import generate_link

def main(args):
    base_string = "/docs/{0}".format(generate_link(args.topic))
    if args.section is None:
        return base_string
    else:
        return "#".join([base_string, generate_link(args.section)])


def make_parser():
    """creates an argument parser for the migration SCRIPT
    """
    parser = ArgumentParser()
    parser.add_argument("--topic", action="store", default=None,
                        help="the topic to link to")
    parser.add_argument("--section", action="store", default=None,
                        help="the section to link to")
    return parser


if __name__ == "__main__":
    parser = make_parser()
    args = CommandLineArgs()
    parser.parse_args(namespace=args)
    if args.topic is None:
        print("must specify a topic!")
        sys.exit(-1)
    else:
        link = main(args)
        print(link)
        sys.exit(0)