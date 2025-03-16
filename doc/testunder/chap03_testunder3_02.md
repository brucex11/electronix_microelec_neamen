The value of λ = 0 is important because it relates to the **channel-length modulation** effect in MOSFETs. When λ is nonzero, it signifies that there is a small variation in the drain current with changes in the drain-to-source voltage *vDS* due to the shortening of the effective channel length as *vDS* increases. This effect causes a slight increase in current even after the transistor enters saturation.

### THIS ALSO APPLIES TO NMOS DEVICES

In the context of the calculation of the **conduction parameter Kp**, the value of λ doesn't affect the result directly because:

1. **Conduction parameter  Kp**  is related to the intrinsic properties of the MOSFET, such as the mobility of the carriers (μp), the oxide capacitance (Cox), and the geometry of the MOSFET width ( W ) and length ( L ).

2. **Channel-length modulation** (represented by λ) only affects the **drain current** in the saturation region when a voltage is applied between the drain and the source. It impacts the **saturation current** calculation (i.e., the current when the MOSFET is in saturation) but doesn't impact the basic **conduction parameter** *Kp*.

   Specifically, λ comes into play when calculating the drain current in saturation, which has a term (1 + λ * vDS) to account for the slight increase in current due to channel-length modulation.

   The formula for the drain current *ID* in the saturation region is:

   ID = Kp * ( vSG - VTP )^2 * ( 1 + λ * vDS )  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Eq (3.7)**

   However, for the calculation of *Kp* alone, we do not consider the effect of λ, because we are focusing on the transistor's intrinsic properties, not the current-voltage relationship in the saturation region.

### Conclusion:
Since λ = 0 in this case, it confirms that the channel-length modulation effect is neglected (i.e., no dependence of current on *vDS* beyond the saturation region), and thus, it does not affect the calculation of the conduction parameter *Kp*. Therefore, λ  is not used in the calculation of *Kp*.

![](lambda_chan_len_modulation.png)
