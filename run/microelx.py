
from typing import Any
from typing import List   # also available: Dict, Set


import parse_cmd_line
import parse_config_file
from class_chap01 import class_chap01
from logger import logger
# from task_ml import class_ml3


def main() -> int:
	"""
	Entry point for script.

	:rtype: int
	:returns: The resulting value from executing the desired command.
	"""

	try:
		# print( f"RUN main !!")
		parse_cmd_line.parse_the_args()
		print( f">>>subcmd specified on cmd-line is '{parse_cmd_line.opera}'" )  # 'opera' for operation
		print( f">>>cfg.ini specified on cmd-line is '{parse_cmd_line.path_to_config_file}'" )
		pcf:parse_config_file.ParseConfigFile = parse_config_file.ParseConfigFile( parse_cmd_line.path_to_config_file )

		lg = logger.build_logger( pcf, parse_cmd_line.opera )
			
		# Retrieve the command-line subcommand as this is the "operation" to perform.
		# This is the implementation of the source-code's design.
		class_name:str = parse_cmd_line.opera
		# Convert the camel-case classname to all lowercase.
		cllow:str = class_name.lower()
		# Generate the module name as below; again, this is per project architecture
		# module-by-subdir and source-code fnames.
		module_name:str = f"class_{cllow}"
		print( f"<<<<<<<<<<<<<<module_name: '{module_name}'" )
		# Retrieve the module's reference per its name:str
		# module_ref = globals()
		module_ref = globals()[module_name]
		# print( f"&&&module_ref: '{module_ref}'" )
		# Retrieve the class reference from the module
		class_ref = getattr( module_ref, class_name )
		# Setup the __init__ parameters
		params = [pcf,lg]
		# Instantiate the class and run it
		class_ref( *params )
		# class_ref( *params ).run()
		# obj = class_ref( *params )
		# obj.run()
		# print(obj)

		# print( '-------------------------------------------------------------------' )
		# print( f"+++++ALL globals()[]: {globals()}" )
		# print( f">>>>>globals()[{module_name}]: {globals()[module_name]}" )
		# print( f"%%%%%module_ref: {module_ref}" )


	except FileExistsError as e:
		print( f"Error in main: {e}" )

	return 0




# def create_class_from_string(class_name: str):
# 	# Create a new class using `type()` where:
# 	# class_name is the name of the class (string)
# 	# (object,) means it will inherit from the base `object` class
# 	return type(class_name, (object,), {})


# def create_class_with_init(class_name: str, init_params: list):
# 	# Dynamically define the __init__ method
# 	def init(self, *args):
# 		for i, param in enumerate(init_params):
# 			setattr(self, param, args[i])

# 	def callMe(self):
# 		print( 'cccccccccccccccccccccccc' )

# 	# Create the class dynamically using type()
# 	# return type(class_name, (object,), {'__init__': init})
# 	return type(class_name, (object,), {'__init__': init, 'callMe':callMe})

# This is useful when the "file" is to be run directly by python (and not imported)
if __name__ == "__main__":
	# print( 'Call ', __name__ )
	main()
else:
	print( "Do not run from import" )
