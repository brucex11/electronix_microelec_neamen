
from inspect import currentframe

def prob3_19(self):
	"""Page 196:
	Enhancement-mode NMOS and PMOS devices both have parameters
	L = 4μm and tox = 500°A.  For the NMOS transistor, VTN = +0.6V,
	μn = 675cm^2/V-s, and the channel width is Wn; for the PMOS transistor,
	VTP = -0.6V, μp = 375cm^2/V-s, and the channel width is Wp. Design
	the widths of the two transistors such that they are electrically equivalent
	and the drain current in the PMOS transistor is ID = 0.8mA when it is
	biased in the saturation region at VSG = 5V.
	What are the values of Kn, Kp, Wn, and Wp?
	ANS   Kn = Kp = 41.3μA/V^2, Wn = 7.09μm, Wp = 12.8μm.
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


	ans_string:str = """
The driver/goal for electrical equivalence is that the drain current in the PMOS
transistor is ID = 0.8mA when it is biased in the saturation region at VSG = 5V.
Therefore, solve for Kp using the PMOS source-drain current equation in saturation:

    iSD = Kp(vSG + VTP)^2

Also, since tox (oxide thickness) and L (channel length) for both devices are
fixed, solve for W (channel width) per Kp via the process conduction parameters
k'p and k'n:

    k'p = up * Cox    k'n = un * Cox

For silicon devices, eox = (3.9)(8.85e-14) F/cm.
"""
	print( ans_string )

	print( "---- (Cox) --------------------------------------------------------" )
	eox:float =  (3.9)*(8.85e-14)   # (oxide permittivity) εox = F/cm
	tox_A:float = 500    # Angstrom
	tox:float = self.angstroms_per_meter( angstroms=tox_A, units='cm' )
	Cox:float = self.calc_MOSFET_oxide_capacitance( eox=eox, tox=tox )
	print( f"---Cox = {Cox}" )

	print( "\n---- (k'p and k'n) ----------------------------------------------" )
	up:float = 375   # cm^2/V-s
	k_prime_p:float = up * Cox
	print( f"---k'p = {k_prime_p}" )

	un:float = 675   # cm^2/V-s
	k_prime_n:float = un * Cox
	print( f"---k'n = {k_prime_n}" )

	ans_string = """
Given PMOS operation in saturation, use equation for saturation current:

    iSD = (k'p/2)(W/L)(VSG + VTP)^2

and solve for W/L.
"""
	print( ans_string )

	vSG_given:float = 5   # V
	VTP:float = -0.6      # V
	iSD:float = 0.8e-03   # A
	print( f"Given: vSG={vSG_given}V, VTP={VTP}V, iD=0.8mA" )

	print( "---- (Wp) ---------------------------------------------------------" )
	WoverL:float = iSD * ( 2 / k_prime_p ) / ( vSG_given + VTP )**2
	print( f"--- (W/L)p = {WoverL}" )

	Lpn:float = 4e-06   # meter
	Wp = WoverL * Lpn
	print( f"and since Lpn is given as {Lpn}m, it follows that Wp = {round(Wp,7)}m" )

	ans_string = """
Finally for PMOS, the (trans)conduction parameter, Kp, is calculated using:

    Kp = (k'p/2)(W/L)  A/V^2.
"""
	print( ans_string )

	print( "---- (Kp) ---------------------------------------------------------" )
	Kp:float = ( k_prime_p / 2) * WoverL
	print( f"--- Kp = {round(Kp,7)}A/V^2" )

	ans_string = """
For electrical equivalence, Kn must equal Kp.  Since L is the same for both
devices, then Wn must be adjusted for the NMOS device.

    Kn == Kp, and so Kn = (k'n/2)(W/L)n

Solve for W/Ln and then Wn.
"""
	print( ans_string )

	print( '---- (Wn) ---------------------------------------------------------' )
	WoverL = Kp * 2 / k_prime_n
	Wn:float = WoverL * Lpn
	print( f"Since Lpn is given as {Lpn}m, it follows that Wn = {round(Wn,8)}m" )

	print( '\n---- (Final Answers) ----------------------------------------------' )
	print( f" Kn = Kp = {round(Kp,7)}/V^2\n Wn = {round(Wn,8)}m\n Wp = {round(Wp,7)}m.")

	print( f"\n--- END {self.prob_str} ---" )
