"""
Given a list of strings such as :
[
	"/home/drugs/valium/",
	"/home/routes/a/",
	"/src/doctor/pediatrician/",
]

Print the input file directory strings as a file tree structure as below:

- home
	- drugs
		- valium
	- routes
		- a
- src
	- doctor
		- pediatrician

"""

def convert_to_tree(files):
	tree = {}
	temp_tree = tree
	for file_path in files:
		directories = parse(file_path)
		for word in directories:
			if word not in list(temp_tree.keys()):
				temp_tree[word] = {}
			# Keeps track of what level we are at in the tree
			temp_tree = temp_tree[word]
		temp_tree = tree
	return tree

# Parses a given file path string into a list of directories and returns the list
def parse(file_path):
	parsed_list = file_path.split("/")
	# First and last element of parsed_list are "" due to beginning and trailing "/"
	# In our file_path input strings
	return parsed_list[1:len(parsed_list)-1]	

def print_as_directories(tree, tab=0, number_of_spaces=4):
	if not tree:
		return
	indent = ' '*tab*number_of_spaces
	for directory,sub_directory in tree.items():
		print("{}- {}".format(indent,directory))
		print_as_directories(sub_directory, tab+1)

def main():
	files =[
		"/home/drugs/xanax/",
		"/home/drugs/valium/",
		"/home/routes/a/",
		"/src/doctor/pediatrician/",
		"/src/disease/acne/",
		"/src/routes/b/",
	]
	tree = convert_to_tree(files)
	print_as_directories(tree)

main()
