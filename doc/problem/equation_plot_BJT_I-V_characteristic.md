To plot a **BJT current-voltage relationship**, the most commonly used equations are derived from the **Shockley diode equation** for the base-emitter junction, and they describe the behavior of the **collector current** ((I_C)) with respect to the **base-emitter voltage** ((V_BE)) and the **collector-emitter voltage** ((V_CE)).

### 1. **Shockley Diode Equation (Base-Emitter Junction)**

For a **BJT in active region**, the base-emitter junction behaves like a diode, and the base-emitter voltage ((V_BE)) controls the emitter current ((I_E)). The base-emitter voltage and emitter current are related by the Shockley equation:

I_E = I_S * [ e^(VBE/VT) - 1 ]

Where:
- ( I_E ) = emitter current
- ( I_S ) = saturation current (a small constant specific to the transistor)
- ( VT ) = thermal voltage, approximately 26 mV at room temperature (given by ( V_T = frack Tq ), where ( k ) is Boltzmann's constant, ( T ) is temperature in Kelvin, and ( q ) is the charge of an electron).
- ( VBE ) = base-emitter voltage

Since ( I_C ~= I_E ) for an NPN transistor in active mode (when the base current is much smaller than the emitter current), the **collector current** ( I_C ) is also described by the same equation, ignoring the base current:

I_C = I_S * [ e^(VBE/VT) - 1 ]

This equation describes the exponential relationship between **collector current** (I_C) and **base-emitter voltage** (VBE).

### 2. **Saturation Region (Collector-Emitter Voltage Impact)**

In the **saturation region** of the BJT, when (V_CE) is small, the transistor behaves like a switch that is "on." The relationship between (I_C) and (V_CE) in the saturation region is less sensitive, and ( I_C ) is roughly constant.

However, for higher (V_CE), the transistor enters the **active region**, where the collector current primarily depends on (V_BE) and the equation above holds.

### 3. **Output Characteristics (Collector-Emitter Relationship)**

For **output characteristics** of a BJT (plotting (I_C) vs. (V_CE) for various (V_BE) values), the **collector current** (I_C) is related to both (V_CE) and (V_BE). The simplified version of the equation in the **active region** is:

I_C = I_S left( e^fracV_BEV_T - 1 right) quad textfor quad V_CE > V_CE(sat)

In this active region, the collector current is **largely independent** of (V_CE), as long as (V_CE) is above the saturation voltage ((V_CE(sat))).

For **saturation**:
- When (V_CE) is small, the transistor enters saturation, and (I_C) will become relatively constant, limited by external resistances and the saturation voltage.

### 4. **Kirk Effect (High (V_CE) Consideration)**

At very high **collector-emitter voltages** ((V_CE)), the Kirk effect may also affect the relationship, causing a slight decrease in (I_C). This is a higher-order phenomenon that is typically small in most practical cases.

### General BJT Current-Voltage Relationship (in Active Region):

- **Base-Emitter Junction**:
  [
  I_C = I_S left( e^fracV_BEV_T - 1 right)
  ]
- **Collector-Emitter Voltage**: For the transistor to be in the active region, ( V_CE > V_CE(sat) ), and the collector current is primarily determined by (V_BE) as shown above.

### Conclusion:

The key equation to plot a **BJT current-voltage relationship** for an NPN transistor in the **active region** is:

[
I_C = I_S left( e^fracV_BEV_T - 1 right)
]

Where (I_C) depends exponentially on the base-emitter voltage (V_BE). For a more complete analysis, especially in the output characteristics, (V_CE) would also come into play, but it primarily affects the saturation and active region behavior.