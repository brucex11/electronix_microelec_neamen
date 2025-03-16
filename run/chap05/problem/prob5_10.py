from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions import assertions

def prob5_10(self):
	"""Page 353:
	An npn transistor has a reverse-saturation current of IS = 5e-15A and
	a current gain of β = 125. The transistor is biased at vBE = 0.615V.
	Determine iB, iC , and iE.
	ANS:  iB = 0.7495μA, iE = 94.44μA, iC = 93.7μA 
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 0.4
	print( '-----------------------------------------------\nSolution' )

	# ---- Answers -------------------
	ans_iB:float = 0.7495e-06   # A
	ans_iE:float = 94.44e-06    # A
	ans_iC:float = 93.7e-06     # A

	# ---- Givens --------------------
	IS:float = 5e-15   # A
	Beta:float = 125
	vBE: float = 0.615   # V


	ans_string:str = """
When NPN device BE junction is forward biased, then operating in active region.
Like the diode (device), current through the junction is an exponential function
of the forward-bias voltage.  See Eq 5.1

In the active-region,

    COLLECTOR-CURRENT IS ESSENTIALLY INDEPENDENT OF COLLECTOR-VOLTAGE
            AND DEPENDS ONLY ON EMITTER-CURRENT.

And,
      EMITTER-CURRENT IS DRIVEN BY THE VBE FORWARD-BIAS VOLTAGE.

The device therefore looks like a constant-current source where the collector
current is controlled by the B-E voltage (VBE).

In other words, the current at one terminal (the collector) is CONTROLLED
by the voltage across the other two terminals.

       This CONTROL is the basic transistor action!!

iC = IS * ( math.exp( VBE / VT) )    Eq (5.2)
"""
	print( ans_string )

	print( '\n---- (iC) -------------------------------------------' )

	calc_iC:float = self.calc_BJT_collector_current( IS=IS, VBE=vBE )
	calc_iC = round(calc_iC,9)

	try:
		assertions.assert_within_percentage( calc_iC, ans_iC, assert_percentage )
		print( f"CALC collector current, per Eq (5.2):  iC = {calc_iC}A is within {assert_percentage}% of accepted answer: {ans_iC}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	print( '\n---- (iB) -------------------------------------------' )
	ans_string = """
Since:

  **>  iC = Beta(iB)   Eq (5.8)  note: conventional current gain
and Beta is given, calculate iB.
"""
	print( ans_string )

	calc_iB:float = calc_iC / Beta
	calc_iB = round(calc_iB,9)

	try:
		assertions.assert_within_percentage( calc_iB, ans_iB, assert_percentage )
		print( f"CALC base current iB = {calc_iB}A is within {assert_percentage}% of accepted answer: {ans_iB}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	print( '\n---- (iE) -------------------------------------------' )
	ans_string = """
With iC and iB known, there are two ways to calculate iE:

  **>  iE = iC + iB         Eq (5.7)

  **>  iE = (1 + Beta)iB    Eq (5.9)

"""
	print( ans_string )

	calc_iE:float = calc_iC - calc_iB
	calc_iE = round(calc_iE,9)

	assert_percentage = 1.6
	try:
		assertions.assert_within_percentage( calc_iE, ans_iE, assert_percentage )
		print( f"CALC emitter current iE = iC - iB = {calc_iE}A is within {assert_percentage}% of accepted answer: {ans_iE}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	calc_iE = ( 1 + Beta ) * calc_iB
	calc_iE = round(calc_iE,9)

	assert_percentage = 0.2
	try:
		assertions.assert_within_percentage( calc_iE, ans_iE, assert_percentage )
		print( f"CALC emitter current iE = (1 + Beta)iB = {calc_iE}A is within {assert_percentage}% of accepted answer: {ans_iE}A." )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	print( f"\n--- END {self.prob_str} ---" )
