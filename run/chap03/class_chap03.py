import ast
# from collections import OrderedDict
# from datetime import datetime
from typing import Dict, List   # also available: Any, Set, Tuple
import importlib
from inspect import currentframe
from math import sqrt
from scipy.constants import Boltzmann

from setup import class_setup


class Chap03( class_setup.Setup ):
	"""
	HW problems:  2A: 3, 5, 13, 16
	HW problems:  2B: 19, 22a and b, 30, 34, 41, 45

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
	def save_figure(self):
		return self._save_figure
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
	# --- Functions: helpers to support all of Chapter 03 ------------------------
	# ----------------------------------------------------------------------------

	def angstroms_per_meter( self, angstroms:float, units:str ) -> float:
		"""
		Args:
			angstroms:float to convert
			units:str 'm' for meters, 'cm' for centimeters
		Return:
			units value: float
		"""
		# Units conversion factor
		Angstroms_per_meter:float = 1e+10
		if( units == 'm' ):
			return angstroms / Angstroms_per_meter
		elif( units == 'cm' ):
			cm_per_meter:float = 100
			return angstroms / Angstroms_per_meter * cm_per_meter

		return -1

	def calc_iDS_for_NMOS_enhancement_in_saturation(
			self, Kn_sat:float, vGS:float, VTN:float ) -> float:
		"""
		Calculate saturated drain current for n-channel/p-substrate MOSFET
		in enhancement mode.

		Args:
			Kn_sat:float (trans)conduction parameter, A/V^2
			vGS:float gate-to-source voltage, V, positive by convention
			VTN:float gate threshold voltage, V, positive by convention
		Return:
			current:float
		"""
		return Kn_sat * (vGS - VTN)**2


	def calc_iDS_for_NMOS_enhancement_in_nonsaturation(
			self, Kn_nonsat:float, vGS:float, VTN:float, vDS:float ) -> float:
		"""
		Calculate non-saturated drain current for n-channel/p-substrate MOSFET
		in enhancement mode.

		Args:
			Kn_nonsat:float (trans)conduction parameter, A/V^2
			vGS:float gate-to-source voltage, V, positive by convention
			VTN:float gate threshold voltage, V, positive by convention
			vDS:float drain-to-source voltage, V, positive by convention
		Return:
			current:float
		"""
		return Kn_nonsat * ( 2 * (vGS - VTN) * vDS - vDS**2 )


	def calc_iDS_for_PMOS_enhancement_in_saturation(
			self, Kp_sat:float, vSG:float, VTP:float ) -> float:
		"""
		Calculate saturated drain current for p-channel/n-substrate MOSFET
		in enhancement mode.

		Args:
			Kp_sat:float (trans)conduction parameter, A/V^2
			vSG:float gate-to-source voltage, V, positive by convention
			VTP:float gate threshold voltage, V, negative by convention
		Return:
			current:float
		"""
		return Kp_sat * (vSG + VTP)**2


	def calc_iDS_for_PMOS_enhancement_in_nonsaturation(
			self, Kp_nonsat:float, vSG:float, VTP:float, vSD:float ) -> float:
		"""
		Calculate non-saturated drain current for p-channel/n-substrate MOSFET
		in enhancement mode.

		Args:
			Kp_nonsat:float (trans)conduction parameter, A/V^2
			vSG:float gate-to-source voltage, V, positive by convention
			VTP:float gate threshold voltage, V, negative by convention
			vSD:float drain-to-source voltage, V, positive by convention
		Return:
			current:float
		"""
		return Kp_nonsat * ( 2 * (vSG + VTP) * vSD - vSD**2 )


	def calc_MOSFET_IV_ohmic_curve_given_VGS( self, **kwargs ) -> List[float]:
		"""
		Pg 141 Table 3.1:
		Depending on channel-type, NMOS or PMOS, calc the:
		* Transition point VDS @ saturation, V
		* Saturation point: (VDS, IDS)
			- this is where slope of IV-curve = zero
			- value:
				* iDS(sat) = max-value in iDS-curve
				* VDS = x_VDS_range[ index @ iDS(sat) ]
				* plot-coordinates index: index @ iDS(sat)

		Keyword arguments:
    **kwargs: keyword arguments:
        VGS:float gate-Source voltage, V
				VTN:float threshold voltage, V
        Kn:float device conduction param, A/V^2
				x_VDS_range:List[float] range of VDS, 0 to some-max-val
		Return:
			List of iDS, A
		"""
		VGS:float = kwargs['VGS']  # V
		VTN:float = kwargs['VTN']  # V
		vDS_sat:float = VGS - VTN  # V
		Kn:float = kwargs['Kn']

		calc_curve:List[float] = []

		for vDS in kwargs['x_VDS_range']:
			i:float = Kn * ( 2 * vDS_sat * vDS - vDS**2 )
			calc_curve.append( i )

		return calc_curve

		
	def calc_MOSFET_K_conduction_parameter( self, **kwargs ) -> float:
		"""
		Pg 133:
		The conduction parameter `(Kn | Kp)` is a function of both
		`electrical` and `geometric parameters`:
  		- the `electrical` oxide capacitance and carrier mobility are essentially
    		constants for a given fabrication technology, and
  		- the `geometry`, or width-to-length ratio W/L, is a variable in the MOSFET's
    		structure/footprint.

		Pg 139:
		The current-voltage characteristics defined by Equations (3.2(a)) and (3.2(b))
		apply to both enhancement- and depletion-mode n-channel devices.

		Note that all 'unit-' dimensions must be the same, eg, all must be centimeter.
		Again, see pg 133 and example 3.1 page 134.

		Keyword arguments:
    **kwargs: keyword arguments:
        W:float channel width, unit-length
        L:float channel length, unit-length
				un:float mobility of majority-carriers in the inversion layer
				eox:float oxide permittivity, Farads/unit-area
				tox:float oxide thickness, same units as eox
		Return:
			Kn or Kp:float - conduction parameter, A/V^2
		"""
		W = kwargs['channel_width']
		L = kwargs['channel_length']
		un = kwargs['carrier_mobility']
		eox = kwargs['oxide_permittivity']
		tox = kwargs['oxide_thickness']

		Cox:float = self.calc_MOSFET_oxide_capacitance( eox=eox, tox=tox )

		return ( W * un * Cox ) / ( 2 * L )
		# return ( W * un * eox ) / ( 2 * L * tox )


	def calc_MOSFET_oxide_capacitance( self, eox:float, tox:float ) -> float:
		"""
		Calculate MOSFET oxide capacitance per unit area.
		Note that eox and tox must have same "length" units, eg, centimeter

		Args:
			eox:float oxide permittivity, Farads/unit-area
			tox:float oxide thickness, same units as eox
		Return:
			Cox:float - oxide capacitance per unit area
		"""
		return eox/tox


	def calc_quadratic_roots( self, coeffs:List[float], roots:List[float] ) -> bool:
		"""
		Given coefficients a, b, c, get the roots.

		Args:
			coeffs:List[float] contains [ a, b, c ]
			roots:List[float] the calulated-roots (reference)

		Return:
			True if discriminant >= 0, False otherwise
		"""
		not_complex:bool = True
		a:float = coeffs[0]
		b:float = coeffs[1]
		c:float = coeffs[2]

		discriminant:float = b**2 - ( 4 * a * c )
		if( discriminant < 0 ):
			not_complex = False
			return not_complex

		xPosRoot:float = ( -b + sqrt(discriminant) ) / ( 2.0 * a )
		xNegRoot:float = ( -b - sqrt(discriminant) ) / ( 2.0 * a )
		roots.extend( [xPosRoot, xNegRoot] )

		return not_complex



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
