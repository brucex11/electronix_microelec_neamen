
from inspect import currentframe
from  math import sqrt
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_46(self):
	"""Page 200:
	The transistors in the circuit in Figure P3.46 both have parameters
	VTN = 0.4V and k'n = 120μA/V^2. (a) If the width-to-length ratios of M1
	and M2 are (W/L)1 = (W/L)2 = 30, determine VGS1, VGS2, Vo, and ID.
	(b) Repeat part (a) if the width-to-length ratios are changed to (W/L)1 = 30
	and (W/L)2 = 15. (c) Repeat part (a) if the width-to-length ratios are
	changed to (W/L)1 = 15 and (W/L)2 = 30.

	ANS(a) for (W/L)1 = (W/L)2 = 30: VGS1 = VGS2 = Vo = 2.5V, ID(sat) = 7.938mA
	ANS(b) for (W/L)1 = 30, (W/L)2 = 15: VGS1 = 2.14V, VGS2 = Vo = 2.86V, ID(sat) = 5.45mA
	ANS(c) for (W/L)1 = 15, (W/L)2 = 30: VGS1 = 2.86V, VGS2 = Vo = 2.14V, ID(sat) = 5.45mA
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.5
	print( '-----------------------------------------------' )

	# ---- Givens --------------------
	VDD:float = 5     # V
	VTN:float = 0.4   # V
	k_prime_n:float = 120e-06   # A/V^2


	# ---- (a) -----------------------
	WoverL_M1M2_equal:float = 30

	ans_iDa:float = 7.938e-03   # A

	# ---- (b) -----------------------
	WoverL_M1b:float = 30
	WoverL_M2b:float = 15

	# ---- (c) -----------------------
	WoverL_M1c:float = 15
	WoverL_M2c:float = 30

	ans_string:str = """
The devices per schematic symbol are n-channel enhancement-mode.
By inspection:
  M1:  VGS = VDS = VDD - Vo
  M2:  VGS = VDS = Vo
  Since M1 and M2 are in series, the current ID is same through each.

For an n-channel enhancement-mode MOSFET, when VGS = VDS, the MOSFET operates
in the saturation-region:

  1. Threshold Voltage (VTN): For the MOSFET to be ON (conducting), the
     gate-to-source voltage VGS must be greater than the threshold voltage VTN.
     This ensures that a conducting channel forms between the drain and the source.

  2. Region of Operation:
    - Cutoff:  When VGS < VTN, the MOSFET is OFF, and there is no conduction.
    - Linear (Ohmic/Triode):  When VGS > VTN and VDS < (VGS - VTN), the MOSFET
      operates in the ohmic region.  In this region, the MOSFET behaves like
      a variable resistor.
    - Saturation:  When VGS > VTN and VDS >= (VGS - VTN), the MOSFET is in
      the saturation region.  In this region, the drain current is primarily
      controlled by VGS and is relatively independent of VDS (as long as VDS
      is above the threshold).

In this case, when VGS = VDS, the MOSFET satisfies the condition for the
saturation region, where VDS >= (VGS - VTN).  Therefore, the MOSFET is in the
saturation region at VGS = VDS.

Per the schematic, M1 and M2 in series, therefore iD is same through both.
"""
	print( ans_string )

	ans_string = """---- (a (W/L)1 = (W/L)2 = 30) -------------------------------------
             iD M1 = iD M2
Kn( VGS1 - VTN )^2 = Kn( VGS2 - VTN )^2
In equation above, since Kn and VTN are same, the MOSFETs are "matched,"
and these two terms cancel."""
	print( ans_string )
	calc_Vo:float = VDD / 2
	print( f"VGS1 = VDD - Vo = {VDD} - Vo = VGS2" )
	print( f"ANS:  Vo = VDD/2 = {calc_Vo}V" )
	print( f"It follows that VGS1 = VGS2 = Vo = {calc_Vo}V" )

	print( "Calc iD in saturation: = (k'n/2) * ( W/L ) * ( Vo - VTN )**2" )
	calc_ID_sat:float = (k_prime_n/2) * (WoverL_M1M2_equal ) * ( calc_Vo - VTN )**2

	try:
		assertions.assert_within_percentage( calc_ID_sat, ans_iDa, assert_percentage )
		print( f"CALC M1, M2 current ID(sat) = {calc_ID_sat:.3e}A", end=' ' )
		print( f"is within {assert_percentage}% of accepted answer." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	ans_string = """
---- (b (W/L)1 = 30, (W/L)2 = 15) ----------------------------------------------
              iD M1 = iD M2
Kn1( VGS1 - VTN )^2 = Kn2( VGS2 - VTN )^2
M1 and M2 are not matched since their (W/L) differ.

Kn1 = (k'n/2)((W/L)1)
Kn2 = (k'n/2)((W/L)2)

Also, VDD - VGS1 - VGS2 = 0 -OR- VGS2 = VDD - VGS1.

Substitute VGS2 with above, solve for VGS1 by equating the current in saturation:

  Kn1(VGS1 - VTN)^2 = Kn2(VDD - VGS1 - VTN)^2
"""
	print( ans_string )

	Kn1:float = (k_prime_n/2 )*(WoverL_M1b)
	Kn2:float = (k_prime_n/2 )*(WoverL_M2b)
	print( f"Kn1 = {Kn1}" )
	print( f"Kn2 = {Kn2}" )

	z:float = Kn1 / Kn2
	print( f"Let z = Kn1 / Kn2 = {z}" )

	calc_VGS1:float = ( VDD - VTN + sqrt(z)*VTN ) / (sqrt(z) + 1)
	calc_VGS1 = round(calc_VGS1,2)
	print( f"VGS1 = {calc_VGS1}V" )
	calc_Vo:float = VDD - calc_VGS1
	calc_VGS2:float = calc_Vo
	print( f"Vo = VGS2 = VDD - VGS1 {calc_Vo}V" )

	print( 'Next, solve for ID(sat) for each MOSFET to confirm they are equal.' )

	calc_ID1:float = Kn1 * ( calc_VGS1 - VTN )**2
	calc_ID1 = round(calc_ID1,5)
	print( f"ID1(sat) = Kn1 * ( calc_VGS1 - VTN )^2 = {calc_ID1*1000}mA")

	calc_ID2:float = Kn2 * ( calc_VGS2 - VTN )**2
	calc_ID2 = round(calc_ID2,5)
	print( f"ID2(sat) = Kn1 * ( calc_VGS2 - VTN )^2 = {calc_ID2*1000}mA")



	ans_string = """
---- (c (W/L)1 = 15, (W/L)2 = 30) ----------------------------------------------
              iD M1 = iD M2
Kn1( VGS1 - VTN )^2 = Kn2( VGS2 - VTN )^2
M1 and M2 are not matched since their (W/L) differ.

Kn1 = (k'n/2)((W/L)1)
Kn2 = (k'n/2)((W/L)2)

Also, VDD - VGS1 - VGS2 = 0 -OR- VGS2 = VDD - VGS1.

Substitute VGS2 with above, solve for VGS1 by equating the current in saturation:

  Kn1(VGS1 - VTN)^2 = Kn2(VDD - VGS1 - VTN)^2
"""
	print( ans_string )

	Kn1:float = (k_prime_n/2 )*(WoverL_M1c)
	Kn2:float = (k_prime_n/2 )*(WoverL_M2c)
	print( f"Kn1 = {Kn1}" )
	print( f"Kn2 = {Kn2}" )

	z:float = Kn1 / Kn2
	print( f"Let z = Kn1 / Kn2 = {z}" )

	calc_VGS1:float = ( VDD - VTN + sqrt(z)*VTN ) / (sqrt(z) + 1)
	calc_VGS1 = round(calc_VGS1,2)
	print( f"VGS1 = {calc_VGS1}V" )
	calc_Vo:float = VDD - calc_VGS1
	calc_VGS2:float = calc_Vo
	print( f"Vo = VGS2 = VDD - VGS1 {calc_Vo}V" )

	print( 'Next, solve for ID(sat) for each MOSFET to confirm they are equal.' )

	calc_ID1:float = Kn1 * ( calc_VGS1 - VTN )**2
	calc_ID1 = round(calc_ID1,5)
	print( f"ID1(sat) = Kn1 * ( calc_VGS1 - VTN )^2 = {calc_ID1*1000}mA")

	calc_ID2:float = Kn2 * ( calc_VGS2 - VTN )**2
	calc_ID2 = round(calc_ID2,5)
	print( f"ID2(sat) = Kn1 * ( calc_VGS2 - VTN )^2 = {calc_ID2*1000}mA")

	print( '\nNote that the ID(sat) currents for part (b) and (c) are equal.' )
