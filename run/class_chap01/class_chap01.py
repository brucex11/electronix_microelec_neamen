
# from collections import OrderedDict
# from datetime import datetime
from typing import Any
from typing import Dict   # also available: Dict, Set
# from typing import Tuple
import os
import pathlib
# import sys
# from tkinter import image_types
import class_chap01.p1_2
from scipy.constants import Boltzmann



# from pytools import glob_dir
from parse_config_file import ParseConfigFile
from pytools import py_file_io
import class_chap01

class Chap01():
	"""

	Args:
		
	"""

	def __init__( self, configparams_obj, logger_obj ) -> None:
		"""
		Call the base-class to parse the config.ini file.
		Prep the log file's PATH.
		Prep the generated output file's PATH.

		Args:
			path_to_config_file : string
				this is passed to the base class for parsing
		"""
		# print( f" BRKPOINT: class: {__name__}; CTOR: {__class__}; method: {self.__init__.__name__}" )
		self._cf = configparams_obj
		self._lg = logger_obj
		print( f"+++PATH to config file: '{self.cf.path_to_config_file}'" )
		self.lg.info( f"PATH to config file: '{self.cf.path_to_config_file}'" )

		# Pick-up the specific config params
		self.prob:str = self.cf.get_config_params['common']['problem_num']
		# Strip the leading 'p' and replace '_' with '.' for printing purpose only.
		tmps:str = self.prob.lstrip(self.prob[0])
		self._prob_str:str = tmps.replace( '_', '.' )

		self._problem_text:str = self.cf.get_config_params['common']['problem_text']
		self._problem_ans:str =  self.cf.get_config_params['common']['problem_ans']


		# Class-level attributes
		# Semiconductor materials constants
		# **B** typically refers to the **empirical constant** used in the expression for the temperature dependence
		# of the intrinsic carrier concentration or other semiconductor properties.
		# **Eg** is the "forbidden" bandgap Energy in electron-volts.
		# An electron–volt is the energy of an electron that has been accelerated through a potential difference of
		# 1 volt, and 1 eV = 1.6e−19 joules.
		self._dict_semicond_mat_consts:Dict = {
			'Si': { 'Eg_ev': 1.1, 'B': 5.23e+15 },
			'Ge': { 'Eg_ev': 0.66, 'B': 1.66e+15 },
			'GaAs': { 'Eg_ev': 1.4, 'B': 2.10e+14 }
		}

		# Initialize constants for all problems
		self._ni:float = 1.5e+10		# intrinsic carrier concentration
		self._qev:float = 1.602176634e-19	# magnitude of the electronic charge, Joules
		self._Tk_300:float = 300  # Kelvin @ room temp
		self.vthermal:float = Boltzmann * self.Tk_300 / self.qev
		self.vthrml0_025852:float = round(self.vthermal,6)
		self.vthrml0_026:float = round(self.vthermal,3)
		self.boltzmann_ev:float = Boltzmann / self.qev


		# See doc/help/call_class_method_by_string_name.txt.
		method = getattr(self, self.prob, None)
		if callable(method):
			method()
		else:
			raise AttributeError( f"Method '{self.prob}' not found" )

		# rsp = input( 'yes if ok, else press <Enter>' )
		# if rsp != 'yes':
		# 	print( 'QUIT' )
		# 	exit()

	# ---------------------------------------------------------------------------
	# --- Getters ---------------------------------------------------------------
	# ---------------------------------------------------------------------------
	@property
	def cf(self):
		return self._cf
	@property
	# short name for logging-object
	def lg(self):
		return self._lg

	@property
	def dict_semicond_mat_consts(self):
		return self._dict_semicond_mat_consts
	@property
	def problem_ans(self):
		return self._problem_ans
	@property
	def problem_text(self):
		return self._problem_text
	@property
	def prob_str(self):
		return self._prob_str
	@property
	def qev(self):
		return self._qev
	@property
	def Tk_300(self):
		return self._Tk_300





	def p1_1(self):
		"""
		"""
		print( f"p1_1------------------{Chap01.__name__}" )
		# print( f"{Chap01.__name__} : Problem {self.prob_str}" )
		from class_chap01.p1_1 import p1_1
		p1_1(self)


	def p1_2(self):
		"""
		"""
		print( f"{Chap01.__name__} : Problem {self.prob_str}" )
		from class_chap01.p1_2 import p1_2
		p1_2(self)


	def run(self):
		"""Call the method per the config.ini file [problem_num]
		"""
		print( f"RUN" )
		opera:str = self.cf.get_config_params['common']['problem_num']

		# Retrieve the command-line subcommand as this is the "operation" to perform.
		# This is the implementation of the source-code's design.
#		class_name:str = parse_cmd_line.opera
		# Convert the camel-case classname to all lowercase.
		cllow:str = 'chap01'  #class_name.lower()
		# Generate the module name as below; again, this is per project architecture
		# module-by-subdir and source-code fnames.
		module_name:str = f"class_{cllow}"
		# Retrieve the module's reference per its name:str
		module_ref = globals()[module_name]
		print( f"&&&module_ref: '{module_ref}'" )
		# Retrieve the class reference from the module
#		class_ref = getattr( module_ref, class_name )




		# opera:str = self.cf.get_config_params['common']['run_this_task']

		# method = getattr( self, opera, None )
		# if callable(method):
		# 	method()
		# else:
		# 	raise AttributeError( f"Method '{opera}' not in '{__class__}'.")

