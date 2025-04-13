To discuss the power consumption of a **5-volt peak-to-peak signal** across a **390-ohm resistor**, while ensuring that the power is less than **180 milliwatts (mW)**, we can break it down step-by-step.

### Key Information:
- **Signal voltage**: 5 V peak-to-peak
- **Resistance**: 390 ohms
- **Power consumption**: Less than 180 mW

### Step 1: Find the RMS (Root Mean Square) voltage

For a sinusoidal signal, the **peak-to-peak voltage** \( V_{pp} \) is related to the **RMS voltage** \( V_{rms} \) by the following relationship:

\[
V_{rms} = \frac{V_{pp}}{2\sqrt{2}}
\]

Where \( V_{pp} \) is the peak-to-peak voltage, and \( V_{rms} \) is the RMS voltage.

Given that \( V_{pp} = 5 \, V \), we can calculate the RMS voltage:

\[
V_{rms} = \frac{5}{2\sqrt{2}} = \frac{5}{2.828} \approx 1.77 \, V
\]

### Step 2: Calculate the power

The power dissipated across a resistor is given by the formula:

\[
P = \frac{V_{rms}^2}{R}
\]

Where:
- \( P \) is the power dissipated across the resistor.
- \( V_{rms} \) is the RMS voltage.
- \( R \) is the resistance.

Substitute the values:

\[
P = \frac{(1.77)^2}{390} \approx \frac{3.13}{390} \approx 0.00803 \, \text{W} = 8.03 \, \text{mW}
\]

### Step 3: Check the power consumption condition

The power dissipated across the resistor is approximately **8.03 mW**, which is well below the specified maximum of **180 mW**. Therefore, the signal across the 390-ohm resistor consumes much less than 180 milliwatts of power.

### Conclusion:

With a **5 V peak-to-peak** signal applied across a **390-ohm resistor**, the power dissipated is approximately **8.03 mW**, which is well under the limit of 180 mW. This confirms that the power consumption condition is satisfied.
