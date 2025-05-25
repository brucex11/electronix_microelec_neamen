import math
from typing import List

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


def r1_parallel_r2( r1:float, r2:float ) -> float:
	"""
	Calculate equivalent resistance of r1 in parallel with r2.

		Args:
			r1: resistor-1 value
			r2: resistor-2 value

		Return: float equivalent resistance
	"""
	return r1 * r2 / (r1 + r2)


def to_s_k( val:float, r_val:int ) -> str:
	"""
	Convert val to kilo and then into string
	with units; good for print to console.

		Args:
			val: value to convert
			r_val: round param

		Return: str \"val\" rounded to r_val
	"""
	rnd:float = round( val*1e-03, r_val )
	return f"{rnd}"


def to_s_mA( val:float, r_val:int ) -> str:
	"""
	Convert amps to mA and then into string
	with units; good for print to console.

		Args:
			val: amps
			r_val: round param

		Return: str \"val-mA\" rounded to r_val (without the '-')
	"""
	rnd:float = round( val*1e+03, r_val )
	return f"{rnd}mA"


def to_s_uA( val:float, r_val:int ) -> str:
	"""
	Convert amps to microA, truncate, and then convert to string
	with units; good for print to console.

		Args:
			val: amps
			r_val: round param

		Return: str \"val-uA\" rounded to r_val and truncated (without the '-')
	"""
	rnd:float = round( val*1e+06, r_val )
	trnc:float = math.trunc( rnd * 1000 ) / 1000
	return f"{trnc}uA"
