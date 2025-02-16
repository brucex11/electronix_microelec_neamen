import ast
import configparser
import errno
# import logging
import os
import pathlib
from typing import Any   # also available: Dict, List, Set
from typing import Dict


class ParseConfigFile:

	def __init__( self, path_to_config_file:str ) -> None:
		"""
		Check if config file exists.  Set bool as appropriate.

		Args:
			path_to_config_file (string): relative or absolute PATH to config file

		"""
		# base-class attributes
		self._dict_config_params:Dict[str,Any] = {}
		self._path_to_config_file:str = path_to_config_file
		self._path_to_log_file:str = ''
		self._subdir_to_log_file:str = ''

		self._lg = None

		# print( f"{__name__} CTOR ({self._path_to_config_file})" )
		if not os.path.isfile( self.path_to_config_file ):
			raise FileExistsError( errno.ENOENT, os.strerror(errno.ENOENT), path_to_config_file )

		configParser = configparser.ConfigParser( allow_no_value=True )
		configParser.read( path_to_config_file )
		for section in configParser.sections():
			self._dict_config_params[section] = {}
			for option in configParser.options( section ):
				self._dict_config_params[section][option] = configParser.get( section, option )

		if( ast.literal_eval( self.get_config_params['common']['print_config_params'] ) ):
			self.print_all_config_parameters()

		# build log-file subdir
		# self._subdir_to_log_file = self.get_config_params['location']['logger_root_dir']
		# self._path_to_log_file = os.path.join(
		# 	self._subdir_to_log_file,
		# 	self.get_config_params['location']['logger_fname'] )
		# print( f"PATH TO LOGGER: {self.path_to_log_file}" )
		# build images subdir


		# Generate the subdir to log file; it must exist for the logging object
		# to be generated.
		# pathlib.Path( self.subdir_to_log_file ).mkdir( parents=True, exist_ok=True )

		# # Configure the logging, build the path
		# ftmp1:str = self.get_config_params['location']['logger_fname']
		# ftmp2:str = ftmp1.replace( 'IMGSZ', self.get_config_params['ml3']['image_size'] )
		# fname:str = ftmp2.replace( 'TASK', self.get_config_params['common']['run_this_task'] )
		# self._path_to_log_file:str = os.path.join( self.subdir_to_log_file, fname )
		# logging.basicConfig(
		# 		filename=self.path_to_log_file,  # Log file name
		# 		filemode='a',  # Write mode ('w' for overwrite, 'a' for append)
		# 		level=logging.DEBUG,  # Set the minimum level of messages to capture
		# 		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log message format
		# )
		# self._lg = logging.getLogger( 'parse-xml' )
		# self.lg.info( '---- START NEW PARSE XML ----' )
		# self.lg.info( f"PATH to this log file: '{self.path_to_log_file}'" )
		# self.lg.info( f"PATH to config file: '{self.path_to_config_file}'" )
		# self.lg.info( f"src_nfract_xml_files: '{self.get_config_params['copyfiles']['src_nfract_xml_files']}'" )
		# self.lg.info( f"xml_copy_subdir: '{self.get_config_params['copyfiles']['xml_copy_subdir']}'" )


	# Getters
	@property
	def path_to_config_file(self):
		return self._path_to_config_file
	@property
	# short name for logging-object
	def lg(self):
		return self._lg
	@property
	def get_config_params(self):
		return self._dict_config_params
	# @property
	# def path_to_log_file(self):
	# 	return self._path_to_log_file
	# @property
	# def subdir_to_log_file(self):
	# 	return self._subdir_to_log_file


	# ---------------------------------------------------------------------------
	# --- Functions -------------------------------------------------------------
	# ---------------------------------------------------------------------------
	def print_all_config_parameters( self ):
		"""
		Print the config params if the ['common']['print_config_params']
		is set to True.
		"""
		# print( f"params: '{self.get_config_params}'" )
		for section, its in self._dict_config_params.items():
			print( f"<><> section: '{section}' (key-pairs below)" )
			for key, val in its.items():
				print( f"     {key} : {val}")

