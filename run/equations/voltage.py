import math
from typing import List

def voltage_divider( V_pos:float, R1:float, R2:float, V_neg:float ) -> float:
	"""
	Calculate the voltage between two resistors.

		V_div = ((V_pos*R2) + (V_neg*R1)) / (R1 + R2)
		-OR-
		V_div = ((V_pos / R1) + (V_neg/R2)) / ((1/R1) + (1/R2))

		Args:
			V_pos: positive voltage
			V_neg: negative voltage
			R1: resistor connected to V_pos
			R2: resistor connected to V_neg
			Is: input current

		Return: float V_div desired voltage between R1 and R2
	"""
	return ((V_pos*R2) + (V_neg*R1)) / (R1 + R2)


def equivalent_parallel_resisitance( list_rs:List[float] ) -> float:
	"""
	Calculate equivalent resistance of resistors in parallel.

		1/Req = 1/R1 + 1/R2 + 1/R2 + ...

		Args:
			list_rs: 3 or more resistance values

		Return: float equivalent resistance
	"""
	req:float = 0
	# Use list comprehension to compute the reciprocal of each value.
	reciprocals = [1/v for v in list_rs]
	total = sum(reciprocals)
	return  1 / total

