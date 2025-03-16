
from inspect import currentframe
from math import sqrt

def prob3_22(self):
	"""Page 196:
	An enhancement-mode NMOS transistor has parameters VTNO = 0.8V,
	γ = 0.8V^1/2, and φf = 0.35V. At what value of VSB will the threshold
	voltage change by 2V due to the body effect?
	ANS    VSB = 10.4V
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	# assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	ans_string:str = """
Finite Output Resistance:
When a real MOSFET is biased in the saturation region, the iD versus vDS
characteristics has an actual, nonzero slope beyond the saturation point.

For vDS > vDS(sat), the effective channel length decreases producing the
phenomenon called `channel length modulation` (lambda).

The actual slope of the curve in the saturation region is expressed as the
iD versus vDS characteristic in the form, for an n-channel device:

    iD = Kn[ (vGS - VTN)^2 * (1+lambda*vDS) ]  see Eq 3.7 pg 142

Body Effect:
In integrated circuits, the substrates of all n-channel MOSFETs are
usually common and are tied to the most negative potential in the circuit.
p-chan devices exhibit the same phenomemon.

To maintain a zero- or reverse-biased source-substrate pn junction,
vSB MUST BE >= 0.  The threshold voltage (VTN) for this condition is given by:

    VTN = VTNO + (gamma)[ (2*phi-f + vSB)^1/2 - (2*phi-f)^1/2 ]  see Eq 3.10 pg 144

      where:
        * VTNO  is threshold voltage for vSB = 0
        * gamma is body-effect parameter (aka bulk-threshold), typically 0.5V^1/2
        * phi-f is a function of the semiconductor doping, typically 0.35Volts

Per Eq 3.10 (above):
* the threshold voltage (VTN) in n-channel devices INCREASES due to
  this body effect,
* The body effect can cause a degradation in circuit performance because
  of the changing threshold voltage.

CALCULATE source-substrate pn junction voltage, vSB, when the threshold
voltage (VTN) changes, ie INCREASES, by +2V due to the body effect.
"""
	print( ans_string )

	print( '---- (Eq 3.10 pg 144) ---------------------------------------------' )
	VTNO:float = 0.8     # V
	gamma:float = 0.8    # V^1/2
	phi_f:float = 0.35   # V
	delta_VTN:float = 2  # V

	print( 'VTN = VTNO + (gamma)[ (2*phi-f + vSB)^1/2 - (2*phi-f)^1/2 ]   Eq 3.10' )
	print( 'VTN - VTNO = (gamma)[ (2*phi-f + vSB)^1/2 - (2*phi-f)^1/2 ]' )
	print( '(VTN - VTNO) /  gamma = (2*phi-f + vSB)^1/2 - (2*phi-f)^1/2' )
	print( '[ ((VTN - VTNO) / gamma) + (2*phi-f)^1/2 ] = (2*phi-f + vSB)^1/2' )
	print( '[ ((VTN - VTNO) / gamma) + (2*phi-f)^1/2 ]^2 = (2*phi-f + vSB)' )
	print( '[ ((VTN - VTNO) / gamma) + (2*phi-f)^1/2 ]^2 - 2*phi-f = vSB' )

	vSB:float = ( ((delta_VTN - VTNO) /  gamma) + sqrt((2*phi_f)) )**2 - 2*phi_f
	print( f"\nANS  vSB = {round(vSB,3)}V" )

	print( f"\n--- END {self.prob_str} ---" )
