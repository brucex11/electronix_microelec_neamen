
import inspect
from assertions import assertions

def ez1_03(self):
	"""Page 19:
	Consider n-type GaAs at T = 300 K doped to a concentration of Nd = 2e+16/cm^3.
	Assume mobility values of μn = 6800 cm^2/V-s and μp = 300 cm^2/V-s.
	(a) Determine the resistivity of the material. (b) Determine the applied
	electric field that will induce a drift current density of 175 A/cm^2.
	ANS:  (a) 0.046ohm-cm  (b) 8.04V/cm
	"""
	fcn_name:str = inspect.currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	print( '-----------------------------------------------' )

	tolerance_percent:float = 3.0  # assertion accuracy
	ans_a:float = 0.046   # Ωcm
	ans_b:float = 8.04    # V/cm

	# electron concentration
	Nd = 2e+16  # /cm^3
	# hole and electron mobility
	u_p:float = 300   # cm^2/V-s
	u_n:float = 6800  # cm^2/V-s

	# Because of the difference in magnitudes between the two concentrations,
	# the conductivity is given by:
	#   sigma (σ) = (qev * μ_n * n) + (qev * μ_n * n) ~= (qev * μ_n * n) in units (Ω-cm)^-1
	#     where qev = 1.602e-19 = magnitude of the electronic charge, Joules
	# Since highly doped with donor atoms, sigma (σ) ~= (qev * μ_n * n) in units (Ω-cm)^-1
	sigma:float = self.qev * u_n * Nd

	# Resistivity is one-over conductivity (ie, the reciprocal)
	resv:float = 1.0 / sigma

	try:
		assertions.assert_within_percentage( resv, ans_a, tolerance_percent )
		print( f"CALC sigma = {round(resv,3)}(ohm-cm)" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )

	# Given drift current density, calc the required electric field
	J:float = 175  # A/cm^2

	E_field:float = J * resv

	try:
		assertions.assert_within_percentage( E_field, ans_b, tolerance_percent )
		print( f"CALC E electric field = {round(E_field,3)}V/cm" )
	except AssertionError as e:
		print( f"CALC AssertionError {pnum}: {e}" )
