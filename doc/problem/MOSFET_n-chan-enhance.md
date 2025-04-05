For an n-channel enhancement-mode MOSFET, when VGS = VDS, the MOSFET operates in the saturation-region:

1. Threshold Voltage (VTN): For the MOSFET to be "on" (conducting), the gate-to-source voltage VGS must be greater than the threshold voltage VTN.  This ensures that a conducting channel forms between the drain and the source.

2. Region of Operation:
   - Cutoff:  When VGS < VTN, the MOSFET is off, and there is no conduction.
   - Linear (Ohmic/Triode):  When VGS > VTN and VDS < (VGS - VTN), the MOSFET operates in the ohmic region.  In this region, the MOSFET behaves like a variable resistor.
   - Saturation:  When VGS > VTN and VDS >= (VGS - VTN), the MOSFET is in the saturation region.  In this region, the drain current is primarily controlled by VGS and is relatively independent of VDS (as long as VDS is above the threshold).

In this case, when VGS = VDS, the MOSFET satisfies the condition for the saturation region, where VDS >= (VGS - VTN).  Therefore, the MOSFET is in the saturation region at VGS = VDS.