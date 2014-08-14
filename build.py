import sys,os
from BeautifulSoup import BeautifulSoup
from markdown2 import markdown_path


def main(root_dir):
	"""Do the actual work of the script
	"""
	doc_dir = os.path.join(root_dir, "doc")
	md_files = get_md_files(doc_dir)
	#create the build directory(s) if it doesn't already exist
	build_dir = os.path.join(root_dir, "build")
	if not os.path.exists(build_dir):
		os.makedirs(build_dir)
	#convert the md files to html and write them to a file
	for md in md_files:
		file_name = os.path.basename(md)[:-3] + ".html"
		html = convert_to_html(md)
		sp_html = convert_html_to_spooniumHTML(html)
		#form the filepath for the new file
		output_dir = os.path.dirname(md).replace("\\doc\\", "\\build\\")
		#make sure the directory exists
		if not os.path.exists(output_dir):
			os.makedirs(output_dir)
		#write it to a file
		write_to_file(file_path=os.path.join(output_dir, file_name), text=sp_html)
		
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
	f = open(file_path, 'w')  #overwrite if the file already exists
	f.write(text)
	f.close()

if __name__ == "__main__":
	if len(sys.argv) > 1:
		print("no args necessary -- run from the root directory of the repo!")
		sys.exit(1)
	else:
		#default to 
		script_dir = os.path.dirname(os.path.realpath(__file__))
		main(script_dir)
		sys.exit(0)