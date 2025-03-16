
from inspect import currentframe
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_30(self):
	"""Page 197:
	Consider the circuit in Figure P3.30.  The transistor parameters are
	VTP = -0.8V and Kp = 0.5mA/V^2.  Determine ID, VSG, and VSD.
	ANS:  ID = 0.2332mA, VSG = 1.483V, VSD = 4.72V.

	See also ./LTspice/chap03/prob3_30/
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
	print( '-----------------------------------------------\nSolution' )

	ans_string:str = """
First, since the given VTP < 0, device is p-chan enhancement mode.

The current (IGB) in the voltage-divider circuit that drives the PMOS gate
is biased by 6V across R1 and R2.  (GB: gate bias).
Calculate the gate voltage to determine if the threshold voltage is exceeded
to "turn on" the transistor.

    IGB = Vtot / (R1 + R2)

Then, to calc the gate voltage, subtract the voltage-drop across R1 from the
+3 supply voltage VSS.
"""
	print( ans_string )

	# ---- Givens --------------------
	VTP:float = -0.8    # V
	Kp:float = 0.5e-03  # A/V^2
	VSS:float = 3   # V
	VDD:float = -3   # V
	R1:float = 8e+03
	R2:float = 22e+03
	RS:float = 0.5e+03
	RD:float = 5e+03

	calc_Vtotal:float = VSS - VDD    # V

	print( '\n---- (gate bias voltage) -------------------------------' )
	IGB:float = calc_Vtotal / (R1+R2)
	VR1 = IGB * R1
	calc_VG:float = VSS - VR1
	print( f"The gate bias voltage VG = {calc_VG}V" )

	print( '\n---- (PMOS cutoff) -------------------------------------' )
	print( f"At cutoff, iD = 0, therefore with 0 voltage-drop across RS," )
	print( f"VS = +3, and then VSG = VS - VG" )
	VSG_cutoff:float = VSS - calc_VG
	print( f"CALC VSG(cutoff) = {VSG_cutoff}V" )

	ans_string = """
---- (source circuit voltage drops) -----------------------------
VSS - VS - VSG - VG = 0

The voltage-drop across RS = ID*RS where ID is determined by the MOSFET biasing.
Therefore, VS = ID*RS.

Assume saturation-region:  ID = Kp*(VSG + VTP)^2
Substitute ID in voltage-drop equation and solve for VSG.

VSS - RS * ( Kp*(VSG + VTP)^2 ) - VSG - VG = 0

---- (calc VSG) -------------------------------------------------
Let z = RS*Kp.
VSS  -  z*(VSG + VTP)^2  -  VSG  -  VG = 0

VSS  -  z*(VSG + VTP)(VSG + VTP)  -  VSG  -  VG = 0
VSS  -  z*(VSG^2 + 2VSG*VTP + VTP^2)  -  VSG  -  VG = 0
VSS  -  z*VSG^2 - 2zVSG*VTP - zVTP^2  -  VSG  -  VG = 0
Combine VSG and constants to covert to quadratic equation.
[ VSS - zVTP^2 - VG ]  -  zVSG^2  -  2zVSG*VTP  -  VSG = 0
[ VSS - zVTP^2 - VG ]  -  zVSG^2  -  VSG(2zVTP + 1) = 0
Rearrange for quadratic.
-zVSG^2  -  (2zVTP+1)VSG  +  [ VSS - zVTP^2 - VG ] = 0

a = -z
b = -(2zVPT+1)
c = [ VSS - zVTP^2 - VG ]
"""
	print( ans_string )

	z:float = Kp * RS
	print( f"z = {z}" )

	a:float = -z
	b:float = -( 2 * z * VTP + 1 )
	c:float = VSS - ( z * VTP**2 ) - calc_VG
	list_abc:List[float] = [ a, b, c ]
	print( f"list_abc: {list_abc}" )

	calc_roots:List[float ] = []  # reference to function-call
	# list_abc:List[float] = [ 1,2,5 ]   # test-coeffs for complex roots
	if( not self.calc_quadratic_roots( list_abc, calc_roots ) ):
		print( 'Quadratic equation roots are complex' )
		return

	print( f"Quadratic roots: {calc_roots}" )
	calc_VSG:float = calc_roots[1]
	calc_VSG = round(calc_VSG,3)
	print( f"VSG cannot be negative, so\n  VSG = {calc_VSG}V" )


	ans_string = f"""
---- (calculate ID(sat)) ----------------------------------------
With VSG calculated, use the ID(sat) equation to solve for ID(sat):

  ID(sat) = Kp[ VSG + VTP ]^2

  where:
    Kp = {Kp}A/V^2
    VSG = {calc_VSG}V
    VTP = {VTP}V
"""
	print( ans_string )

	calc_ID_sat:float = Kp * ( calc_VSG + VTP )**2
	calc_ID_sat = round(calc_ID_sat,7)
	print( f"ID(sat) = {calc_ID_sat}A = {calc_ID_sat*1000}mA" )

	ans_string = f"""
---- (calculate VSD) --------------------------------------------
With the current through the series components now known, {calc_ID_sat*1000}mA,
use KVL to calculate VSD:

  VSS - VRS - VSD - VRD - VDD = 0
  -OR-
  VSD = VSS - VRS - VRD - VDD

  where:
    VSS = {VSS}V
    VRS = ID(sat) * RS  =  {calc_ID_sat} * {RS}
    VRD = ID(sat) * RD  =  {calc_ID_sat} * {RD}
    VDD = {VDD}V
"""
	print( ans_string )

	calc_VRS:float = calc_ID_sat * RS
	calc_VRD:float = calc_ID_sat * RD
	calc_VSD:float = VSS - calc_VRS - calc_VRD - VDD
	calc_VSD = round(calc_VSD,2)
	print( f"VSD = {calc_VSD}V" )


	ans_string = f"""
---- (calculate VSD(sat)) ---------------------------------------
VSD(sat) = VSG + VTP  =  {calc_VSG} + {VTP}
"""
	print( ans_string )

	calc_VSD_sat:float = calc_VSG + VTP
	print( f"VSD(sat) = {calc_VSD_sat}V" )

	print( f"\n--- END {self.prob_str} ---" )
