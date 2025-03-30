from typing import List

def equivalent_parallel_resisitance( list_rs:List[float] ) -> float:
	"""
	Calculate equivalent resistance of resistors in parallel.

		1/Req = 1/R1 + 1/R2 + 1/R2 + ...

		Args:
			list_rs:List[float] 3 or more resistance values
		Return float resistance
	"""
	req:float = 0
	# Use list comprehension to compute the reciprocal of each value.
	reciprocals = [1/v for v in list_rs]
	total = sum(reciprocals)
	return  1 / total


def r1_parallel_r2( r1:float, r2:float ) -> float:
	"""
	Calculate equivalent resistance of r1 in parallel with r2

		Args:
			r1:float resistor-1 value
			r2:float resistor-2 value
		Return float resistance
	"""
	return r1 * r2 / (r1 + r2)
