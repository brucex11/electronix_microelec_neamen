from inspect import currentframe
import math
from typing import List, Any  # Tuple, Dict, Set

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from assertions.assertions import assert_within_percentage
from equations.equations import to_s_k, to_s_mA, to_s_uA
from equations.equations import equivalent_parallel_resisitance
from equations.equations import r1_parallel_r2
from equations.equations import current_divider


def test7_log_omega(self):
	"""Plot log(omega) and 20log(omega).
	Sun, Apr 20, 2025  8:28:59 AM
	ANS:  draw Bode-plot."
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

	#  α   β   Ω   μ   λ   γ   ξ   ω  π  τ

	omega_range:List[float] = [round(0.01 + i * 0.01, 2) for i in range(100000)]  # 100000 values from 0.01 to 1000
	# print( omega_range )

	tenthX_crossing_point:List[Any] = []  # ratio is 0.1X
	z0_dB_crossing_point:List[Any] = []   # ratio is 1X (unity)
	sqrt2X_crossing_point:List[Any] = []  # ratio is sqrt(2)X
	twoX_crossing_point:List[Any] = []    # ratio is 2X
	tenX_crossing_point:List[Any] = []    # ratio is 10X

	list_log_omega:List[float] = []

	for idx, ω in enumerate(omega_range):
		val:float = 20 * math.log10( ω )
		list_log_omega.append( val )
		if( ω == 0.1 ):
			tenthX_crossing_point = [omega_range[idx],int(val)]
			print( f"tenthX_crossing_point: {tenthX_crossing_point}" )
		if( ω == 1 ):
			z0_dB_crossing_point = [omega_range[idx],int(val)]
			print( f"z0_dB_crossing_point: {z0_dB_crossing_point}" )
		if( ω == 1.4 ):  # closest to sqrt(2) = 1.414213
			val = round(val,0)
			sqrt2X_crossing_point = [omega_range[idx],int(val)]
			print( f"sqrt2X_crossing_point: {sqrt2X_crossing_point}" )
		if( ω == 2 ):
			twoX_crossing_point = [omega_range[idx],int(val)]
			print( f"twoX_crossing_point: {twoX_crossing_point}" )
		if( ω == 10 ):
			tenX_crossing_point = [omega_range[idx],int(val)]
			print( f"tenX_crossing_point: {tenX_crossing_point}" )


	# Tight_layout() doesn't quite behave as expected with semilog or log-log plots,
	# so use newer implementation with 'constrained_layout=True' parameter.
	# Hm, the above in conjunction with plt.tight_layout() -OR- fig.tight_layout()
	# still does not work (there's still 'margin' between the log-line and the axes).
	fig, ax1 = plt.subplots(constrained_layout=True)  # Create a figure and axis for the first plot
	ax1.set_xlabel('ω/ωo')  # shared x-axis
	ax1.set_ylabel('20log(ω/ωo)', color='k')  # Set y-axis label for the first axis

	# linear v linear ( y v x )
	# ax1.plot( omega_range, list_log_omega, color='r', label='log' )
	# linear v log
	ax1.semilogx( omega_range, list_log_omega, color='k', label='log' )
	# log v linear
	# ax1.semilogy( omega_range, list_log_omega, color='k', label='log' )
	# log v log
	# ax1.loglog( omega_range, list_log_omega, color='k', label='log' )

	lw:float = 2.0
	# Add a horiz guide line at 0.1X that stops at 20log(ω/ωo)
	plt.hlines( y=tenthX_crossing_point[1],
		xmin=omega_range[0], xmax=tenthX_crossing_point[0],
		label=f"{tenthX_crossing_point[1]}dB @ω/ωo=0.1X",
		color='purple', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 10X that stops at 20log(ω/ωo)
	plt.vlines( x=tenthX_crossing_point[0],
		ymin=list_log_omega[0], ymax=tenthX_crossing_point[1],
		color='purple', linestyle='--', linewidth=lw )

	# Add an entire-height horizontal guide line at unity
	# plt.axhline( y=z0_dB_crossing_point[1], color='k', label='unity' , linestyle='--', linewidth=lw )
	# Add an entire-height vertical guide line at unity
	# plt.axvline( x=z0_dB_crossing_point[0], color='k', linestyle='--', linewidth=lw )

	# Add a horiz guide line at unity that stops at 20log(ω/ωo)
	plt.hlines( y=z0_dB_crossing_point[1],
		xmin=omega_range[0], xmax=z0_dB_crossing_point[0],
		label=f"{z0_dB_crossing_point[1]}dB @ω/ωo=unity",
		color='k', linestyle='--', linewidth=lw )
	# Add a vertical guide line at unity that stops at 20log(ω/ωo)
	plt.vlines( x=z0_dB_crossing_point[0],
		ymin=list_log_omega[0], ymax=z0_dB_crossing_point[1],
		color='k', linestyle='--', linewidth=lw )

	# Add a horiz guide line at sqrt(2) that stops at 20log(ω/ωo)
	plt.hlines( y=sqrt2X_crossing_point[1],
		xmin=omega_range[0], xmax=sqrt2X_crossing_point[0],
		label=f"{sqrt2X_crossing_point[1]}dB @ω/ωo=sqrt(2)X",
		color='r', linestyle='--', linewidth=lw )
	# Add a vertical guide line at sqrt(2) that stops at 20log(ω/ωo)
	plt.vlines( x=sqrt2X_crossing_point[0],
		ymin=list_log_omega[0], ymax=sqrt2X_crossing_point[1],
		color='r', linestyle='--', linewidth=lw )


	# Add an entire-height horizontal guide line at 2X
	# plt.axhline( y=twoX_crossing_point[1], color='b', label='2X' , linestyle='--', linewidth=lw )
	# Add an entire-height vertical guide line at 2X
	# plt.axvline( x=twoX_crossing_point[0], color='b', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 2X that stops at 20log(ω/ωo)
	plt.hlines( y=twoX_crossing_point[1],
		xmin=omega_range[0], xmax=twoX_crossing_point[0],
		label=f"{twoX_crossing_point[1]}dB @ω/ωo=2X",
		color='b', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 2X that stops at 20log(ω/ωo)
	plt.vlines( x=twoX_crossing_point[0],
		ymin=list_log_omega[0], ymax=twoX_crossing_point[1],
		color='b', linestyle='--', linewidth=lw )


	# Add an entire-height horizontal guide line at 10X
	# plt.axhline( y=tenX_crossing_point[1], color='g', label='10X' , linestyle='--', linewidth=lw )
	# Add an entire-height vertical guide line at 10X
	# plt.axvline( x=tenX_crossing_point[0], color='g', linestyle='--', linewidth=lw )

	# Add a horiz guide line at 10X that stops at 20log(ω/ωo)
	plt.hlines( y=tenX_crossing_point[1],
		xmin=omega_range[0], xmax=tenX_crossing_point[0],
		label=f"{tenX_crossing_point[1]}dB @ω/ωo=10X",
		color='g', linestyle='--', linewidth=lw )
	# Add a vertical guide line at 10X that stops at 20log(ω/ωo)
	plt.vlines( x=tenX_crossing_point[0],
		ymin=list_log_omega[0], ymax=tenX_crossing_point[1],
		color='g', linestyle='--', linewidth=lw )


	ax1.tick_params(axis='y', labelcolor='k')
	plt.legend()  # adds a legend to label the current curve

	# Diode current - create second y-axis (id1) on to-be-shared x-axis (VPS)
	# ax2 = ax1.twinx()
	# ax2.plot( VPS_x_coord, id1, color='b', label='I(D1)' )  # customize color, recall 'k' = black
	# ax2.set_ylabel('I(D1) A', color='b')  # Set y-axis label for the second axis
	# ax2.tick_params(axis='y', labelcolor='b')
	# plt.legend()  # adds a legend to label the voltage curve

	# drop a point on the graph at the Q_point
	# plt.scatter( x=q_point[0], y=q_point[1], color='black', label=f"Q-point ({q_point[0]}V, {round(q_point[1],5)*1000}mA)" )

	plt.title( f"{pnum} Bode" )
	plt.text(x=0.5, y=58, s='τ=RC=1', fontsize=12, color='k')

	# plt.gca().xaxis.set_major_locator( MaxNLocator(nbins=4) )
	# plt.tight_layout()
	plt.axis('tight')
	plt.legend()  # adds a legend to label the highlighted point
	plt.show()


	ans_string:str = f"""
"""
	print( ans_string )

	print( f"--- END {self.prob_str} ---" )
