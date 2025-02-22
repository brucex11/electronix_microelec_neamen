
from inspect import currentframe
import math
from typing import List
from typing import Tuple

from assertions import assertions

def exer1_02(self):
	"""
	(a) Calculate the majority and minority carrier concentrations in Si at
	T = 300 K for (i) Nd = 2e+16/cm^3 and (ii) Na = 1e+15/cm^3.
	(b) Calculate the majority and minority carrier concentrations in GaAs at
	T = 300 K for (i) Nd = 2e+16/cm^3 and (ii) Na = 1e+15/cm^3.
	Comment: In an n-type semiconductor, electrons are called the majority carrier
	because they far outnumber the holes, (therefore holes are termed the minority
	carrier).  In contrast, in a p-type semiconductor, the holes are the majority
	carrier and the electrons are the minority carrier.
	ANS (a)(i)  no = 2e+16/cm^3, po = 1.125e+04/cm^3
	ANS (a)(ii) po = 1e+15/cm^3, no = 2.25e+05/cm^3
	ANS (b)(i)  no = 2e+16/cm^3, po = 1.625e-04/cm^3
	ANS (a)(ii) po = 1e+15/cm^3, no = 3.24e-04/cm^3
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	tolerance_percent:float = 5.0  # assertion accuracy
	print( '-----------------------------------------------' )

	carrier_concentration:List[float] = []
	# At 300K, the Si intrinsic carrier concentration is 1.5e+10/cm^3.
	ni_Si:float = self.ni_Si_300K

	print( '--- (a)(i) Si ---' )
	ans_ai:Tuple = ( 2e+16, 1.125e+04 )  # per cm^3
	Nd:float = 2e+16
	print( f"CALC (a)(i): Since Nd >> ni, no ~= {Nd:.3e}/cm^3" )
	carrier_concentration.append( Nd )  # for assertion

	po:float = ni_Si**2 / Nd
	carrier_concentration.append( po )  # for assertion

	for idx, ans in enumerate(ans_ai):
		try:
			assertions.assert_within_percentage( carrier_concentration[idx], ans, tolerance_percent )
			print( f"CALC carrier concentration: {carrier_concentration[idx]:.3e} is within {tolerance_percent}% of accepted answer." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	carrier_concentration.clear()  # for next assertions

	print( '--- (a)(ii) Si ---' )
	ans_aii:Tuple = ( 1e+15, 2.25e+05 )  # per cm^3
	Na:float = 1e+15  # per cm^3
	print( f"CALC (a)(ii): Since Na >> ni, po ~= {Na:.3e}/cm^3" )
	carrier_concentration.append( Na )  # for assertion

	no:float = ni_Si**2 / Na
	carrier_concentration.append( no )

	for idx, ans in enumerate(ans_aii):
		try:
			assertions.assert_within_percentage( carrier_concentration[idx], ans, tolerance_percent )
			print( f"CALC carrier concentration: {carrier_concentration[idx]:.3e} is within {tolerance_percent}% of accepted answer." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	carrier_concentration.clear()  # for next assertions


	# At 300K, the GaAs intrinsic carrier concentration must be calculated.
	temp:float = 300  # Kelvin

	B:float = self.dict_semicond_mat_consts['GaAs']['B']
	ni_GaAs:float = B * ( temp ** (3/2) ) \
			* math.exp( -1.0 * self.dict_semicond_mat_consts['GaAs']['Eg_ev'] / (2 * self.boltzmann_ev * temp) )

	print( '\n--- (b)(i) GaAs ---' )
	print( f"--- For (b) ni for GaAs @300K = {ni_GaAs:.3e}/cm^3" )
	ans_bi:Tuple = ( 2e+16, 1.625e-04 )  # per cm^3

	#  Recall that Nd:float = 2e+16
	print( f"CALC (b)(i): Since Nd >> ni, no ~= {Nd:.3e}/cm^3" )
	carrier_concentration.append( Nd )

	po = ni_GaAs**2 / Nd
	carrier_concentration.append( po )

	for idx, ans in enumerate(ans_bi):
		try:
			assertions.assert_within_percentage( carrier_concentration[idx], ans, tolerance_percent )
			print( f"CALC carrier concentration: {carrier_concentration[idx]:.3e} is within {tolerance_percent}% of accepted answer." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )

	carrier_concentration.clear()  # for last assertions

	print( '--- (b)(ii) GaAs ---' )
	ans_bii:Tuple = ( 1e+15, 3.24e-03 )  # per cm^3
	# Na:float = 1e+15  # per cm^3
	print( f"CALC (b)(ii): Since Na >> ni, po ~= {Na:.3e}/cm^3" )
	carrier_concentration.append( Na )  # for assertion

	no = ni_GaAs**2 / Na
	carrier_concentration.append( no )

	for idx, ans in enumerate(ans_bii):
		try:
			assertions.assert_within_percentage( carrier_concentration[idx], ans, tolerance_percent )
			print( f"CALC carrier concentration: {carrier_concentration[idx]:.3e} is within {tolerance_percent}% of accepted answer." )
		except AssertionError as e:
			print( f"CALC AssertionError {pnum}: {e}" )
