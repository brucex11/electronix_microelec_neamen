from inspect import currentframe
import math
from typing import List, Any  # Tuple, Dict, Set

import matplotlib.pyplot as plt

# from assertions.assertions import assert_within_percentage
# from equations.equations import to_s_k, to_s_mA, to_s_uA
# from equations.equations import equivalent_parallel_resisitance
# from equations.equations import r1_parallel_r2
# from equations.current import current_divider
# from equations.voltage import voltage_divider


def blitz01_HPF_cap(self):
	"""Top-left circuit:
	Find the total frequency response.
	cpi = 5pF, cu = 2pF, Beta = 100, and VA = 150V.
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
	# assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  τ

	# ---- Givens --------------------
	R:float = 43629
	C:float = 10e-06
	K:float = 6.8


	# ---- Assumptions ---------------
	ω_range:List[float] = [round(0.01 + i * 0.01, 2) for i in range(10000)]  # 10000 values from 0.01 to exactly 100.0
	print( f"FIRST value-ω_range: {ω_range[0]}" )
	print( f"LAST value-ω_range:  {ω_range[-1]}" )
	# print( ω_range )
	print( f"len(ω_range): {len(ω_range)}" )
	# return


	# ---- Calcs ----------------------
	tau:float = R * C
	ωc:float = 1 / tau   # cut-off freq radians
	ωc_cutoff:float = round(ωc,2)   # round according to ω_range increment
	fc:float = 1 / (2 * math.pi * tau)
	fc_plot:float = round(fc,3)

	ans_string:str = f"""
For this circuit, the input contains a series-coupling capacitor circuit.
Per the runtime of blitz01.py:

  Av = {K}.

The time constant tau-s = (RS + Ri)*C1.
  RS + Ri = 43628.77929629945.

  tau = (RS + Ri) * C1
      = (10000.0 + 33628.77929629945) * 1e-05
  tau = 0.4362877929629945s.

Therefore, the corner-frequency fc = 1 / (2pi*tau)s.

  fc = 1 / (2pi*tau)
     = 1 / (2 * 3.141592653589793 * 0.4362877929629945)
  fc = 0.36479348186896143Hz.

The corner-frequency fc is recalculated here:

  fc = 1 / (2pi*tau)
     = 1 / (2pi*{tau})
  fc = {fc} = {fc_plot}Hz.
  ωc = {ωc}rad.
"""
	print( ans_string )
	# return

	# ----------------------------------------------------------------------------
	# --- mag --------------------------------------------------------------------
	# ----------------------------------------------------------------------------

	ax1_plot_label_Tdb:str = '|T(ω)|=20log[ω/sqr(1+ω^2)]'
	list_Tdb:List[float] = []
	ωpoint01_dB_crossing_point:List[Any] = []    # ω=.01
	ωpoint1_dB_crossing_point:List[Any] = []   # ω=.1
	ω1_dB_crossing_point:List[Any] = []    # ω=1
	ω10_dB_crossing_point:List[Any] = []   # ω=10

	ω_cutoff_crossing_point:List[Any] = []   # (ω/ωc)=1

	# T_jω:float = 1 / (1 + ω)

	# ---- Calcs ---------------------
	for idx, ω in enumerate(ω_range):
		eq:float = K * ω * tau * math.sqrt( 1 / (1 + (ω/ωc)**2) )
		val2:float = 20 * math.log10( eq )
		val2 = round(val2,2)
		list_Tdb.append( val2 )
		if( ω == .01 ):
			ωpoint01_dB_crossing_point = [ω_range[idx],val2]
			print( f"ωpoint01_dB_crossing_point: {ωpoint01_dB_crossing_point}" )
		if( ω == .1 ):
			ωpoint1_dB_crossing_point = [ω_range[idx],val2]
			print( f"ωpoint1_dB_crossing_point: {ωpoint1_dB_crossing_point}" )
		if( ω == ωc_cutoff ):
			ω_cutoff_crossing_point = [ω_range[idx],val2]
			print( f"ω_cutoff_crossing_point: {ω_cutoff_crossing_point}" )
		if( ω == 1 ):
			ω1_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω1_dB_crossing_point: {ω1_dB_crossing_point}" )
		if( ω == 10 ):
			ω10_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω10_dB_crossing_point: {ω10_dB_crossing_point}" )


# 	ans_string:str = """
# ---- ({}DC op point) ----
# REPLACE THIS TEXT.
# """
	# print( ans_string )

	# print( '\n---- (a) ----' )

	# Tight_layout() doesn't quite behave as expected with semilog or log-log plots,
	# so use newer implementation with 'constrained_layout=True' parameter.
	# Hm, the above in conjunction with plt.tight_layout() -OR- fig.tight_layout()
	# still does not work (there's still 'margin' between the log-line and the axes).
	fig, ax1 = plt.subplots(constrained_layout=True)  # Create a figure and axis for the first plot
	ax1.set_xlabel('ω')  # shared x-axis
	ax1.set_ylabel('|T(ω)|', color='k')  # Set y-axis label for the first axis
	# ax1.set_ylabel('20log(ω/ωo)', color='k')  # Set y-axis label for the first axis

	# linear v linear ( y v x )
	# ax1.plot( ω_range, list_Tdb, color='b', label='T(ω) = 1 / (1 + ω)' )
	# ax1.plot( ω_range, list_Tjω, color='r', label='T(ω) = 1 / (1 + ω)' )

	# linear v log
	# ax1.semilogx( ω_range, list_Tjω, color='b', label=ax1_plot_label_Tjω )
	ax1.semilogx( ω_range, list_Tdb, color='b', label=ax1_plot_label_Tdb )

	# log v linear
	# ax1.semilogy( ω_range, list_log_omega, color='k', label='log' )

	# log v log
	# ax1.loglog( ω_range, list_log_omega, color='k', label='log' )


	ax1.tick_params(axis='y', labelcolor='k')
	plt.legend()  # adds a legend to label the current curve

	lw:float = 1.0
	# Add a horiz guide line at .01
	plt.hlines( y=ωpoint01_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ωpoint01_dB_crossing_point[0],
		label=f"{ωpoint01_dB_crossing_point[1]}dB@ω=.01",
		color='k', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(100)
	plt.vlines( x=ωpoint01_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ωpoint01_dB_crossing_point[1],
		color='k', linestyle='--', linewidth=lw )

	# Add a horiz guide line at .1
	plt.hlines( y=ωpoint1_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ωpoint1_dB_crossing_point[0],
		label=f"{ωpoint1_dB_crossing_point[1]}dB@ω=.1",
		color='purple', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 1000 that stops at 20log(1000)
	plt.vlines( x=ωpoint1_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ωpoint1_dB_crossing_point[1],
		color='purple', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 1
	plt.hlines( y=ω1_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω1_dB_crossing_point[0],
		label=f"{ω1_dB_crossing_point[1]}dB@ω=1",
		color='g', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω1_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω1_dB_crossing_point[1],
		color='g', linestyle='--', linewidth=lw )

	# Add a horiz guide line at cutoff
	plt.hlines( y=ω_cutoff_crossing_point[1],
		xmin=ω_range[0], xmax=ω_cutoff_crossing_point[0],
		label=f"{ω_cutoff_crossing_point[1]}dB@ω={ω_cutoff_crossing_point[0]}",
		color='r', linestyle='--', linewidth=lw )
	# Add a vertical guide line at cutoff that stops at 20log(ωc)
	plt.vlines( x=ω_cutoff_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω_cutoff_crossing_point[1],
		color='r', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 10
	plt.hlines( y=ω10_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω10_dB_crossing_point[0],
		label=f"{ω10_dB_crossing_point[1]}dB@ω=10",
		color='cyan', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω10_dB_crossing_point[0],
		ymin=list_Tdb[0], ymax=ω10_dB_crossing_point[1],
		color='cyan', linestyle='--', linewidth=lw )



	plt.title( f"{pnum} -- HFP freq resp" )
	plt.text(x=.02, y=0, s=f"Av(max)={K}", fontsize=14, color='k')

	# plt.xlim(left=10)

	# plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=4) )
	# plt.tight_layout()
	# plt.axis('tight')
	plt.legend()  # adds a legend to label the highlighted point
	# plt.show()


	# ----------------------------------------------------------------------------
	# --- phase ------------------------------------------------------------------
	# ----------------------------------------------------------------------------

	list_phase:List[float] = []
	ωpoint01_dB_crossing_point:List[Any] = []  # ω=.01
	ωpoint1_dB_crossing_point:List[Any] = []   # ω=.1
	ω1_dB_crossing_point:List[Any] = []        # ω=1
	ω10_dB_crossing_point:List[Any] = []       # ω=10

	ω_cutoff_crossing_point:List[Any] = []   # (ω/ωc)=1


	K_angle:float = 0
	if( K>0 ):
		K_angle = 0
	elif( K<0 ):
		K_angle = -180
	else:
		print( 'Invalid K val, hard-exit' )
		exit()
	ax1_plot_label_phase:str = f"<K={K_angle}+90-arctan(ω/ωc)"


	# ---- Calcs ---------------------
	for idx, ω in enumerate(ω_range):
		eq:float = 180 / math.pi * math.atan(ω/ωc)
		val2:float = K_angle + 90 - eq     # 2nd Ed, pg 712
		val2 = round(val2,1)
		list_phase.append( val2 )
		if( ω == .01 ):
			ωpoint01_dB_crossing_point = [ω_range[idx],val2]
			print( f"ωpoint01_dB_crossing_point: {ωpoint01_dB_crossing_point}" )
		if( ω == .1 ):
			ωpoint1_dB_crossing_point = [ω_range[idx],val2]
			print( f"ωpoint1_dB_crossing_point: {ωpoint1_dB_crossing_point}" )
		if( ω == ωc_cutoff ):
			ω_cutoff_crossing_point = [ω_range[idx],val2]
			print( f"ω_cutoff_crossing_point: {ω_cutoff_crossing_point}" )
		if( ω == 1 ):
			ω1_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω1_dB_crossing_point: {ω1_dB_crossing_point}" )
		if( ω == 10 ):
			ω10_dB_crossing_point = [ω_range[idx],val2]
			print( f"ω10_dB_crossing_point: {ω10_dB_crossing_point}" )



	fig, ax1 = plt.subplots(constrained_layout=True)  # Create a figure and axis for the first plot
	ax1.set_xlabel('ω')  # shared x-axis
	ax1.set_ylabel('<K deg', color='k')  # Set y-axis label for the first axis

	# linear v log
	# ax1.semilogx( ω_range, list_Tjω, color='b', label=ax1_plot_label_Tjω )
	ax1.semilogx( ω_range, list_phase, color='b', label=ax1_plot_label_phase )

	# log v linear
	# ax1.semilogy( ω_range, list_log_omega, color='k', label='log' )

	# log v log
	# ax1.loglog( ω_range, list_log_omega, color='k', label='log' )


	ax1.tick_params(axis='y', labelcolor='k')
	plt.legend()  # adds a legend to label the current curve

	lw:float = 1.0
	# Add a horiz guide line at .01
	plt.hlines( y=ωpoint01_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ωpoint01_dB_crossing_point[0],
		label=f"{ωpoint01_dB_crossing_point[1]}deg@ω=.01",
		color='k', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(100)
	plt.vlines( x=ωpoint01_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ωpoint01_dB_crossing_point[1],
		color='k', linestyle='--', linewidth=lw )

	# Add a horiz guide line at .1
	plt.hlines( y=ωpoint1_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ωpoint1_dB_crossing_point[0],
		label=f"{ωpoint1_dB_crossing_point[1]}deg@ω=.1",
		color='purple', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 1000 that stops at 20log(1000)
	plt.vlines( x=ωpoint1_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ωpoint1_dB_crossing_point[1],
		color='purple', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 1
	plt.hlines( y=ω1_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω1_dB_crossing_point[0],
		label=f"{ω1_dB_crossing_point[1]}deg@ω=1",
		color='g', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω1_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ω1_dB_crossing_point[1],
		color='g', linestyle='--', linewidth=lw )

	# Add a horiz guide line at cutoff
	plt.hlines( y=ω_cutoff_crossing_point[1],
		xmin=ω_range[0], xmax=ω_cutoff_crossing_point[0],
		label=f"{ω_cutoff_crossing_point[1]}deg@ω={ω_cutoff_crossing_point[0]}",
		color='r', linestyle='--', linewidth=lw )
	# Add a vertical guide line at cutoff that stops at 20log(ωc)
	plt.vlines( x=ω_cutoff_crossing_point[0],
		ymin=list_phase[-1], ymax=ω_cutoff_crossing_point[1],
		color='r', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 10
	plt.hlines( y=ω10_dB_crossing_point[1],
		xmin=ω_range[0], xmax=ω10_dB_crossing_point[0],
		label=f"{ω10_dB_crossing_point[1]}deg@ω=10",
		color='cyan', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 100 that stops at 20log(10)
	plt.vlines( x=ω10_dB_crossing_point[0],
		ymin=list_phase[-1], ymax=ω10_dB_crossing_point[1],
		color='cyan', linestyle='--', linewidth=lw )



	plt.title( f"{pnum} -- HFP freq resp" )

	if( K > 0 ):
		plt.text(x=.02, y=80, s=f"Av(max)={K}", fontsize=14, color='k')
		plt.text(x=.02, y=75, s=f"fc={fc_plot}Hz", fontsize=14, color='k')
		plt.text(x=.02, y=70, s=f"ωc={round(ωc,2)}rad", fontsize=14, color='k')
	else:  # K=-1
		plt.text(x=1.5, y=-150, s=f"Av(max)={K}", fontsize=14, color='k')
		plt.text(x=1.5, y=-160, s=f"fc={fc_plot}Hz", fontsize=14, color='k')
		plt.text(x=1.5, y=70, s=f"ωc={round(ωc,2)}rad", fontsize=14, color='k')

	# plt.xlim(left=10)
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()



# 	ans_string:str = f"""
# """
# 	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
