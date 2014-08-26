import sys, os, re
from argparse import ArgumentParser
from _classes import CommandLineArgs, MissingArgError
from urllib2 import urlopen, HTTPError, URLError

def check_links(directory, domain):
    link_regex = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")  #setup the regex
    for dirpath, sub_dirs, files in os.walk(directory):
        for _file in files:
            #read all the text in the file
            with open(os.path.join(dirpath, _file), 'r') as f:
                print("reading file {0}".format(os.path.join(dirpath, _file)))
                text = f.read()
            #extract links from text
            for match in re.finditer(link_regex, text):
                #form a url to make a request to
                if is_internal(match.group(2)):
                    link_text = domain + match.group(2)
                elif is_mailto(match.group(2)):
                    continue  #skip mail links
                elif is_emptylink(match.group(2)):
                    print('  link "{0}" was an empty link (#)'.format(match.group(1)))
                    continue
                else:
                    link_text = match.group(2)
                #open the url and get the status code
                try:
                    url_return = urlopen(link_text)
                    status_code = url_return.getcode()
                except HTTPError:
                    status_code = 404
                except (URLError, ValueError):
                    status_code = 690
                #record errors
                if status_code == 200:
                    continue  #don't cause alarm
                else:
                    print('  link "{0}" returned status code {1}'.format(match.group(1), status_code))

def is_internal(link):
    if link[0] == "/":
        return True
    else:
        return False

def is_mailto(link):
    if link[:6] == "mailto":
        return True
    else:
        return False

def is_emptylink(link):
    if link == "#":
        return True
    else:
        return False

def make_parser():
    """creates an argument parser for the migration SCRIPT
    """
    parser = ArgumentParser()
    parser.add_argument("--topic", action="store", default=None,
                        help="the topic to link to")
    return parser

if __name__ == "__main__":
    #setup directories
    script_dir = os.path.dirname(os.path.realpath(__file__))
    doc_dir = os.path.join(script_dir, "doc")
    #parse command line args
    parser = ArgumentParser()
    parser.add_argument("--domain", action="store", default="http://spoonium.net",
                        help="the root domain to check relative links against")
    args = CommandLineArgs()
    parser.parse_args(namespace=args)
    check_links(doc_dir, args.domain)