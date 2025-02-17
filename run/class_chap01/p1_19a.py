import inspect
import math
from scipy.constants import Boltzmann

from assertions import assertions

def p1_19a(self):
	"""
	Determine the built-in potential barrier Vbi in a silicon pn junction for
	(i) Nd = Na = 5.e+15/cm-cubed; (ii) Nd = 5.e+17/cm+e3 and Na = 1.+e15/cm^3;
	(iii) Na = Nd = 1.+e18/cm^3.
	ANS: 1.19 (a) (i) 0.661V, (ii) 0.739V, (iii) 0.937V
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( f"Problem: {self.prob_str}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	ans_i:float = 0.661
	ans_ii:float = 0.739
	ans_iii:float = 0.937

	print( 'For the pn junction in thermal equilibrium, the voltage due to diffusion of holes and electrons' )
	print( 'is called the built-in potential barrier, or built-in voltage Vbi:' )
	print( '  Vbi = (kT/e)ln[(Na*Nd/ni^2)]' )
	print( f"    where: k == Boltzmann's constant: {Boltzmann} Joules / Kelvin" )
	print(  '           T == abs temp in Kelvin' )
	print(  '           e == magnitude of the electronic charge' )
	print(  '           Na == net acceptor concentration in the p-region' )
	print(  '           Nd == net donor concentration in the n-region' )
	print(  '           ni == intrinsic carrier concentration' )
	print( f"    and Vthermal @ room-temp (300K) == kT/e = {self.vthrml0_026}V" )
	print( '-----------------------------------------------' )

	# Initialize constants
	pnum:str = f"{self.prob_str}(i)"
	Na:float = 5.0e+15		# net acceptor concentration in the p-region
	Nd:float = 5.0e+15		# net donor concentration in the n-region
	ni:float = 1.5e+10		# intrinsic carrier concentration

	# Start calculations
	# The natural logarithm is only defined for positive numbers (x > 0).
	# math.log(x) computes ln(x) for positive values of x.
	vbi = self.vthrml0_026 * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( vbi, ans_i, 1.0 )
		print( f"CALC {pnum}:\tfor silicon, Vbi = {round(vbi, 3)}V" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	pnum:str = f"{self.prob_str}(ii)"
	Na:float = 1.0e+15		# net acceptor concentration in the p-region
	Nd:float = 5.0e+17		# net donor concentration in the n-region
	vbi = self.vthrml0_026 * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( vbi, ans_ii, 1.0 )
		print( f"CALC {pnum}:\tfor silicon, Vbi = {round(vbi, 3)}V" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )


	pnum:str = f"{self.prob_str}(iii)"
	Na:float = 1.0e+18		# net acceptor concentration in the p-region
	Nd:float = 1.0e+18		# net donor concentration in the n-region
	vbi = self.vthrml0_026 * math.log( Na * Nd / ni**2 )
	try:
		assertions.assert_within_percentage( vbi, ans_iii, 1.0 )
		print( f"CALC {pnum}:\tfor silicon, Vbi = {round(vbi, 3)}V" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
