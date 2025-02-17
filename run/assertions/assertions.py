
def assert_within_percentage( actual:float, expected:float, percentage:float=5.0 ) -> None:
	"""
		Args:
			actual:float the calculated value to check
			expected:float the target value
			percentage:float default=5%
	"""
	tolerance = expected * ( percentage / 100.0 )
	# print( f"abs(actual - expected) ?= tolerance -- {abs(actual - expected)} ?= {abs(tolerance)}" )
	# config the output number format
	if( (actual > 1000) or (actual < 0.001) ):
		o_msg = f"Actual {actual:.3e} is not within {percentage}% of expected {expected:.3e}"
	else:
		o_msg = f"Actual {actual:.3e} is not within {percentage}% of expected {expected}"

	assert abs(actual - expected) <= abs(tolerance), o_msg
