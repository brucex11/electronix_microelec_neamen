import ast
# from collections import OrderedDict
# from datetime import datetime
# from typing import Any
from typing import Dict   # also available: Dict, Set
# from typing import Tuple
import math
import os
import importlib
from inspect import currentframe
# import sys
from scipy.constants import Boltzmann

# from pytools import glob_dir
# from parse_config_file import ParseConfigFile
# from pytools import py_file_io
# import class_chap01


class Chap01():
	"""
	Chapter title:  Semiconductor Materials and Diodes
	HW problems:  3, 19, 27

	Functions for critical concepts in this chapter are included as member functions
	in this file.

	For example, section 1.2.4 speaks-to the ideal Current-Voltage relationship
	for a diode when an electric-field (voltage) is applied across the pn junction
	(of said diode).
	See calc_diode_ideal_current(...)

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
		fcn_name:str = currentframe().f_code.co_name
		print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		self._cf = configparams_obj
		self._lg = logger_obj
		# print( f"+++PATH to config file: '{self.cf.path_to_config_file}'" )
		self.lg.info( f"PATH to config file: '{self.cf.path_to_config_file}'" )

		# Pick-up the specific config params
		self.prob:str = self.cf.get_config_params['common']['problem_num']
		# Strip the leading 'p' and replace '_' with '.' for printing purpose only.
		tmps:str = self.prob.lstrip(self.prob[0])
		self._prob_str:str = tmps.replace( '_', '.' )

		self._problem_txt:str = self.cf.get_config_params['common']['problem_txt']
		self._problem_ans:str = self.cf.get_config_params['common']['problem_ans']

		# save figure params
		self._save_figure = ast.literal_eval(
			self.cf.get_config_params['common']['save_figure'] )
		self._save_figure_dir:str = os.path.join(
			self.cf.get_config_params['common']['save_figure_rootdir'],
			self.cf.get_config_params['common']['save_figure_subdir'],
			self.cf.get_config_params['common']['project_title']
		)


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
	def ni_GaAs_300K(self):
		return self._ni_GaAs_300K
	@property
	def ni_Ge_300K(self):
		return self._ni_Ge_300K
	@property
	def ni_Si_300K(self):
		return self._ni_Si_300K
	@property
	def problem_ans(self):
		return self._problem_ans
	@property
	def problem_txt(self):
		return self._problem_txt
	@property
	def prob_str(self):
		return self._prob_str
	@property
	def qev(self):
		return self._qev
	@property
	def save_figure(self):
		return self._save_figure
	@property
	def save_figure_dir(self):
		return self._save_figure_dir
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
	# --- Functions: helpers to support all of Chapter 01 ------------------------
	# ----------------------------------------------------------------------------

	def calc_diode_ideal_current( self, IS:float, VD:float ) -> float:
		"""
		This function implements the theoretical relationship between the current
		and voltage in the pn junction of a diode.

		Args:
			IS:float reverse saturation current
			VD:float voltage across junction
		
		Return: diode drift current
		"""
		fcn_name:str = currentframe().f_code.co_name
		print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		print( f"&&&&& VT: {self.vthrml0_026:.5e}V @ 300Kelvin" )
		ID:float = IS * ( ( math.exp( VD / self.vthrml0_026) ) - 1 )
		return ID


	def calc_diode_ideal_current_complete(
			self, IS:float, VD:float, Tk:float, n:float ) -> float:
		"""
		This function implements the theoretical relationship between the current
		and voltage in the pn junction of a diode.  Requires all variables
		(hence 'complete').
		Calculates the VT thermal voltage based on temp, Boltzmann, and electron
		charge.

		Args:
			IS:float reverse saturation current
			VD:float voltage across junction
			Tk:float temp in Kelvin
			n:float  emission coefficient or ideality factor,
							 and its value is in the range 1 <= n <= 2.
		
		Return: diode drift current
		"""
		fcn_name:str = currentframe().f_code.co_name
		print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		VT:float = ( Boltzmann * Tk ) / self.qev
		print( f"&&&&& VT: {VT:.5e}V @ {round(Tk,4)}Kelvin" )
		ID:float = IS * ( math.exp( VD / VT ) - 1 )
		return ID


	def calc_diode_ideal_voltage( self, IS:float, ID:float ) -> float:
		"""
		This function implements the theoretical relationship between the voltage
		and current in the pn junction of a diode.

		Args:
			IS:float reverse saturation current
			ID:float current through junction
		
		Return: diode voltage VD
		"""
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# VT:float = ( Boltzmann * Tk ) / self.qev
		VT:float = self.vthrml0_026

		# The original equation below
		# ID:float = IS * ( math.exp( VD / VT ) - 1 )
		# See Mathematics for Scientists, Bak, Licchtenberg, page 174 for log-math-rules for division
		# math.log(ID) - math.log(IS) + math.log(1) = (VD /VT)
		VD:float = VT * ( math.log(ID) - math.log(IS) + 0 )   # math.log(1) = 0

		return VD


	# ----------------------------------------------------------------------------
	# --- Dynamic method caller --------------------------------------------------
	# ----------------------------------------------------------------------------
	def run(self):
		"""Call the method per the config.ini file [problem_num]
		"""
		fcn_name:str = currentframe().f_code.co_name
		print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# build the module name starting with this class's name
		class_name:str = self.__class__.__name__
		# convert the camel-case classname to all lowercase
		cllow:str = class_name.lower()
		module_name:str = f"{cllow}.{self.prob}"
		# module_name:str = f"class_{cllow}.{self.prob}"
		method_name:str = f"{self.prob}"
		module = importlib.import_module( module_name )
		method = getattr( module, method_name )
		if callable(method):
			method(self)
		else:
			raise AttributeError( f"Method '{self.prob}' not found" )
