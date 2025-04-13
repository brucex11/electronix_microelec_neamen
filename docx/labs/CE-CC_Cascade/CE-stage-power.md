

For file C:\SourceCode\GitHub\electronix\microelec_neamen\docx\labs\CE-CC_Cascade\LTspice\simulation\CE/casc_ce01.asc


Nice — let's add a **22kΩ resistive load** to the output (collector node) and calculate the **new power consumption**.

---

### ⚙️ Setup Recap (with Load):

- **VCC = 12V**
- **R_C = 6kΩ**
- **R_E = 1kΩ**
- **Transistor collector current (I_C) ≈ 1 mA**
- **Voltage at collector (V_C) ≈ 6V**
- **Load resistor \( R_L = 22 \text{ kΩ} \)** connected from collector to ground

---

### 💡 1. **What Happens When You Add a Load?**

When you connect a **22kΩ load from the collector to ground**, it forms a **parallel combination** with \( R_C \) 
in terms of AC impedance, **but** for **DC power** we treat it as another current path.

---

### 🔋 2. **Power Through the Load Resistor**

Assuming:
- \( V_C = 6V \) (as before, at quiescent)
- Load \( R_L = 22kΩ \)

Then the **current through the load** is:

\[
I_L = \frac{V_C}{R_L} = \frac{6V}{22kΩ} ≈ 0.273 \text{ mA}
\]

Power dissipated in the load:

\[
P_L = V_C \cdot I_L = 6V \cdot 0.273 \text{ mA} ≈ \boxed{1.64 \text{ mW}}
\]

---

### 🔌 3. **Updated Total Power Consumption**

Add it all up:
- Transistor: 5 mW (unchanged)
- Voltage divider: 1.22 mW (unchanged)
- Load: 1.64 mW (new)

\[
P_{total} = 5 + 1.22 + 1.64 = \boxed{7.86 \text{ mW}}
\]

---

### ✅ Summary

| Source            | Power (mW) |
|-------------------|------------|
| Transistor        | 5.00       |
| Voltage Divider   | 1.22       |
| 22kΩ Load         | 1.64       |
| **Total**         | **7.86**   |

---

Let me know if you want to simulate this in LTspice or explore the **AC gain with this load**, since it also affects output impedance and bandwidth.
