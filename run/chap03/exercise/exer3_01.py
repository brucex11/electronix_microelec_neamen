
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from chap03 import class_chap03 as ch3

def exer3_01(self):
	"""Page 134:
	An NMOS transistor with VTN = 1V has a drain current iD = 0.8mA
	when vGS = 3V and vDS = 4.5V.  Calculate the drain current when:
	a) vGS = 2V, vDS = 4.5V; and (b) vGS = 3V, vDS = 1V.

	Solution: Solve for Kn conduction parameter per equations 3.2a and 3.2b,
	then solve for drain current given vGS and vDS.

	Assuming operation in nonsaturation region where vDS < vDS(sat), use eq 3.2a.
	Assuming operation in saturation region where vGS > VTN, use eq 3.2b.

	ANS  (a) 0.2mA  (b) 0.6mA.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 1.0
	print( '-----------------------------------------------' )

	ans_a:float = 0.2e-03   # A
	ans_b:float = 0.6e-03   # A

	VTN:float = 1.0     # V
	iDS_given:float = 0.8e-03   # 0.8mA
	vGS_given:float = 3     # V
	vDS_given:float = 4.5   # V

	# --- calcs ---
	Kn_sat:float = iDS_given /  ( vGS_given - VTN )**2

	vGS:float = 2
	iDS_sat:float =\
		ch3.Chap03.calc_iDS_for_NMOS_enhancement_in_saturation(
		self, Kn_sat=Kn_sat, vGS=vGS, VTN=VTN
	)
	iDS_sat = round(iDS_sat, 4)

	ans_string:str = f"""
---- (determine region of operation) ----
Region of operation is driven by Gate voltage vGS and Drain voltage vDS.

MOSFET enters saturation-region when:
 * the Gate-voltage exceeds the threshold turn-ON voltage VTN
 -AND-
 * vDS > vGS - VTN.

Therefore,  vDS(sat) = vGS - VTN  -AND-  vDS(sat) is a function of vGS.

For the given MOSFET, VTN = 1V.
When vGS = 3V and vDS = 4.5V:

  vDS(sat) = 3 - 1 = 2V.  Since vDS is 4.5V, MOSFET is biased
  in the saturation region.

Calculate Kn using the saturation-region equation for iD.

  Kn = iDS / ( vGS - VTN )**2
     = {iDS_given} / ( {vGS_given} - {VTN} )**2
  Kn = {Kn_sat}A/V^2.

--- a) vGS = 2V, vDS = 4.5V ---
  vDS(sat) = 2 - 1 = 1V, and since vDS = 4.5V > 1V, in saturation.

  Since iD per the I-V characteristic in saturation has zero-slope,
    iD(sat) = .0002A

Double-check the Chap03 class method (and do the calculation anyway):

  iDS = Kn * (vGS - VTN)**2
      = {Kn_sat} * ({vGS} - {VTN})**2
  iDS = {iDS_sat}A.
"""
	print( ans_string )

	vGS:float = 3
	vDS:float = 1
	# EQUATION for iDS_in_NONsaturation
	# iDS_nonsat:float = Kn_sat * ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 )
	iDS_nonsat:float =\
		ch3.Chap03.calc_iDS_for_NMOS_enhancement_in_nonsaturation(
		self, Kn_nonsat=Kn_sat, vGS=vGS, VTN=VTN, vDS=vDS
	)
	iDS_nonsat = round(iDS_nonsat, 4)

	ans_string:str = f"""
--- b) vGS = 3V, vDS = 1V ----
  vDS(sat) = 3 - 1 = 2V, and since vDS = 1V < 2V, in non-saturation.

Calculate Kn using the nonsaturation-region equation for iD.

  iDS = Kn * ( ( 2 * (vGS - VTN ) * vDS ) - vDS**2 ) 
      = {Kn_sat} * ( ( 2 * ({vGS} - {VTN} ) * {vDS} ) - {vDS}**2 )
  iDS(ohmic) = {iDS_nonsat}A.
"""
	print( ans_string )

	try:
		assert_within_percentage( iDS_nonsat, ans_b, assert_percentage )
		print( f"CALC NMOS ohmic iDS = {round(iDS_nonsat, 4)}A is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
