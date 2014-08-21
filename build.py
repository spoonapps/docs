"""The primary build script for the spoonium docs! 

To build the docs, run this script from the command line: 
>python build.py 

This will generate:
1. a /build folder that mirrors the structure of the /doc folder except all the markdown has been converted
to html
2. a new docs.html file in the /build -- this is the new version of /docs on spoonium.net
"""

import sys, os
from _classes import DocTemplate, DocTopic, DocSection, NoMetaFileError
from _funcs import create_doc_from_yaml, process_dir, write_docshtml, write_docspages


def main(doc_dir, build_dir):
    """Walk the doc directory and create a build folder and json resource
    """
    #create the initial doc template
    doc_template = create_doc_from_yaml(os.path.join(doc_dir, "meta.yaml"))
    #start walking... 
    for dirpath, sub_dirs, files in os.walk(doc_dir):
        if "meta.md" not in files:
            if dirpath == doc_dir or len(files) < 2:  #ignore the top level of doc dir and dirs without files
                continue
            else:
                #missing a meta file where there should be one
                raise NoMetaFileError(dirpath)
        else:
            #process the directory, adding all the pages found to the 
            #appropriate section of doc_template
            print("Processing directory %s" % dirpath)
            tmp_template = process_dir(dirpath, files, build_dir, doc_template)
            if tmp_template is None:  #hack to prevent null assignment on final walk
                continue
            doc_template = tmp_template
    #should now have a completed build dir and a doc template
    print("building docs.html...")
    write_docspages(doc_template, build_dir)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("no args necessary -- run from the root directory of the repo!")
        sys.exit(1)
    else:
        #default to 
        script_dir = os.path.dirname(os.path.realpath(__file__))
        build_dir = os.path.join(script_dir, "build")
        if not os.path.exists(build_dir):  #root build dir
            os.makedirs(build_dir)
        if not os.path.exists(os.path.join(build_dir, "docs")):  #subdir to dump main doc html files to
            os.makedirs(os.path.join(build_dir, "docs"))
        main(os.path.join(script_dir, "doc"), build_dir)
        print("Success!!")
        sys.exit(0)