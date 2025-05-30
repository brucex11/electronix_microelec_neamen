import ast
# from datetime import datetime
from typing import Dict   # also available: Any, List, Set, Tuple
import importlib
from inspect import currentframe
from math import pi
from scipy.constants import Boltzmann

from setup import class_setup


class Chap07( class_setup.Setup ):
	"""
	HW problems:  low frequency response: 17, 21, 31, and 52.
	HW problems:  high frequency response: 52 part ), first two blitz circuits
								per ./docx/chap07/Blitz_Sophia_Freq_response_schematics.pdf
	Args:

	"""

	def __init__( self, path_config_file:str ) -> None:
		"""
		Call the base-class to parse the config.ini file.
		Prep the log file's PATH.
		Prep the generated output file's PATH.

		Args:
			path_to_config_file : string
				this is passed to the base class for parsing
		"""
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		super().__init__( path_config_file )


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
		self._ni_Si_300K:float = 1.5e+10		# Si intrinsic carrier concentration @ 300K
		self._ni_Ge_300K:float = 2.466e+13	# Ge intrinsic carrier concentration @ 300K
		self._ni_GaAs_300K:float = 1.899e+06	# GaAs intrinsic carrier concentration @ 300K
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

		# exez.exer2_01.exer2_01(self)

	# ----------------------------------------------------------------------------
	# --- Getters ----------------------------------------------------------------
	# ----------------------------------------------------------------------------
	@property
	def boltzmann_ev(self):
		return self._boltzmann_ev
	@property
	def dict_semicond_mat_consts(self):
		return self._dict_semicond_mat_consts
	@property
	def ni_GaAs_300K(self):
		return self._ni_GaAs_300K
	@property
	def ni_Ge_300K(self):
		return self._ni_Ge_300K
	@property
	def ni_Si_300K(self):
		return self._ni_Si_300K
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
	# --- Functions: helpers to support all of Chapter 07 ------------------------
	# ----------------------------------------------------------------------------
	def beta_cutoff_freq( self, rπ:float, Cπ:float, Cμ:float ) -> float:
		"""
		Calc 3dB corner-frequency of the short-circuit current gain for BJT.
		Args:
			rπ : forward-biased junction diffusion-resistance
			Cπ  : forward-biased B-E junction capacitance
			Cμ  : reverse-biased B'-C' junction capacitance
		
		Return: beta cutoff frequency that is 3dB corner-freq
		"""
		fb:float = 1 / ( 2 * pi * rπ * ( Cπ + Cμ) )
		return fb

	def calc_gm( self, ICQ:float) -> float:
		"""
		Args:
			ICQ: Q-point collector current
		
		Return: BJT transconductance A/V
		"""
		gm:float = ICQ / self._vthrml0_026
		gm = round(gm,6)
		return gm

	def calc_rpi( self, IBQ:float) -> float:
		"""
		Args:
			IBQ: Q-point base current
		
		Return: BJT VBE resistance
		"""
		rpi:float = self._vthrml0_026 / IBQ
		rpi = round(rpi,0)
		return rpi


	# ----------------------------------------------------------------------------
	# --- Dynamic method caller --------------------------------------------------
	# ----------------------------------------------------------------------------
	def run_in_dir(self):
		"""Call the method per the config.ini file [problem_num] WHEN THE MODULE
			 (OR .PY FILENAME) IS IN THE SAME SUBDIR AS THIS MODULE/.PY FILE.
		"""
		fcn_name:str = currentframe().f_code.co_name
		print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# build the module name starting with this class's name
		class_name:str = self.__class__.__name__
		# convert the camel-case classname to all lowercase
		cllow:str = class_name.lower()
		# module_name:str = f"class_{cllow}.{self.prob}"
		module_name:str = f"{cllow}.{self.prob}"
		method_name:str = f"{self.prob}"
		module = importlib.import_module( module_name )
		method = getattr( module, method_name )
		if callable(method):
			method(self)
		else:
			raise AttributeError( f"Method '{self.prob}' not found" )


	def run_in_subdir(self):
		"""Call the method per the config.ini file [problem_num]
		"""
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# # Example to retrieve all modules
		# global_variables = globals()
		# # Filter out modules that start with '__' and are instances of types like 'sys' (modules)
		# modules = {name: obj for name, obj in global_variables.items() if isinstance(obj, type(sys)) and not name.startswith('__')}
		# # List of module names
		# module_names = list(modules.keys())
		# print( f">>>>>>>>>>>>>>>>>>>{currentframe().f_code.co_name}-module_names: {module_names}" )

		# Build the FULL module name in req'd format: class-name.subdir-name.python-fname
		#   where:
		#      class-name:   contains all lower-case chars,
		#      subdir-name:  is picked up from the config.ini file,
		#      python-fname: is aka a python "module" without the .py extension,
		#                    and is also picked up from the config.ini file.
		# this class's name
		class_tmp:str = self.__class__.__name__
		# print( f"class_name: {class_tmp}" )
		# convert the camel-case classname to all lowercase
		class_name:str = class_tmp.lower()
		subdir_name:str = self.subdir_name
		py_fname_sans_extension:str = self.prob
		# build the FULL module name
		module_name:str = f"{class_name}.{subdir_name}.{py_fname_sans_extension}"
		# use the module-name string to import the desired module
		module = importlib.import_module( module_name )
		# finally, grab the function-name in the module
		method = getattr( module, py_fname_sans_extension )
		if callable(method):
			method(self)
		else:
			raise AttributeError( f"Method '{self.prob}' not found" )

		# 22Feb25:
		# TBD that the py-files that contain the calculations-code do NOT
		# necessarily need to be inside a (def:) method/function.
		# If so, then the 'getattr' call above may be eliminated.
