
import inspect
import math
from typing import List
from typing import Tuple

from assertions import assertions

def ex1_03(self):
	"""Page 18
	Objective: Calculate the drift current density for a given semiconductor.
	Consider silicon at T = 300 K doped with arsenic atoms at a concentration
	of Nd = 8e+15/cm^3 . Assume mobility values of μn = 1350 cm^2/V-sec
	and μp = 480 cm^2/V-sec. Assume the applied electric field is 100 V/cm.
	ANS:  173μA/cm^2
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	ans:float = 173e-06   # μA/cm^2

	# electron concentration
	Nd = 8e+15  # /cm^3
	# hole concentration
	p:float = self.ni_Si_300K**2 / Nd

	# Because of the difference in magnitudes between the two concentrations,
	# the conductivity is given by:
	#   sigma (σ) = (qev * μ_n * n) + (qev * μ_n * n) ~= (qev * μ_n * n) in units (Ω-cm)^-1
	#     where qev = 1.602e-19 = magnitude of the electronic charge, Joules
	u_n:float = 1350   # cm^2/V-sec
	sigma:float = self.qev * u_n * Nd

	try:
		assertions.assert_within_percentage( sigma, 1.73, 3.0 )
		print( f"CALC sigma = {round(sigma,3)}(ohm-cm)^-1 -OR-" )
		print( f"CALC sigma = {round(sigma,3)}/(ohm-cm)" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# drift current density
	E_field:float = 100  # V/cm
	J:float = E_field * sigma

	try:
		assertions.assert_within_percentage( J, 173, 3.0 )
		print( f"CALC J current density = {round(J,3)}A/cm^2" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
