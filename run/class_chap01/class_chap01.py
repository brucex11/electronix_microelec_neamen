
# from collections import OrderedDict
# from datetime import datetime
from typing import Any
from typing import Dict   # also available: Dict, Set
# from typing import Tuple
import os
import importlib
# import sys
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
		# print( f"+++PATH to config file: '{self.cf.path_to_config_file}'" )
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
		self._vthermal:float = Boltzmann * self.Tk_300 / self.qev
		self._vthrml0_025852:float = round(self.vthermal,6)
		self._vthrml0_026:float = round(self.vthermal,3)
		self._boltzmann_ev:float = Boltzmann / self.qev

		# rsp = input( 'yes if ok, else press <Enter>' )
		# if rsp != 'yes':
		# 	print( 'QUIT' )
		# 	exit()

	# ----------------------------------------------------------------------------
	# --- Getters ----------------------------------------------------------------
	# ----------------------------------------------------------------------------
	@property
	def cf(self):
		return self._cf
	@property
	# short name for logging-object
	def lg(self):
		return self._lg

	@property
	def boltzmann_ev(self):
		return self._boltzmann_ev
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
	@property
	def vthermal(self):
		return self._vthermal
	@property
	def vthrml0_025852(self):
		return self._vthrml0_025852
	@property
	def vthrml0_026(self):
		return self._vthrml0_026


	# ----------------------------------------------------------------------------
	# --- Functions --------------------------------------------------------------
	# ----------------------------------------------------------------------------
	def run(self):
		"""Call the method per the config.ini file [problem_num]
		"""
		# build the module name starting with this class's name
		class_name:str = self.__class__.__name__
		# convert the camel-case classname to all lowercase
		cllow:str = class_name.lower()
		module_name:str = f"class_{cllow}.{self.prob}"
		method_name:str = f"{self.prob}"
		module = importlib.import_module( module_name )
		method = getattr( module, method_name )
		if callable(method):
			method(self)
		else:
			raise AttributeError( f"Method '{self.prob}' not found" )
