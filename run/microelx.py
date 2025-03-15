"""
.. py:currentmodule:: py_main.py

Runs a shell command.
"""

from  inspect import currentframe
import logging
import sys
# import importlib
from typing import Any
from typing import List   # also available: Dict, Set

import parse_cmd_line
import parse_config_file
from chap01 import class_chap01
from chap02 import class_chap02
from chap03 import class_chap03
from chap05 import class_chap05
# from chap77 import class_chap77
from logger import logger


def main() -> int:
	"""
	Entry point for script.

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	try:
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; function: '{fcn_name}'" )

		parse_cmd_line.parse_the_args()
		# print( f">>>subcmd specified on cmd-line is '{parse_cmd_line.chapter_subcmd}'" )
		# print( f">>>cfg.ini specified on cmd-line is '{parse_cmd_line.path_to_config_file}'" )
		pcf:parse_config_file.ParseConfigFile = parse_config_file.ParseConfigFile( parse_cmd_line.path_to_config_file )

		lg:logging.Logger = logger.build_logger( pcf, parse_cmd_line.chapter_subcmd )

		# # Example to retrieve all modules-by-name
		# global_variables = globals()
		# # Filter out modules that start with '__' and are instances of types like 'sys' (modules)
		# modules = {name: obj for name, obj in global_variables.items() if isinstance(obj, type(sys)) and not name.startswith('__')}
		# # List of module names
		# module_names = list(modules.keys())
		# print( f"module_names: {module_names}" )

		# Retrieve the command-line subcommand as this is the "operation" to perform.
		# This is the implementation of the source-code's design.
		class_name:str = parse_cmd_line.chapter_subcmd
		# print( f"class_name: {class_name}" )
		# Convert the camel-case classname to all lowercase.
		cllow:str = class_name.lower()
		# Generate the module name as below; again, this is per project architecture
		# module-by-subdir and source-code fnames.
		module_name:str = f"class_{cllow}"

		try:
			# Retrieve the module's reference per its name:str
			module_ref = globals()[module_name]
			# print( f"module_ref: '{module_ref}' -> TYPE: '{type(module_ref)}'" )
			# Retrieve the class reference from the module
			class_ref = getattr( module_ref, class_name )
			# print( f"class_ref: '{class_ref}' -> TYPE: '{type(class_ref)}'" )
			# Setup the __init__ parameters
			params = [pcf,lg]
			# Instantiate the class and run it
			# Chap 01
			# class_ref( *params ).run()
			# Chap 02 and above
			class_ref( *params ).run_in_subdir()
			# Note per line above: the code in the run() class-method could be moved
			# to the end of the class __init__() method there eliminating the need
			# for the run() method.  Then, the call would simply be as below:
			# class_ref( *params )
		except AttributeError as e:
			print( f"Exception caught in main: {e} for getattr( {class_ref} )" )

	except FileExistsError as e:
		print( f"Exception caught in main: {e}" )

	return 0


# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
