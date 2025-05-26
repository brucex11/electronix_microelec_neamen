
from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from chap03 import class_chap03 as ch3

def exer3_02(self):
	"""Page 137:
	A PMOS device with VTP = -1.2V has a drain current iD = 0.5mA
	when vSG = 3V and vSD = 5V. Calculate the drain current when
	(a) vSG = 2V, vSD = 3V;
	(b) vSG = 5V, vSD = 2V.
	ANS (a) 0.0986mA  (b) 1.72mA.
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

	ans_a:float = 0.0986e-03   # A
	ans_b:float = 1.72e-03     # A

	# Givens
	VTP:float = -1.2     # V
	iDS_given:float = 0.5e-03  # A
	vSG_given:float = 3        # V
	vSD_given:float = 5        # V

	vSD_sat:float = vSG_given + VTP
	Kp_sat:float = iDS_given / ( vSG_given + VTP )**2

	# --- (a) ---
	vSG_a:float = 2   # V
	vSD_a:float = 3   # V

	iSD_sat:float =\
		ch3.Chap03.calc_iDS_for_PMOS_enhancement_in_saturation(
		self, Kp_sat=Kp_sat, vSG=vSG_a, VTP=VTP
	)
	iSD_sat = round(iSD_sat, 8)

	ans_string:str = f"""
---- (determine region of operation) ----
Region of operation is driven by Gate voltage vSG and Drain voltage vSD.

MOSFET enters saturation-region when:
 * the Gate-voltage exceeds the threshold turn-ON voltage VTP
 -AND-
 * vSD > vSG + VTP.

Therefore, vSD(sat) = vSG + VTP  -AND-  vSD(sat) is a function of vSG.

For the given MOSFET, VTP = {VTP}V.
When vSG = {vSG_given}V and vSD = {vSD_given}V:

  vSD(sat) = {vSG_given} + {VTP} = {vSD_sat}V.
  Since vSD is {vSD_given}V, MOSFET is biased
  in the saturation region.

Calculate Kp using the saturation-region equation for iD.

  Kp = iSD / ( vSG - VTP )**2
     = {iDS_given} / ( {vSG_given} + {VTP} )**2
  Kp = {Kp_sat}A/V^2.

--- a) vSG = {vSG_a}V, vSD = {vSD_a}V ---
  vSD(sat) = 3 + (-1.2) = 1.8V, and since vSD = 5V > 1.8V, in saturation.

  iSD = Kp * (vSG + VTP)**2
      = {Kp_sat} * ({vSG_a} + {VTP})**2
  iSD = {iSD_sat}A.
"""
	print( ans_string )


	# --- (b) --------------------------------------------------------------------
	vSG_b:float = 5   # V
	vSD_b:float = 2   # V

	iSD_b:float = ch3.Chap03.calc_iDS_for_PMOS_enhancement_in_nonsaturation(
		self, Kp_nonsat=Kp_sat, vSG=vSG_b, VTP=VTP, vSD=vSD_b
	)

	ans_string = f"""
--- b) vSG = {vSG_b}V, vSD = {vSD_b}V ---
  vSD(sat) = {vSG_b} + ({VTP}) = 3.8V, and since vSD = {vSD_b}V < 3.8V, in ohmic.

  iSD = Kp * ( 2 * (vSG + VTP) * vSD - vSD**2 )
      = {Kp_sat} * ( 2 * ({vSG_b} + {VTP}) * {vSD_b} - {vSD_b}**2 )
  iSD = {iSD_b}A.
"""
	print( ans_string )

	try:
		assert_within_percentage( iSD_b, ans_b, assert_percentage )
		print( f"CALC PMOS enhancement mode in non-saturation: iSD = {round(iSD_b,5)}A", end=' ' )
		print( f"is within {assert_percentage}% of accepted answer {ans_b}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
