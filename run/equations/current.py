import math
from typing import List

def current_divider( R_thru:float, R_other:float, Is:float ) -> float:
	"""
	Calculate current through two parallel resistances. The desired current
	flows thru R_thru branch, the other flows through R_other branch.
	In paramater list, R_thru is the resistor through which the current
	is desired (and is output by this function).

		I_thru = [ R_thru / (R_other + R_thru) ] * Is

		Args:
			R_thru: resistor for desired current
			R_other: the other parallel resistor
			Is: input current

		Return: float I_thru desired current
	"""
	return  ( R_thru / (R_other + R_thru) ) * Is
