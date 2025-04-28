from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def blitz02(self):
	"""Top-right circuit:
	Find the total frequency response.  Ignore parasitic capacitances cpi and cu.
	cpi = 5pF, cu = 2pF, Beta = 100, and VA = 150V.
	./chap07/blitz/Blitz_Sophia_Freq_response_schematics.pdf.
	./LTspice/chap07/blitz02/.
	./docx/chap07/blitz/02/blitz02.docx
	Sun, Apr 27, 2025  7:31:57 AM
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 1.6
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  τ

	# ---- Givens --------------------
	Beta:float = 100
	VA:float = 150    # V
	VCC:float = 12
	VEE:float = 0
	RS:float = 0
	R1:float = 1e+06
	RC:float = 6e+03
	C1:float = 2.2e-06
	cpi:float = 5e-12  # pF
	cu:float =  2e-12  # pF

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V
	# IBQ:float = 11.3e-06  # per LTspice simulation

	# ---- Calcs ---------------------
	IBQ = (VCC - VBE) / R1
	ICQ:float = Beta * IBQ
	# Rib:float = VBE / IBQ


	ans_string:str = f"""
---- (DC op point assuming IBQ=0) ----
Assuming VBE=0.7 and  Beta=100.

Calc IBQ:

  IBQ = (VCC - VBE) / R1
      = ({VCC} - {VBE}) / {R1}
  IBQ = {IBQ}A = {to_s_uA(IBQ,3)}.

  ICQ = Beta * IBQ
      = {Beta} * {IBQ}
  ICQ = {ICQ} = {to_s_mA(ICQ,6)}.
"""
	print( ans_string )
	# return


	# Get diff % between theoretical IBQ and LTspice.
	# try:
	# 	assert_within_percentage( IBQ, 15.469e-06, assert_percentage )
	# 	print( f"ASSERT IBQ theoretical = {IBQ}A is within {assert_percentage}% of LTspice sim: {15.469e-06}A." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )


	# ---- Calcs ---------------------
	VT:float = self._vthrml0_026
	# Q1 input resistance
	rpi:float = (VT) / IBQ
	rpi = round(rpi,1)
	# Rib:float = rpi + (1 + Beta)*RE
	# Ri:float = r1_parallel_r2(RTh,Rib)
	RTh:float = r1_parallel_r2(R1,rpi)

	# Q1 output resistance
	ro:float = VA / (Beta * IBQ)
	ro = round(ro,1)
	Ro:float = r1_parallel_r2(ro,RC)
	Ro = round(Ro,1)

	# Q1 transconductance
	gm:float = ICQ / VT
	gm = round(gm,6)


	ans_string = f"""
Input resistance:
  rpi = VT / IBQ
      = {VT} / {IBQ}
  rpi = {rpi} = {to_s_k(rpi,1)}k.

This is the Thevenin resistance to calculate the RC time-constant.
  R1||rpi = {R1}||{rpi}
      RTh = {RTh} = {to_s_k(RTh,0)}k.

Output resistance:
  ro = VA / (Beta * IBQ) = VA / ICQ
     = {VA} / ({Beta} * {IBQ})
  ro = {ro} = {to_s_k(ro,0)}k.

  Ro = (ro||RC)
     = ({ro}||{RC})
  Ro = {Ro} = {to_s_k(Ro,3)}k.

Transconductance:
  gm = ICQ / VT
     = {ICQ} / {VT}
  gm = {gm} = {to_s_mA(gm,1)}/V.
"""
	print( ans_string )
	# return

	# ---- Calcs ---------------------
	tau:float = (RS + RTh) * C1
	fc:float = 1 / ( 2 * math.pi * tau )

	ans_string = f"""
---- (Corner freq) ----
Since the input capacitor C1 is 'series-coupling', the resistance 'seen'
by C1 = RTh.

The time constant tau-s = RTh*C1.
  tau = RTh * C1
      = {RTh} * {C1}
  tau = {tau}s.

Therefore, the corner frequency fc = 1 / (2pi*tau)s.

  fc = 1 / (2pi*tau)
     = 1 / (2 * {math.pi} * {tau})
  fc = {fc}Hz.

"""
	print( ans_string )
	# return


	# ---- Calcs ---------------------
	# Vpi:float = Ib / rpi
	# Vo:float = -gm * Vpi * Ro

	# K:float = -(gm * rpi * Ro) * (RTh/(RTh + Rib)) * ( 1 / (RS + Ri) )
	K:float = -(gm * rpi * Ro) / RTh
	K = round(K,0)
	# K:float = 250
	Av_max:float = 20 * math.log10( abs(K) )

	ans_string = f"""
---- (Av(max) calc) ----
Calculate the small-signal voltage-gain Av = Vo/Vi.

  **> Av(max) = K * ( s*tau / ( 1 + s*tau) )

  **> K = -(gm * rpi * Ro) / RTh
        = -({gm} * {rpi} * {Ro}) / {RTh}
      K = {K}.

  **> |Av(max)|dB = 20*log10( K )
                  = 20*log10( {abs(K)} )
  **> |Av(max)|dB = {Av_max}.
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
