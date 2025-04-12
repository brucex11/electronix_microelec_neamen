from inspect import currentframe
import math
from typing import List, Tuple  # Any, Dict, Set

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2


def prob6_50D(self):
	"""Page 460:
	For the transistor in Figure P6.50, the parameters are β = 100 and VA = inf.
	(a) Design the circuit such that IEQ = 1mA and the Q-point is in the center
	of the dc load line. (b) If the peak-to-peak sinusoidal output voltage is 4V,
	determine the peak-to-peak sinusoidal signals at the base of the transistor
	and the peak-to-peak value of vs. (c) If a load resistor RL = 1kΩ is
	connected to the output through a coupling capacitor, determine the peak-to-
	peak value in the output voltage, assuming vs is equal to the value determined
	in part (b).
	See file ./docx/chap06/problem/chap06_prob6_50D.docx.
	Fri, Apr 11, 2025  9:27:26 AM
	ANS:  (a) RE = 5k, RB = 434.3k, IBQ = 9.9uA
				(b) vb p-p = 4.02V, vs p-p = 4.03V
			  (c) See folder ./LTspice/chap06/ prob6_50D/.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π

	# ---- Answers -------------------
	ans:float = 1

	# ---- Design specs --------------
	VCC:float = 10     # V
	IEQ:float = 0.001  # 1mA
	Beta:float = 100
	vo_pp:float = 4    # V
	Rs:float = 700     # Ω
	RL:float = 1000    # Ω

	# ---- Assumptions ---------------
	VBE:float = 0.7   # V
	VCEQ:float = VCC / 2   #  Q-point is in the center of the dc load line

	# ---- DC Calcs ---------------------
	RE:float = VCEQ / IEQ
	RB:float = (VCC - VBE - VCEQ) * (1 + Beta) / IEQ  # correct!
	IBQ:float = IEQ / (1 + Beta)
	IBQ = round(IBQ,7)

	# Recalculate RB using IBQ
	RB = (VCC - VBE - VCEQ) / IBQ  # correct!
	RB = round(RB,0)


	ans_string:str = f"""
---- DC analysis ----
Given IEQ and Q-point in the center of the DC load line,
calculate RE and RB using DC-analysis.

  VCEQ = VCC / 2 = {VCC} / 2
       = {VCEQ}V.

Solve for RE:

  VRE   = (VCEQ - 0) = (IEQ * RE)
  VCEQ  = (IEQ * RE)
    RE = VCEQ / IEQ
       = {VCEQ} / {to_s_mA(IEQ,3)}
    RE = {RE} = {to_s_k(RE,3)}k.

Solve for RB using KVL in B-E branch.
First, calculate IBQ given Beta and IE:

  IBQ = IEQ / (1 + Beta)
      = {IEQ} / (1 + {Beta})
  IBQ = {IBQ} = {to_s_uA(IBQ,6)}

KVL in B-E junction branch:

  VCC - IBQ*RB - VBE - VCEQ = 0
	IBQ*RB = VCC - VBE - VCEQ

  RB = (VCC - VBE - VCEQ) / IBQ
  RB = {RB} = {to_s_k(RB,1)}k.
"""
	print( ans_string, end='' )


	# ---- AC vb p-p Calcs ---------------------
	RE:float = VCEQ / IEQ
	rpi:float = self._vthrml0_026 / IBQ
	rpi = round(rpi,0)

	Av:float = (1 + Beta)*RE / ( rpi + (1 + Beta)*RE )
	Av = round(Av,4)
	vb_pp:float = vo_pp / Av
	vb_pp = round(vb_pp,3)


	ans_string = f"""
---- AC analysis vb p-p ----
Draw the AC small-signal equivalent circuit (see file
./LTspice/schematics_for_diagrams_only/chap06/prob6_50D
/prob6_50D_AC_small-signal_equivalent.asc).

rpi is required, so do the calculation:

  rpi = VT / IBQ = (Beta * VT) / ICQ   Eq 6022 pg 379
      = {self._vthrml0_026} / {IBQ}
  rpi = {rpi} = {to_s_k(rpi,3)}k.

Using the AC small-signal equivalent circuit, there are
4 steps to do the analysis:
  1) apply KVL to B-E junction-branch for INPUT and
     solve for IBQ.
  2) apply Ohm's law to Q1-emitter-branch (RE) for OUTPUT and
     solve for vo.
  3) substitute IBQ per the INPUT equation for
     IBQ in OUTPUT equation.
  4) divide by vb to obtain the ratio Av = vo/vb.

1) INPUT KVL
  vb - IBQ*rpi - vRE = 0

Now, to solve for vRE, use Ohm's law per the given emitter
quiescent current IEQ and the calculated resistance RE.

  vRE = IEQ * RE = (1 + Beta)*IBQ*RE

Now apply KVL to the AC small-signal equivalent circuit
INPUT branch:

  vb - IBQ*rpi - vRE = 0
  vb - IBQ*rpi - (1 + Beta)*IBQ*RE = 0

Solve for IBQ:

  vb = IBQ*rpi + (1 + Beta)*IBQ*RE
     = IBQ * (rpi + (1 + Beta)*RE)

  **> IBQ = vb / (rpi + (1 + Beta)*RE)

2) OUTPUT
Use Ohm's law for OUTPUT circuit in emitter branch for vo:

  vo = IEQ * RE
     = (1 + Beta)*IBQ*RE

  **> vo = (1 + Beta)*IBQ*RE

3) Substitute IBQ per the INPUT equation for
   IBQ in OUTPUT equation:

  vo = (1 + Beta)*RE * IBQ
     = (1 + Beta)*RE * [vb / (rpi + (1 + Beta)*RE)]
     = (1 + Beta)*RE * (vb) / (rpi + (1 + Beta)*RE)

4) Divide by vb for ratio Av = vo / vb:

  **> Av = (1 + Beta)*RE / (rpi + (1 + Beta)*RE)
         = (1 + {Beta})*{RE} / ({rpi} + (1 + {Beta})*{RE})
         = {Av}.

Now, peak-to-peak at Q1's base-node vb = vo / Av = {vo_pp} / {Av}
     vb = {vb_pp}Vp-p.
"""
	print( ans_string )


	# ---- AC vs p-p Calcs ---------------------
	Rib:float = rpi + (1 + Beta)*RE
	Ri:float = r1_parallel_r2(RB, Rib)

	vs_pp:float = ( vb_pp * (Rs + Ri) ) / Ri
	vs_pp = round(vs_pp,3)

	ans_string = f"""
---- AC analysis vs p-p ----
For AC small-signal equivalent circuit, see file
./LTspice/schematics_for_diagrams_only/chap06/prob6_50D
/prob6_50D_AC_small-signal_equivalent.asc.

The input-side of the circuit is a single loop with vs
as the signal source and resistor Rs and Ri in series.

Rib is the resistance looking into Q1's base-node and
\"seen\" through the rest of the circuit; for this
schematic, this includes rpi, and RE.

Q1 input resistance into the base:

  Rib = rpi + (1 + Beta)*RE
      = {rpi} + (1 + {Beta})*{RE}
  Rib = {Rib} = {to_s_k(Rib,1)}k.

And,
  Ri = RB||Rib
     = {RB}||{Rib}
  Ri = {Ri} = {to_s_k(Ri,1)}k.

Use voltage-divider to determine vs.

  vb = (vs * Ri) / (Rs + Ri)
  vb * (Rs + Ri) = (vs * Ri)
  vs = [vb * (Rs + Ri)] / Ri
     = [{vb_pp} * ({Rs} + {to_s_k(Ri,1)}k)] / {to_s_k(Ri,1)}k
  vs = {vs_pp}Vp-p.
"""
	print( ans_string, end='' )


	# ---- AC with load RL Calcs ---------------------
	RE_p_RL:float = r1_parallel_r2(RE, RL)
	RE_p_RL = round(RE_p_RL,0)
	Rib_with_load:float = rpi + (1 + Beta)*RE_p_RL
	Ri_with_load:float = r1_parallel_r2(RB, Rib_with_load)

	vb_pp = ( vs_pp * Ri_with_load) / (Rs + Ri_with_load )
	vb_pp = round(vb_pp,2)

	vo_pp = ( vb_pp * (1+Beta)*RE_p_RL) / (rpi + (1+Beta)*RE_p_RL)
	vo_pp = round(vo_pp,2)

	ans_string = f"""
---- AC analysis add load RL = 1k ----
For AC small-signal equivalent circuit, see file
./LTspice/schematics_for_diagrams_only/chap06/prob6_50D
/prob6_50D_AC_small-signal_with_1k-load.asc.

With load resistor RL, Rib decreases because RE is now
in parallel with RL.
Determine the \"new\" vo p-p using vs = {vs_pp}V.

Q1 input resistance into the base:

  Rib = rpi + (1 + Beta)*(RE||RL)
      = {rpi} + (1 + {Beta})*({RE_p_RL})
  Rib = {Rib_with_load} = {to_s_k(Rib_with_load,1)}k.

(Note that Rib has dropped from {to_s_k(Rib,1)}k to {to_s_k(Rib_with_load,1)}k).

And,
  Ri = RB||Rib
     = {RB}||{Rib_with_load}
  Ri = {Ri_with_load} = {to_s_k(Ri_with_load,1)}k.

(Note that Ri has dropped from {to_s_k(Ri,1)}k to {to_s_k(Ri_with_load,1)}k).

Use 2 voltage-dividers to determine vo p-p:
  1) vs -> vb
  2) vb -> vo.

1) Use voltage-divider to determine vb.

  vb = (vs * Ri) / (Rs + Ri)
  vb = ({vs_pp} * {Ri_with_load}) / ({Rs} + {Ri_with_load})
  vs = [vb * (Rs + Ri)] / Ri
     = [{vb_pp} * ({Rs} + {to_s_k(Ri,1)}k)] / {to_s_k(Ri,1)}k

  vb = {vb_pp}Vp-p.

2) Use voltage-divider to determine vo.

  vo = (vb * (1+Beta)*RE||RL) / (rpi + (1+Beta)*RE||RL)
     = ({vb_pp} * (1+{Beta})*{RE_p_RL}) / ({rpi} + (1+{Beta})*{RE_p_RL})

  vo = {vo_pp}Vp-p.
"""
	print( ans_string, end='' )
	

	print( f"--- END {self.prob_str} ---" )



	# try:
	# 	assert_within_percentage( calc_result, ans, assert_percentage )
	# 	print( f"ASSERT ID = {calc_result}A is within {assert_percentage}% of accepted answer: {ans}." )
	# except AssertionError as e:
	# 	print( f"AssertionError {pnum}: {e}" )


# Usage single value:
# ans_a:float = 0.518e-03   # A
# try:
# 	assert_within_percentage( iDS, ans_a, assert_percentage )
# 	print( f"ASSERT NMOS iDS = {iDS:.3e}A is within {assert_percentage}% of accepted answer: {ans_a:.3e}." )
# except AssertionError as e:
# 	print( f"AssertionError {pnum}: {e}" )

# try:
# 	assert_within_percentage( iSD, ans_a, assert_percentage )
# 	print( f"ASSERT PMOS enhancement mode in saturation: iSD = {round(iSD,7)}V", end=' ' )
# 	print( f"is within {assert_percentage}% of accepted answer {ans_a}V." )
# except AssertionError as e:
# 	print( f"AssertionError {pnum}: {e}" )

# Usage with List:
# list_calc_iD:List[float] = []   #  don't forget to use list_calc_iD.append(val) to load the list!!
# ans_a_iDS:Tuple = (0.518e-03, 0.691e-03, 0.691e-03)   #
# for idx, ans_iDS in enumerate(ans_a_iDS):
# 	try:
# 		assert_within_percentage( list_calc_iDS[idx], ans_iDS, assert_percentage )
# 		print( f"ASSERT NMOS iDS = {list_calc_iDS[idx]:.3e}A is within {assert_percentage}% of accepted answer: {ans_iDS:.3e}." )
# 	except AssertionError as e:
# 		print( f"AssertionError {pnum}: {e}" )


# 	if( ast.literal_eval(self.dict_params['draw_figure']) ):
# 		prep_fig( self, x=diode_voltages, y=calc_result )

# def prep_fig(self, x=(), y=[] ):
# 	import os
# 	import pathlib
# 	import matplotlib.pyplot as plt
# 	from matplotlib.ticker import MaxNLocator

# 	print( f"{prep_fig.__name__}" )
# 	print( f"p1_27.__name__: {p1_27.__name__}" )
# 	dir_plot = os.path.join( self.dir_draw_root, self.dir_draw_subdir )
# 	print( f"dir_plot: '{dir_plot}'" )
# 	pathlib.Path( dir_plot ).mkdir( parents=True, exist_ok=True )

# 	fname = "{a}.png".format( a=p1_27.__name__ )
# 	path_plot = os.path.join( dir_plot, fname )
# 	print( f"path_plot: '{path_plot}'" )

# 	# x = [1, 2, 3, 4, 5]
# 	# y = [2, 3, 5, 7, 11]
# 	x = x
# 	y = y

# 	plt.figure( figsize=self.param_figure_figsize )
# 	plt.scatter(x, y, color='blue', marker='o')  # You can customize the color and marker style

# 	# Set titles and labels
# 	plt.title('Diode Current')
# 	plt.xlabel('Diode V')
# 	plt.xlim( -2.5, 1 )
# 	# Set the x-axis to have 12 divisions
# 	plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=12) )

# 	plt.ylabel('Diode A')
# 	plt.ylim( -1, 25 )
# 	# plt.yscale( 'log' )

# 	# Display the plot
# 	plt.show()
