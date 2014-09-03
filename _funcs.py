from __future__ import print_function
import fileinput, os, yaml, shutil, re
from urllib import quote_plus
from BeautifulSoup import BeautifulSoup
from argparse import ArgumentParser
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from _classes import DocTemplate, DocTopic, DocSection

#=======================
#BUILD SCRIPT FUNCTIONS
#=======================
def mutate_path_for_web(file_path, _dir):
    """Mutates the file path provided and turns it into a
    suitable path for incorporation into the spoonium docs page
    """
    return file_path.replace(_dir, "../components/docs").replace("\\", "/")


def process_markdown_file(markdown_file):
    """Processes the markdown file and returns HTML in "Spoonium" format
    """
    #convert to html
    with open(markdown_file, 'r') as f:
        text = f.read()
    return markdown(text, extras=['wiki-tables', 'fenced-code-blocks'])


def process_html_for_spoonium(html):
    #switch <blockquote><p> --> <pre><code> (for cmd blocks within ul/ols)
    soup  = BeautifulSoup(html)
    for blockquote in soup.findAll('blockquote'):
        blockquote.name = 'pre'
        for p in blockquote.findAll('p'):
            p.name = 'code'
    #find any tables and add class="doc-table"
    for table in soup.findAll('table'):
        table['class'] = 'doc-table'
    #find all <pre><code> blocks without code highlighting and format for cmdline
    code_blocks = [code.text
                   for code in soup.findAll('code')
                   if code.parent.name == 'pre']  # this logic is good
    #TODO: parse the text for '#' and '>' and style lines appropriately
    #trying to split the text into an array and process --> lose the assignment.. may need regex
    return str(soup)


def create_doc_from_yaml(yaml_file):
    """Creates a DocTemplate from a yaml file
    Returns the new DocTemplate
    """
    doc = DocTemplate()
    with open(yaml_file, 'r') as f:
        topics = yaml.load_all(f)
        for topic in topics:
            #create a new DocTopic
            _topic = DocTopic(topic['display_name'], topic['ordering'])
            for section in topic['sections']:
                #create a new topic
                _section = DocSection(section['display_name'], section['ordering'], section['pages'], section['subsections'])
                #add it to the _topic
                _topic.add_section(_section)
            #add the topic to the doc
            doc.add_topic(_topic)
    return doc


def process_directory(dirpath, files, root_build_dir, doc_template):
    """Processes a directory, adding all of the pages in the directory
    to the appropriate section of the docs

    Within this function, the markdown is also converted to HTML and added
    to the parallel folder in the build directory
    """
    #generate an output directory for the files, if one doesn't already exist
    output_dir = dirpath.replace("\\doc\\", "\\build\\")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    directory_meta = process_dir_meta(dirpath)
    topic = doc_template.get_topic_named(directory_meta['topic'])
    section = topic.get_section_named(directory_meta['section'])
    
    #if we get here, then the section must exist
    for f in files:
        if f == "meta.md":
            continue  #don't process it!
        elif f.endswith(".md"):
            #generate html and add to build dir
            html = process_markdown_file(os.path.join(dirpath, f))
            html = process_html_for_spoonium(html)
            output_file_path = os.path.join(output_dir, f[:-2] + "html")
            write_to_file(output_file_path, html)
            #add to doc template
            mutated_path = mutate_path_for_web(output_file_path, root_build_dir)
            section.add_page(mutated_path)
        else:
            #this is a resource file and should be copied over
            shutil.copyfile(dirpath+"\\"+f, output_dir+"\\"+f)
    return doc_template


def process_dir_meta(directory):
    meta_file = os.path.join(directory, "meta.md")
    with open(meta_file, 'r') as f:
        text = f.read()
    meta = markdown(text, extras=['metadata'])
    return meta.metadata


#DEPRECTATED
def write_docshtml(doc_template, build_dir):
    """renders a jinja2 template for the docs
    and writes it to an html file
    """
    root_dir = os.path.abspath(os.path.join(build_dir, os.pardir))
    print(root_dir)
    env = Environment(loader=FileSystemLoader(os.path.join(root_dir, "templates")))
    template = env.get_template('docs_temp.html')
    docs_html = template.render(doc_template=doc_template)
    #write to a file
    write_to_file(os.path.join(build_dir, "docs.html"), docs_html)


def write_docspages(doc_template, build_dir):
    """renders a jinja2 template for each docs
    page and writes it to an html file
    """
    root_dir = os.path.abspath(os.path.join(build_dir, os.pardir))
    print(root_dir)
    env = Environment(loader=FileSystemLoader(os.path.join(root_dir, "templates")))
    template = env.get_template("docs_temp.html")
    sidenav_template = env.get_template("sidenav.html")
    for topic in doc_template.get_ordered_topics():
        html = template.render(doc_template=doc_template, intopic=topic)
        write_to_file(os.path.join(os.path.join(build_dir, "docs"), topic.get_link_name() + ".html"), html)
        #write sidenav component for topic
        sidenav_html = sidenav_template.render(topic=topic)
        write_to_file(os.path.join(os.path.join(build_dir, "sidenav"), topic.get_link_name() + ".html"), sidenav_html)
        

def write_to_file(file_path, text):
    """Write the contents of the input text to a file
    at the given file_path
    """
    with open(file_path, 'w') as f:
        f.write(text)


def generate_link(name):
    """Generates the text to use a link for the given name
    """
    return quote_plus(re.sub(r'[^_a-zA-Z0-9 -]*', '', name.lower()))

#==========================
#MIGRATION SCRIPT FUNCTIONS
#==========================

def make_parser():
    """creates an argument parser for the migration SCRIPT
    """
    parser = ArgumentParser()
    parser.add_argument("--topic", action="store", default=None,
                        help="the topic, or topic of the section, to migrate")
    parser.add_argument("--section", action="store", default=None,
                        help="the section to migrate")
    parser.add_argument("--to", action="store", default=None,
                        help="the display_name to change the object to")
    return parser

def topic_migration(doc_dir, current_name, new_name):
    """change the name of a topic in the meta.yaml and in all links and meta files
    """
    #find the topic in the meta.yaml and rewrite it
    new_topics = [] #empty list of converted topics
    found = False
    meta_yaml = os.path.join(doc_dir, "meta.yaml")
    with open(meta_yaml, 'r') as f:
        topics = yaml.load_all(f)
    for topic in topics:
        print("comparing {0} and {1}".format(current_name, topic['display_name']))
        if current_name == topic['display_name']:
            #match!
            topic['display_name'] = to_name
            print( '  matched!')
            found = True
        else:
            pass
        new_topics.append(topic)
    if not found:
        print("didn't find topic %s" % new_name)
        return 1
    else:
        #move all the meta files
        migrate_topic_meta(doc_dir, current_name, new_name)
        migrate_links(doc_dir, current_name, new_name)
        with open(meta_yaml, 'w') as f:
            for topic in new_topics:
                f.write('---\n')
                yaml.dump(topic, f, default_flow_style=False)
        return 0

def section_migration(doc_dir, topic_name, current_name, new_name):
    """change the name of a section in a topic and migrate all links and meta files
    """
    new_topics = [] #empty list of converted topics
    found = False
    meta_yaml = os.path.join(doc_dir, "meta.yaml")
    with open(meta_yaml, 'r') as f:
        topics = yaml.load_all(f)
        for topic in topics:
            if topic.display_name == topic_name:
                #look for section
                for section in topic['sections']:
                    print(' comparing {0} and {1}'.format(current_name, section['display_name']))
                    if current_name == section['display_name']:
                        found = True
                        print('    matched!')
                        section['display_name'] = new_name #assign the new name
                    else:
                        pass
            else:
                continue
    if not found:
        print("didn't find section %s" % new_name)
        return 1
    else:
        #move all the meta files
        migrate_section_meta(doc_dir, topic_name, current_name, new_name)
        migrate_links(doc_dir, topic_name, current_name, new_name)
        with open(meta_yaml, 'w') as f:
            for topic in new_topics:
                f.write('---\n')
                yaml.dump(topic, f, default_flow_style=False)
        return 0


def migrate_topic_meta(doc_dir, topic_name, to_name):
    """for migrating topic meta files
    """
    replacement_string = "---\ntopic: {0}\nsection: {1}\n---"
    for dirpath, sub_dirs, files in os.walk(doc_dir):
        if "meta.md" not in files:
            continue
        else:
            with open(os.path.join(dirpath, "meta.md"), 'r') as f:
                text = f.read()
                meta = markdown(text, extras=['metadata'])
            if meta.metadata['topic'].lower() == topic_name.lower(): 
                #match!
                print("    found matching meta file in {0}".format(dirpath))
                with open(os.path.join(dirpath, "meta.md"), 'w') as f:
                    f.write(replacement_string.format(to_name, meta.metadata['section']))
            else:
                continue


def migrate_section_meta(doc_dir, topic_name, section_name, to_name):
    """for migrating the section name in meta files
    """
    replacement_string = "---\ntopic: {0}\nsection: {1}\n---"
    for dirpath, sub_dirs, files in os.walk(doc_dir):
        if "meta.md" not in files:
            continue
        else:
            with open(os.path.join(dirpath, "meta.md"), 'r') as f:
                text = f.read()
                meta = markdown(text, extras=['metadata'])
            if meta.metadata['topic'].lower() == topic_name.lower() and meta.metadata['section'].lower() == section_name.lower(): 
                #match!
                print("    found matching meta file in {0}".format(dirpath))
                with open(os.path.join(dirpath, "meta.md"), 'w') as f:
                    f.write(replacement_string.format(meta.metadata['topic'], section_name))
            else:
                continue

def migrate_links(doc_dir, topic_name, section_name=None, to_name=None):
    """migrate all the links corresponding to a particular topic/section
    """
    if to_name is None:
        raise ValueError("must specify a to_name parameter")
    #form the string to find and replace with
    base_string = "(/docs/{0}"
    base_match = base_string.format(generate_link(topic_name))
    if section_name is None:
        match_string = base_match
        replace_string = base_string.format(generate_link(to_name))
    else:
        match_string = "#".join([base_match, generate_link(section_name)])
        replace_string = "#".join([base_match, generate_link(to_name)])
    #walk the directories and find/replace matches
    for dirpath, sub_dirs, files in os.walk(doc_dir):
        for f in files:
            for line in fileinput.input(os.path.join(dirpath, f), inplace=True):
                print(line.replace(match_string, replace_string), end='')
