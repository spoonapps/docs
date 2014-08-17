import sys, os
import json
from BeautifulSoup import BeautifulSoup
from markdown2 import markdown_path, markdown


def main(doc_dir, build_dir):
	"""Walk the doc directory and create a build folder and json resource
	"""
	#start walking... 
	for dirpath, sub_dirs, files in os.walk(doc_dir):
		if "meta.md" not in files:
			if len(files) < 2:  #need to have at least a file and meta.md
				continue
			else:
				raise NoMetaFileError(dirpath)
		else:
			process_directory(dirpath, files, build_dir)
	#construct the json from the _docs object
	resource_json = json.dumps(_docs, cls=ObjectToDictEncoder, sort_keys=True, indent=2) 
	write_to_file(file_path=os.path.join(build_dir, "meta.json"), text=resource_json)


def process_directory(dirpath, files, root_build_dir):
	"""Processes a directory and adds its representation as a Section to the 
	_docs object
	"""
	#generate an output directory for the files
	output_dir = dirpath.replace("\\doc\\", "\\build\\")
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	#read the meta.md and get a section object to work with
	section_name = process_metafile(os.path.join(dirpath, "meta.md"))
	section = get_section(section_name)
	#if the section doesn't exist, create it
	if get_section(section_name) is None:
		section = Section(section_name)
		_docs.add_section(section)
	#for each file convert to html add it to the section
	for f in files:
		if f == "meta.md":
			#don't process it!
			continue
		else:
			#write the new html file
			html = markdown_path(os.path.join(dirpath, f))
			sp_html = convert_html_to_spooniumHTML(html)
			new_file_path = os.path.join(output_dir, f[:-2] + "html")
			write_to_file(file_path=new_file_path, text=sp_html)
			#add the new path to the section
			mutated_path = mutate_path_for_web(new_file_path, build_dir)
			section.add_page(mutated_path)


def mutate_path_for_web(file_path, _dir):
	"""Mutates the file path provided and turns it into a
	suitable path for incorporation into the spoonium docs page
	"""
	return file_path.replace(_dir, "components/docs").replace("\\", "/")


def get_section(section_name):
	for _section in _docs.sections:
		if section_name == _section.name:
			return _section
		else:
			continue
	return None


def process_metafile(meta_file):
	"""Processes the meta file and returns the section name
	"""
	with open(meta_file, 'r') as f:
		text = f.read()
	meta = markdown(text, extras=['metadata'])
	return meta.metadata['section']


def get_md_files(root_dir):
	"""Traverses all of the subdirectories in the supplied directory
	and returns a list of the full paths to each markdown file
	in the directory
	"""
	return [os.path.join(d, f)
			for d, sub_dir, files in os.walk(root_dir)
			for f in files if f.endswith(".md")]


def convert_to_html(md_file_path):
	"""Converts the markdown file to the expected HTML format to 
	be used in the spoonium docs
	"""
	return markdown_path(md_file_path)


def convert_html_to_spooniumHTML(html_in):
	"""Wraps the input html in a <div class="wiki-content"></div>
	for use in the spoonium docs. It will also find the h1 and assign it an ID corresponding to
	the content of that h1. 

	Example h1 conversion: <h1>Spoonium Basics</h1> --> <h1 id="Spoonium_Basics">Spoonium Basics</h1>
	"""
	#find any h1's and convert them
	soup = BeautifulSoup(html_in)
	for h1 in soup.findAll('h1'):
		h1['id'] = h1.string.replace(' ', '_')
	#wrap the content in a div and return
	return '<div class="wiki-content">\n' + str(soup) + '\n</div>'


def write_to_file(file_path, text):
	"""Write the contents of the input text to a file
	at the given file_path
	"""
	with open(file_path, 'w') as f:
		f.write(text)


class Section:
	"""Represents a section of the docs, AKA an id that can be linked to
	"""
	def __init__(self, name):
		self.name = name
		self.pages = []

	def to_dict(self):
		return {
			"name": self.name,
			"pages": self.pages
		}
	
	def add_page(self, page):
		self.pages.append(page)


class NoMetaFileError(Exception):
	"""Raised when a meta.md file is not found in a directory
	"""

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)


class ObjectToDictEncoder(json.JSONEncoder):
	"""Just serializes an object based on its to_dict method
	"""
	def default(self, obj):
		return obj.to_dict()


class Docs:
	"""Represents the docs, in total
	"""
	def __init__(self):
		self.topics = []  #the sections for the navbar
		

	def add_section(self, section):
		self.sections.append(section)

	def to_dict(self):
		return {'docs': self.sections}

_docs = Docs() #the doc object to work on -- global
if __name__ == "__main__":
	if len(sys.argv) > 1:
		print("no args necessary -- run from the root directory of the repo!")
		sys.exit(1)
	else:
		#default to 
		script_dir = os.path.dirname(os.path.realpath(__file__))
		build_dir = os.path.join(script_dir, "build")
		if not os.path.exists(build_dir):
			os.makedirs(build_dir)
		main(os.path.join(script_dir, "doc"), build_dir)
		sys.exit(0)