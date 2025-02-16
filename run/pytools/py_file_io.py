import glob
# import subprocess
import os
import re
import shutil
# import sys

from pathlib import Path
from typing import Any
from typing import List   # also available: Any, Dict, Set, Tuple
from typing import Tuple


def count_files_in_directory( directory:str ):
	try:
		# Create a Path object
		path = Path(directory)
		# Count files
		file_count = sum(1 for entry in path.iterdir() if entry.is_file())
		return file_count
	except Exception as e:
		print(f"ERROR count_files_in_directory: {e}")
		return None


def copy_files_per_text_file( fpath:str, subdir_to:str ) -> None:
	"""The source text file contains the paths to the XML files to copy.
	Since there are duplicate fnames under different subdirs, a "count"
	is appended to the source-xml file for the destination (copy-to).
	Note that the copy-cmd does not tolerate '\n' at end of string.
	Note that the source-xml.txt file was manually modified to support the
	'shutil.copy' call (below).

	Args:
		fpath:str to text file with paths to src-files to copy
		subdir:str dir for copy-to

	Returns:
		List of source-xml files to be copied

	"""
	# print( f"subdir: '{subdir_to}'" )
	with open( fpath, 'r' ) as file:
		# Read the entire content of the file into a list object
		file_content = file.readlines()

	# print( f"{len(file_content)}" )
	count = 0
	for fin in file_content:
		sfile = fin.strip()
		count += 1
		# Get basename and extension separately
		path = Path( sfile )
		path.parents
		bname = path.stem
		extension = path.suffix

		# append the count to bname
		count_str = f"{count:04}"
		new_fname = f"{bname}_{count_str}{extension}"
		dest_path = os.path.join( subdir_to, new_fname )
		print( f"sfile: {sfile}" )
		print( f"dest_path: {dest_path}" )
		# subprocess.run( ['copy', sfile, dest_path], shell=True )
		# result = subprocess.run(['copy', "y:\\Contactless_Protocol_Dry-Run\\Submissions\\AATech\\20230628T1359-AA_Technology_Intl-01-Submission\\Person-A-Finger-01.xml", ""], capture_output=True, text=True )
		shutil.copy(sfile, dest_path)
		# sys.exit()


def does_file_exist( subdir:str, fname:str ) -> bool:
	"""Build the file PATH from the parameters.

	Args:
			subdir:str dir path where file exists (or not)
			fname: str 

	Returns:
			bool True if file exists
	"""
	fnd = False
	print( '++++++++++++++++++++CHECK output csv exists ')
	print( f"subdir: '{subdir}'")

	# get basename of SEARCH response file
	print( f"fname: '{fname}'")
	# bname = os.path.basename( fname )
	# print( f"bname: '{bname}'")

	# change extension from .txt to .csv
	# base, _ = os.path.splitext( bname )
	# Add the new extension
	# new_filename = f"{base}.{'csv'.lstrip('.')}"
	new_filename = f"{fname}.csv"
	print( f"new_filename: '{new_filename}'")

	# append new fname to subdir output file
	path_output = os.path.join( subdir, new_filename )
	print( f"path_output: '{path_output}'")

	if os.path.isfile( path_output ):
		fnd = True

	return fnd


def file_read_return_string( fpath:str ) -> Tuple[str,int]:
	"""_summary_

	Args:
			fpath:str full PATH to file

	Returns:
			_str_: _entire file's content into single string_
			_int_: length of string
	"""
	# Open the file in read mode
	with open( fpath, 'r' ) as file:
		# Read the entire content of the file into a variable
		file_content = file.read()
	
	lngth = len(file_content)

	return file_content, lngth


def file_read_return_array( fpath:str ) -> Tuple[List[str],int]:
	"""_summary_

	Args:
			fpath (str): full PATH to file

	Returns:
			_list_: entire file's content into list object
			_int_: COUNT elements in _list_
	"""
	# Open the file in read mode
	with open(fpath, 'r') as file:
		# Read the entire content of the file into a variable
		file_content = file.readlines()
	
	# print( f"type file content: {type(file_content)}" )

	lngth = len(file_content)

	return file_content, lngth


def file_read_as_binary( fpath:str ) -> Tuple[bytes,int]:
	"""
	Read a binary file.

	Args:
			fpath (string): full PATH to file

	Returns:
			_list_: entire file's content into list object
			_int_: COUNT elements in _list_
	"""
	with open( fpath, 'rb' ) as file:
		file_content = file.read()

	lngth = len(file_content)

	return file_content, lngth


def glob_dirs_only( glob_path:str ) -> List[str]:
	"""
	"""
	list_subdirs = [d for d in glob.glob( glob_path ) if os.path.isdir(d) ]
	return list_subdirs


def glob_list_in_subdirs( subdir:str, ext:str ):
	"""
	Use this function when the subdir(param) contains only subirs (and not files)
	like for the case when SEARCH-response files are spread across subdirs and
	not all files are in one subdir (see glob_expr).

	Args:
			dir (str): subdir containing only subdirs to glob
			ext (str): 'txt' for SEARCH-response files
								 'csv' for SEARCH-survey files

	Returns:
			list: of PATHs
	"""

	def alphanumeric_key( s:str ):
		# Split the string into a list of numbers and non-numbers
		return [int(text) if text.isdigit() else text for text in re.split('(\\d+)', s)]

	glob_expr = os.path.join(subdir, "./**/*.") + ext
	items = glob.glob( glob_expr )
	sorted_items = sorted(items, key=alphanumeric_key)
	return sorted_items


def glob_list_of_files( subdir:str, ext:str ) -> List[str]:
	"""
	Use this function when the subdir(param) contains only files and no further
	subdirs (see glob_expr).

	Args:
			dir (str): subdir containing files to glob
			ext (str): compression-type

	Returns:
			list: of PATHs
	"""

	def alphanumeric_key( s:str ):
		# Split the string into a list of numbers and non-numbers
		return [int(text) if text.isdigit() else text for text in re.split('(\\d+)', s)]

	glob_expr = os.path.join(subdir, "*.") + ext
	# print( f"glob_expr: '{glob_expr}'" )
	# glob_dir = os.path.join(glob_expr) + ext
	# for name in glob.glob( glob_dir ):
	#     print(name)

	items = glob.glob( glob_expr )

	sorted_items = sorted(items, key=alphanumeric_key)

	return sorted_items


def write_list_to_file( path:str, data:List[str] ):
	"""
	Write to text file.

	Args:
			fpath : string full PATH to file
			data : list of the data to be written

	"""
	with open( path, 'w' ) as file:
		for item in data:
			file.write( f"{item}\n" )


def write_list_list_to_file( path:str, header:str, data:List[List[Any]] ):
	"""
	Write to text file.

	Args:
			fpath : string full PATH to file
			data : list of the data to be written

	"""
	with open( path, 'w' ) as file:
		file.write( f"{header}\n" )
		for item in data:
			s:str = ','.join(str(num) for num in item)
			file.write( f"{s}\n" )


def write_append_line_to_file( path:str, data:str ):
	"""
	Append to text file.

	Args:
			fpath : string full PATH to file
			data : single line to append

	"""
	with open( path, 'a' ) as file:
		file.write( f"{data}\n" )
