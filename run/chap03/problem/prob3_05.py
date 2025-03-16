
from inspect import currentframe

def prob3_05(self):
	"""Page 194:
	The threshold voltage of each transistor in Figure P3.5 is VTN = 0.4V.
	Determine the region of operation of the transistor in each circuit.
	ANS (a) saturation  (b) ohmic  (c) cutoff
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}\nSolution"
	print( f"Problem: {pnum}" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------' )


	VTN_given:float = 0.4   # V

	ans_string:str = """
The devices per schematic symbol are n-channel enhancement-mode.  This is
confirmed by the given threshold voltage as `VTN` (vs `VTP`) -AND- VTN > 0.

For each device, calculate VDS(sat) and compare against VDS:
* if VDS > VDS(sat), operation is saturation-region
* if VDS < VDS(sat), operation is ohmic-region
* if VG == VS, VDS is a don't-care, operation is cutoff

Given:  VTN = +0.4V.
"""
	print( ans_string )

	print( '---- (a) -------------------------------------------' )
	VG:float = 2.2   # V, per the schematic
	VD:float = 2.2   # V, per the schematic
	VS:float = 0     # gnd, per the schematic
	VGS:float = VG - VS   # V
	VDS:float = VD - VS   # V
	VDS_sat:float = round(VGS - VTN_given, 2)

	print( f"Per the schematic, VGS = {VGS}V, VDS = {VDS}V." )
	print( f"Therefore, VDS(sat) = VGS - VTN = {VDS_sat}V." )
	if( VGS == 0 ):
		print( f"Since VGS = {VGS}V, operation-region is cutoff." )
	elif( VDS > VDS_sat ):
		print( f"Since VDS > VDS(sat), operation-region is saturation." )
	elif( VDS <= VDS_sat ):
		print( f"Since VDS <= VDS(sat), operation-region is ohmic/nonsaturation." )

	print( '---- (b) -------------------------------------------' )
	VG = 0      # gnd, per the schematic
	VD = -0.6   # V, per the schematic
	VS = -1     # V, per the schematic
	VGS = VG - VS   # V
	VDS = VD - VS   # V
	VDS_sat = round(VGS - VTN_given, 2)

	print( f"Per the schematic, VGS = {VGS}V, VDS = {VDS}V." )
	print( f"Therefore, VDS(sat) = VGS - VTN = {VDS_sat}V." )
	if( VGS == 0 ):
		print( f"Since VGS = {VGS}V, operation-region is cutoff." )
	elif( VDS > VDS_sat ):
		print( f"Since VDS > VDS(sat), operation-region is saturation." )
	elif( VDS <= VDS_sat ):
		print( f"Since VDS <= VDS(sat), operation-region is ohmic/nonsaturation." )

	print( '---- (c) -------------------------------------------' )
	VG = 1    # V, per the schematic
	VD = 3    # V, per the schematic
	VS = 1    # V, per the schematic
	VGS = VG - VS   # V
	VDS = VD - VS   # V
	VDS_sat = round(VGS - VTN_given, 2)

	print( f"Per the schematic, VGS = {VGS}V, VDS = {VDS}V." )
	print( f"Therefore, VDS(sat) = VGS - VTN = {VDS_sat}V." )
	if( VGS == 0 ):
		print( f"Since VGS = {VGS}V, operation-region is cutoff." )
	elif( VDS > VDS_sat ):
		print( f"Since VDS > VDS(sat), operation-region is saturation." )
	elif( VDS <= VDS_sat ):
		print( f"Since VDS <= VDS(sat), operation-region is ohmic/nonsaturation." )

	print( f"--- END {self.prob_str} ---" )
