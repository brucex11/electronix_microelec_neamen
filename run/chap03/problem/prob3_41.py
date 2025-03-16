
from inspect import currentframe
from math import sqrt
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob3_41(self):
	"""Page 199:
	Design the circuit in Figure P3.41 so that VSD = 2.5V. The current in the
	bias resistors should be no more than 10 percent of the drain current. The
	transistor parameters are VTP = +1.5V and Kp = 0.5mA/V^2.
	ANS: Page 1363:
	IDQ = 1.25mA, R2 = 59.4kΩ, R1 = 20.6kΩ.
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


	VSS:float = 5          # V
	VDD:float = -5         # V
	RS:float = 2000        # ohm
	VSD_spec:float = 2.5   # V
	VTP:float = +1.5       # V
	Kp:float = 0.5e-03     # A/V^2

	# calc_ID:float = 0

	ans_string:str = """
Per the schematic MOSFET symbol, the device is manufactured in depletion-mode.
Therefore, a channel exists even at zero gate voltage, and a positive gate voltage
must be applied to turn the transistor OFF.

Per the given specs: since VSD = 2.5V, then the voltage drop across RS = 5 - 2.5 = 2.5V.
This "forces" the current through the PMOS channel since the channel is in series
with RS.
"""
	print( ans_string )

	print( '---- (calc ID) ---------------------------------------------' )

	calc_IDQ: float = ( VSS - VSD_spec ) / RS
	print( f"IDQ = ( VSS - VSD_spec ) / RS = {calc_IDQ}A" )


	ans_string = """
Per the given specs: current through the bias resistors R1 and R2 must be less
than or equal to 10% of drain current.  To meet this, start by calculating the
series resistance R1 + R2 between 10V supply (VSS - VDD) and (0.1)(IDQ).
"""
	print( ans_string )

	# print( '---- (calc R1+R2) ---------------------------------------------' )
	# Rbias_total:float = ( VSS - VDD ) / (0.1 * calc_IDQ )
	# print( f"R1+R2 = Rbias_total = ( VSS - VDD ) / (0.1 * IDQ ) = {Rbias_total}ohm" )

	print( '---- (calc VSG in saturation) -------------------------------------' )

	calc_VSG:float = sqrt( calc_IDQ / Kp ) - VTP
	print( f"VSG = sqrt( IDQ / Kp ) - VTP = {calc_VSG}V" )


	ans_string = """
By determining the gate voltage, the voltage drops across the bias resistors
will be known, and with the bias current already specified and calulated,
the individual bias resistor values are calculated.

The gate voltage VG is simply VS - VGS.
"""
	print( ans_string )

	print( '---- (calc R1 and R2) ---------------------------------------------' )
	Ibias_lim:float = 0.1   # 10%
	print( f"Ibias current limit = {Ibias_lim * 100}%")
	calc_VG:float = VSD_spec - calc_VSG
	print( f"VG = VS - VSG = {round(calc_VG, 2)}V" )

	calc_R1:float = ( VSS - round(calc_VG, 2) ) / ( Ibias_lim * calc_IDQ )
	print( f"R1 = ( VSS - VG ) / ( Ibias_lim * IDQ ) = {calc_R1}ohm" )

	calc_R2:float = ( round(calc_VG, 2) - VDD ) / ( Ibias_lim * calc_IDQ )
	print( f"R2 = ( VG - VDD ) / ( Ibias_lim * IDQ ) = {calc_R2}ohm" )

	print( f"\n--- END {self.prob_str} ---" )
