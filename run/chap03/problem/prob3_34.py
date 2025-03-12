
from inspect import currentframe
from math import sqrt
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_34(self):
	"""Page 198:
	The transistor parameters for the transistor in Figure P3.34 are
	VTN = 0.4 V, k'n = 120μA/V^2, and W/L = 50. (a) Determine VGS such
	that ID = 0.35mA. (b) Determine VDS and VDS (sat).
	ANS  (a)  VGS = 0.8V 
	ANS  (b)  VDS = 1.1V, VDS(sat) = 0.342V, since VDS > VDS(sat) in saturation.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------' )

	VTN:float = 0.4   # V
	k_prime_n:float = 120e-06   # AV^2
	WoverL:float = 50
	iDS:float = 0.35e-03   # A

	ans_string:str = """
The I-V characteristics defined by Equations (3.2(a)) and (3.2(b)) (Table 3.1)
apply to both enhancement- and depletion-mode n-channel devices.
Per Figure P3.34, and since VTN is positive, the device is enhancement mode.

Given enough specs, calculate Kn conductance parameter, and then use it to
calculate VGS using the I-V equation for saturation.
"""
	print( ans_string )

	print( "---- (k'n process conduction parameter) ---------------------------" )
	print( "Kn = ( k'n / 2)(W/L)  where units of k'n are " )
	Kn:float = ( k_prime_n / 2) * WoverL
	print( f"Kn = {Kn}A/V^2")

	ans_string = """
---- (VGS) --------------------------------------------------------
3.2b
iD = Kn( VGS - VTN )^2
iD / Kn = ( VGS - VTN )^2
sqrt( iD / Kn ) = VGS - VTN
therefore
VGS = sqrt( iD / Kn ) + VTN
"""
	print( ans_string )

	VGS:float = sqrt( iDS / Kn ) + VTN
	print( f"VGS = {VGS}V" )

	ans_string = """
---- (VD = 1.8 - voltage drop across RD) ---------------------------------------
Since the current through RD is the same as iD (since the MOSFET and RD are
in series), then voltage at drain-terminal VD = VDD - (iD*R).
Finally, since the source-terminal of the MOSFET is ground, then VDS = VD.
"""
	print( ans_string )
	VDD:float = 1.8   # v
	RD:float = 2000  # Ω
	VDS:float = VDD - iDS * RD
	print( f"VDS = VD = {VDS}V" )

	ans_string = """
---- (ohmic- or saturation-region of operation?) -------------------------------
MOSFET operation transition-point from ohmic to saturation-mode is when
VDS(sat) = VGS - VTN.
When VDS < VGS - VTN, ohmic-region.
When VDS > VGS - VTN, saturation.
"""
	print( ans_string )

	VDS_sat:float = VGS - VTN
	print( f"VDS(sat) = {round(VDS_sat,3)}V" )
	if( VDS < VDS_sat ):
		print( f"VDS @ {round(VDS,3)}V < VDS(sat) @ {round(VDS_sat,3)}V : device opertaing in ohmic-region." )
	else:
		print( f"VDS @ {round(VDS,3)}V > VDS(sat) @ {round(VDS_sat,3)}V : device opertaing in saturation-region." )
