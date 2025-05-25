from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.current import current_divider
from equations.voltage import voltage_divider


def blitz01_cap(self):
	"""Top-left circuit:
	Find the total frequency response.
	Cpi = 5pF, Cu = 2pF, Beta = 100, and VA = 150V.
	./chap07/blitz/Blitz_Sophia_Freq_response_schematics.pdf.
	./LTspice/chap07/blitz01/.
	./docx/chap07/blitz/01_cap/blitz01.docx
	Sun, Apr 27, 2025  5:33:42 PM
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
	VCC:float = 18
	VEE:float = 0
	RS:float = 10e+03
	R1:float = 300e+03
	R2:float = 60e+03
	RC:float = 10e+03
	RE:float = 1e+03
	# C1:float = 10e-06
	C1:float = 10e-06
	Cpi:float = 5e-12  # pF
	Cu:float =  2e-12  # pF

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V
	# IBQ:float = 15.47e-06  # per LTspice simulation

	# ---- Calcs ---------------------
	VTh:float = (R2 * VCC) / (R1 + R2)
	RB:float = r1_parallel_r2(R1,R2)
	IBQ = (VTh - VBE) / (RB + (1+Beta)*RE)
	ICQ:float = Beta * IBQ

	ans_string:str = f"""
This schematic is exactly the same as Fig 7.21a pg 486.
The difference between small-signal equivalent Fig 7.21b and the small-signal
equivalent circuit for this problem is that ro is not infinite because the
Early voltage VA is given as 150V.

---- (DC op point assuming IBQ=0) ----
Per LTspice, VQ1B = 2.23V which is considerably lower than that calculated
assuming IBQ=0, VBE=0.7, and given Beta=100 as will be seen below.

For Rib=inf, RB = (R1||R2).

Using voltage-divider:
  VTh = (R2 * VCC) / (R1 + R2)
      = ({R2} * {VCC}) / ({R1} + {R2})
  VTh = {VTh}V.

  R1||R2 = {R1}||{R2}
      RB = {RB} = {to_s_k(RB,0)}k.

Using KVL for B-E junction branch:

  VTh - VRTh - VBE - VRE = 0
  VTh - IBQ*RB - VBE - (1+Beta)IBQ*RE = 0
  VTh - VBE = IBQ*RB + (1+Beta)IBQ*RE

  IBQ = (VTh - VBE) / (RB + (1+Beta)*RE)
      = ({VTh} - {VBE}) / ({RB} + (1+{Beta})*{RE})
  IBQ = {IBQ}A = {to_s_uA(IBQ,2)}.

  ICQ = Beta * IBQ = {to_s_mA(ICQ,3)}.
"""
	print( ans_string )


	# Get diff % between theoretical IBQ and LTspice.
	try:
		assert_within_percentage( IBQ, 15.469e-06, assert_percentage )
		print( f"ASSERT IBQ theoretical = {IBQ}A is within {assert_percentage}% of LTspice sim: {15.469e-06}A." )
	except AssertionError as e:
		print( f"AssertionError {pnum}: {e}" )


	# ---- Calcs ---------------------
	IBQ = 15.469e-06
	VT:float = self._vthrml0_026
	# Q1 input resistance
	rpi:float = (Beta * VT) / ICQ
	rpi = round(rpi,1)
	Rib:float = rpi + (1 + Beta)*RE
	Ri:float = r1_parallel_r2(RB,Rib)

	# Q1 output resistance
	ro:float = VA / (Beta * IBQ)
	ro = round(ro,1)
	Ro:float = r1_parallel_r2(ro,RC)
	Ro = round(Ro,1)

	# Q1 transconductance
	gm:float = ICQ / VT
	gm = round(gm,6)


	ans_string = f"""
---- (DC op point using LTspice IBQ) ----
IBQ = {to_s_uA(IBQ,3)}.

Input resistance:
  rpi = VT / IBQ
      = {VT} / {IBQ}
  rpi = {rpi} = {to_s_k(rpi,1)}k.

  Rib = rpi + (1 + Beta)*RE
      = {rpi} + (1 + {Beta})*{RE}
  Rib = {Rib} = {to_s_k(Rib,1)}k.

  Ri = (RB||Rib)
     = ({RB}||{Rib})
  Ri = {Ri} = {to_s_k(Ri,1)}k.

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


	# ---- Calcs ---------------------
	CM:float = Cu * (1 + gm * Ro)
	Ceq:float= Cpi + CM
	# fc:float = 1 / ( 2 * math.pi * tau )
	Req:float = equivalent_parallel_resisitance( [Rib, RB, RS] )

	tau_p:float = Req * Ceq

	fh:float = 1 / ( 2 * math.pi * tau_p )

	ans_string = f"""
---- (Miller capacitance) ----
Per theory:

  CM = Cu * (1 + gm * Ro)   where Ro = (ro||RC)
     = {Cu} * (1 + {gm} * {Ro})
  CM = {CM}.

The upper 3dB frequency is determined by using the time-constant technique.

  fh = 1 / (2*pi*tau-p)   see pg 521

where tau-p = Req*Ceq . In this case, the equivalent capacitance
is Ceq = Cpi + CM, and the equivalent resistance is the effective
resistance seen by the capacitance, Req = (Rib||RB||RS).

  Ceq = Cpi + CM
      = {Cpi} + {CM}
  Ceq = {Ceq}.

  Req = {Req}.

  tau_p = Req * Ceq = {tau_p}.

  fh = 1 / (2*pi*tau-p)
     = 1 / (2*pi*tau-p)
  fh = {fh}Hz.
"""
	print( ans_string )
	return

	# ---- Calcs ---------------------
	tau:float = (RS + Ri) * C1
	fc:float = 1 / ( 2 * math.pi * tau )

	ans_string = f"""
---- (Corner freq) ----
Since the input capacitor C1 is 'series-coupling', the resistance 'seen'
by C1 = RS + Ri.

The time constant tau-s = (RS + Ri)*C1.
  RS + Ri = {RS+Ri}.

  tau = (RS + Ri) * C1
      = ({RS} + {Ri}) * {C1}
  tau = {tau}s.

Therefore, the corner frequency fc = 1 / (2pi*tau)s.

  fc = 1 / (2pi*tau)
     = 1 / (2 * {math.pi} * {tau})
  fc = {fc}Hz.

"""
	print( ans_string )


	# ---- Calcs ---------------------
	# Vpi:float = Ib / rpi
	# Vo:float = -gm * Vpi * Ro

	K:float = -(gm * rpi * Ro) * (RB/(RB + Rib)) * ( 1 / (RS + Ri) )
	Av_mag:float = 20 * math.log10( abs(K) )

	ans_string = f"""
---- (Input-current/output-voltage analysis) ----
Calculate the small-signal voltage-gain Av = Vo/Vi.

Substitute the input current Ib into the equation for output-voltage Vo.

For the small-signal equivalent circuit Fig 7.21b, the circuit input
current Ii flows through the series resistances RS, C1, and Ri:

  Ii = Vi / (RS + (1/sC1) + Ri)   (Eq 1)

Using a current divider, determine the base current.

Ib = (RB/(RB + Rib)) * Ii    (2)

Vpi = Ib*rpi   (3)

For the small-signal equivalent circuit Fig 7.21b, the output voltage:
  Vo = -gm * Vpi * (ro||RC)
  Vo = -gm * Vpi * Ro       (4)

Substitute for Vpi (Eq 3) into (4):

  Vo = -gm * (Ib*rpi) * Ro

Substitute for Ib (Eq 2):

  Vo = -gm * [(RB/(RB + Rib))] * Ii * rpi * Ro

Finally, substitute for Ii (Eq 1):

  Vo = -gm * [(RB/(RB + Rib))] * [Vi / (RS + (1/sC1) + Ri)] * rpi * Ro
  Vo = -(gm * rpi * Ro) * [(RB/(RB + Rib))] * [Vi / (RS + (1/sC1) + Ri)]

Bring-over Vi and rearrange:

  Av = Vo / Vi
  Av = -(gm * rpi * Ro) * [(RB/(RB + Rib))] * [1 / (RS + (1/sC1) + Ri)]

Combine the DC-gain components:

  K = -(gm * rpi * Ro) * [(RB/(RB + Rib))]

such that:

  Av = K * [1 / (RS + (1/sC1) + Ri)]    SEE PAGE 487

For the frequency-dependent portion of the Av equation, multiply
by (sC1/sC1) to put into known form that contains the time-constant
tau = (RS + Ri)*C1:

  [1  / ( RS + (1/sC1) + Ri )] * (sC1/sC1)
	sC1 / ( sC1*RS + 1 + sC1*Ri )
	sC1 / ( sC1*RS + sC1*Ri + 1 )
	sC1 / ( sC1*(RS + Ri) + 1 )

	Sub C1 = tau / (RS + Ri)

	s*(tau / (RS + Ri)) / ( s*(tau / (RS + Ri)*(RS + Ri) + 1 )
	( 1 / (RS + Ri) ) * ( s*tau / (s*tau + 1))

	Move the ( 1 / (RS + Ri) ) over to K such that:

  K = -(gm * rpi * Ro) * (RB/(RB + Rib)) * ( 1 / (RS + Ri) )

  **> Av = K * ( s*tau / ( 1 + s*tau) )

Therefore, max gain = K.

  K = -({gm} * rpi * Ro) * (RB/(RB + Rib)) * ( 1 / (RS + Ri) )
	K = {K}.
And,

  **> |Av(max)|dB = 20*log10( K )
                  = 20*log10( {abs(K)} )
  **> |Av(max)|dB = {Av_mag}.

"""
	print( ans_string )



	print( f"--- END {self.prob_str} ---" )
