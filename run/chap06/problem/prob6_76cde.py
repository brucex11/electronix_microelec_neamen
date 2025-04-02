from inspect import currentframe
from typing import List

from equations.equations import equivalent_parallel_resisitance


def prob6_76cde(self):
	"""Page 466:
	Consider the circuit shown in Figure P6.76 with transistor parameters
	β = 120 and VA = inf.
	(a) Determine the small-signal parameters gm, rπ, and ro for both transistors.
	(b) Plot the dc and ac load lines for both transistors.
	(c) Determine the overall small-signal voltage gain Av = vo/vs.
	(d) Determine the input resistance Ris and the output resistance Ro.
	(e) Determine the maximum undistorted swing in the output voltage.
	ANS(a):  gm1 = 22mA/V, rpi1 = 5451.0Ω, ro1 = inf
					 gm2 = 187mA/V, rpi2 = 642.0Ω, ro2 = inf
	ANS(c):  Av1 = -97.2, Av2 = 0.976, Av = Av1*Av2 = -94.9
 	ANS(d):  Ris = 3.61kΩ, Ro = 47.6kΩ
 	ANS(e):  max vo = 2.10Vp-p (peak-to-peak)
	Wed, Apr 2, 2025 11:07:31 AM
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers from (a)-------------------
	gm1 = 22e-03   # A/V
	IBQ_Q2 = 4.052e-05  # A
	rpi_Q2:float = self._vthrml0_026 / IBQ_Q2
	Rib_Q2:float = 26804   # Ω
	Ri_Q2:float = 7924     # Ω
	rpi_Q1:float = 5451    # Ω
	gm2:float = 187e-03    # A/V
	ICQ2:float = 4.86e-03  # A

	# ---- Givens --------------------
	Beta:float = 120  # both Q1 and Q2
	VCC:float = 12
	VEE:float = 0

	# Q1
	R1:float = 67.3e+03
	R2:float = 12.7e+03
	RC1:float = 10000
	RE1:float = 2000

	# Q2
	R3:float = 15e+03
	R4:float = 45e+03
	RE2:float = 1.6e+03

	# Load
	RL:float = 250


	# ---- Assumptions ---------------
	VBE:float = 0.7   # V


	print( '\n---- (calcs for Q1,Q2 Av and total GAIN) ---------------' )

	list_RC_Q1:List[float] = [RC1,Ri_Q2]
	RC1_parallel_Ri_Q2:float = equivalent_parallel_resisitance( list_RC_Q1 )
	Av1:float = -gm1 * RC1_parallel_Ri_Q2

	RE2_parallel_RL:float = equivalent_parallel_resisitance( [RE2,RL] )
	# Av2:float = gm1 * RE2_parallel_RL
	REzf:float = (1 + Beta) * RE2_parallel_RL
	Av2:float = REzf / (rpi_Q2 + REzf)

	Av:float = Av1 * Av2

	ans_string:str = f"""
The circuit's total/overall gain Av is the product of each Q's
individual gain;

  Av = Av1 * Av2.

Use the small-signal equivalent circuit for Q1 to calculate Av1.
Q1's transconductance, gm1, was determined in part (a):

  gm1 = ICQ_Q1 / VT = {gm1}A/V.

Q1 vo = -gm1 * vbe * Q1-collector-resistance.

Q1 vbe = ( rpi1 / ( rpi1 + RB) ) * vs  (voltage divider on input)
-OR-
  vs = ( (rpi1 + RB) / rpi1 ) * vbe
  and since Rb = 0,
  vs = vbe.

Av1 = vo / vs
    = ( -gm1 * vbe * Q1-collector-resistance ) / vbe
    = ( -gm1 * Q1-collector-resistance )

The Q1 collector-resistance for small-signal is RC1||Ri_Q2.

To determine Q2's input resistance Ri_Q2, first calculate its rpi:

  rpiQ2 = VT / IBQ_Q2
        = {self._vthrml0_026} / {IBQ_Q2}
        = {rpi_Q2}ohm
Then,
  **>  Q2 Rib = rpiQ2 + (1+Beta) * (RE2||RL)
              = {rpi_Q2} + (1+{Beta}) * (RE2_parallel_RL)
              = {rpi_Q2} + (1+{Beta}) * (RE2_parallel_RL)
              = {Rib_Q2}ohm.

Therefore, Q2's input resistance (seen at Q1's collector) is
Ri_Q2 = R3||R4||Q2-Rib.

  Ri_Q2 = {R3}||{R4}||{Rib_Q2}
        = {Ri_Q2}ohm.

Now, calculateQ1 Av1:

  Av1 = -gm1 * (RC1||Ri_Q2)
      = -{gm1} * ({RC1}||{Ri_Q2})
      = -{gm1} * {RC1_parallel_Ri_Q2}
      = {Av1}.

Av2 = small-signal voltage gain is defined as Vo / Vs (phasor notation).
Av2 is the product of two ratios:

  1) REzf / Rib_Q2
     where:
     REzf = emitter-resistance due to impedance-reflection
          = (1 + Beta) * RE2||RL
     Rib_Q2 = total input resistance at the base-terminal
            = rpi_Q2 + emitter-resistance due to impedance-reflection
            = rpi_Q2 + REzf

  2) Ri / (RS + Ri)
     where:
     Ri = R3||R4||Rib_Q2
     RS = voltage source resistance = 0

  Av = ( REzf /     Rib )      X ( Ri / (0 + Ri) )
     = ( REzf / (rpi_Q2 + REzf) ) X ( Ri / Ri )
     = ( REzf / (rpi_Q2 + REzf) ) X ( 1 )
     = ( REzf / (rpi_Q2 + REzf) )
     = ( {REzf} / ({rpi_Q2} + {REzf}) )

  Av2 = {Av2}.

Total gain Av = Av1 * Av2
              = {Av1} * {Av2}
              = {Av}.
"""
	print( ans_string )


	print( '\n---- (calcs for Ris and Ro) ----------------------' )

	Ris:float = equivalent_parallel_resisitance( [R1,R2,rpi_Q1] )
	RS:float = equivalent_parallel_resisitance( [R3,R4,RC1] )
	REzf_Q2:float = (rpi_Q2 + RS) / (1 + Beta)
	Ro:float = equivalent_parallel_resisitance( [REzf_Q2,RE2] )

	ans_string = f"""
Ris is the input impedance for Q1 which is the parallel resistances
of R1, R2, rpi_Q1.

  Ris = R1||R2||rpi_Q1
      = {R1}||{R2}||{rpi_Q1}
      = {Ris}ohm.


Ro = Q2'S emitter impedance reflection against 4 resistances 'looking back'
from the emitter: rpi_Q2, R3, R4, and RC1.

Note that R3, R4, and RC1 are in parallel, so let
  RS = R3||R4||RC1
     = {R3}||{R4}||{RC1}
     = {RS}ohm.

rpi_Q2 is in series with RS; apply impedance-reflection against this
sum:
  REzf_Q2 = (rpi_Q2 + RS) / (1 + Beta)
          = ({rpi_Q2} + {RS}) / (1 + {Beta})
          = {REzf_Q2}ohm.
Finally,
Ro is the output impedance of Q2's reflection-impedance in parallel
with RE2.
  Ro = REzf_Q2||RE2
     = {REzf_Q2}||{RE2}
     = {Ro}ohm.
"""
	print( ans_string )


	print( '\n---- (calcs for max vo undistorted swing) -----------' )
	RE2_parallel_RL = equivalent_parallel_resisitance( [RE2,RL] )
	delta_vce:float = ICQ2 * RE2_parallel_RL
	delta_vce = round(delta_vce,2)
	max_pp_swing:float = 2 * delta_vce
	max_pp_swing = round(max_pp_swing,1)

	ans_string = f"""
From part (a), ICQ2 = {ICQ2*1000}mA.
Load R for AC is RE2||RL.

  RL_AC = RE2||RL
        = {RE2}||{RL}
        = {RE2_parallel_RL}ohm.

Still to learn why:
  |delta_vce| = ICQ_Q2 * RL_AC
              = {ICQ2} * {RE2_parallel_RL}
              = {delta_vce}v.

Max. output voltage swing {max_pp_swing}v peak-to-peak.
"""

	print( ans_string )

	print( f"\n--- END {self.prob_str} ---" )
