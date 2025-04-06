import ast
# from datetime import datetime
import importlib
from inspect import currentframe
import math
from typing import Any, Dict, List   # also available:  Set, Tuple

from scipy.constants import Boltzmann

from setup import class_setup


class Chap05( class_setup.Setup ):
	"""
	HW problems:  2, 10, 17a and d and then 20, 30, 59a with a Vcc of 20V.

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
	def param_figure_figsize(self):
		return self._param_figure_figsize
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
	# --- Functions: helpers to support all of Chapter 05 ------------------------
	# ----------------------------------------------------------------------------
	def calc_BJT_collector_current( self, IS:float, VBE:float ) -> float:
		"""
		This function implements the theoretical relationship between the current
		and voltage in the collector (junction) of BJT.

		Args:
			IS:float reverse saturation current
			VD:float voltage across base-emitter junction
		
		Return: emitter current
		"""
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# print( f"&&&&& VT: {self.vthrml0_026:.5e}V @ 300Kelvin" )
		ID:float = IS * ( math.exp( VBE / self.vthrml0_026) )
		return ID


	def bjt_collector_IV_characteristic_IC( self, **kwargs ) -> float:
		"""
		When considering the Early voltage (VA), the collector current (IC) in a BJT is affected by the Early effect
		- which accounts for the variation of the collector current with the collector-emitter voltage (VCE).
		The equation to model the collector current considers VBE to be constant.
		Typical values for IS:
		  * Si: 10^-14 to 10^-12 A

		Keyword arguments:
    **kwargs: keyword arguments:
        IS:float reverse saturation current, A
				TK:float temperature, Kelvin
				VA:float Early voltage, V
				VBE:float base-emitter voltage, V
				VCE:float collector-emitter voltage, V
		
		Return: emitter current IC
		"""
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		IS:float = kwargs['IS']
		VT:float = self.thermal_voltage( kwargs['TK'] )
		VA:float = kwargs['VA']
		VBE:float = kwargs['VBE']
		VCE:float = kwargs['VCE']
		print( f"VT: {VT}" )
		IC:float = IS * ( math.exp( VBE / VT) ) * ( 1 + (VCE / VA) )
		return IC


	def bjt_collector_IV_characteristic_IC_list( self, **kwargs ) -> Dict[str,Any]:
		"""
		When considering the Early voltage (VA), the collector current (IC) in a BJT is affected by the Early effect
		- which accounts for the variation of the collector current with the collector-emitter voltage (VCE).
		The equation to model the collector current considers VBE to be constant.
		Typical values for IS:
		  * Si: 10^-14 to 10^-12 A

		Keyword arguments:
    **kwargs: keyword arguments:
        IS:float reverse saturation current, A
				TK:float temperature, Kelvin
				VA:float Early voltage, V
				VBE:float base-emitter voltage, V
				plot_params:List[Any] dictionary of plot params
				plot_params['VCE_max_volts']:float max VCE value
				plot_params['VCE_list_count']:int controls lenght of return list
		Return: emitter current IC
		"""
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# output
		dict_IV:Dict[str,Any] = {}
		IS:float = kwargs['IS']
		VT:float = self.thermal_voltage( kwargs['TK'] )
		VA:float = kwargs['VA']
		VBE:float = kwargs['VBE']
		VCE_max_volts:float = kwargs['plot_params']['VCE_max_volts']
		VCE_list_count:int = kwargs['plot_params']['VCE_list_count']
		print( f"VT: {VT}" )

		step_size:float = (VA + VCE_max_volts) / VCE_list_count

		list_VCE_range:List[float] = [round(-VA + i * step_size, 3) for i in range(VCE_list_count+1)]
		dict_IV['VCE'] = list_VCE_range
		# print( f"list_VCE_range: {list_VCE_range}V" )
		# print( f"len(list_VCE_range): {len(list_VCE_range)}" )

		list_IC:List[float] = []
		for VCE in list_VCE_range:
			list_IC.append( IS * ( math.exp( VBE / VT) ) * ( 1 + (VCE / VA) ) )

		dict_IV['IC'] = list_IC
		# print( f"list_IC: {list_IC}A" )
		# print( f"len(list_IC): {len(list_IC)}" )

		# Calculate ro = run/rise.
		rise:float = list_IC[-1] - list_IC[0]
		ro:float = ( VA + VCE_max_volts ) / rise
		dict_IV['ro'] = ro

		return dict_IV


	def thermal_voltage( self, TK:float=300 ) -> float:
		"""
		round() seems to stop at 6-significant digits: 0.025852.

		Args:
			TK:float temp in Kelvin, default to room temp 300K
		
		Return: thermal voltage
		"""
		# fcn_name:str = currentframe().f_code.co_name
		# print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
		# print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

		# print( f"&&&&& VT: {self.vthrml0_026:.5e}V @ 300Kelvin" )
		vt:float = Boltzmann * TK / self.qev
		# vt:float = round( (Boltzmann * TK / self.qev), 7)
		return vt




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
