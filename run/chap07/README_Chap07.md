# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics Chap 07
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.

Figures and notes for all `./subdir` examples, exercises, and problems for this
chapter are contained in MSWord docx located in the `./docx/` folder.
Don't forget to update .gitignore to preclude .docx binaries from repository.

# Search This Document
Use the keywords below for python-code implementations, problems with plots, etc.
When applicable, each problem has keywords that reflect code in that problem.

## Available Keywords
* `bode_plot`  `time_constant`  `plot_example`
* `Av`  `20log`
* `3dB_cutoff_freq`  `beta_cutoff_freq`


# Examples, Exercises, Test Your Understanding, and Problems
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.X):

X.X: Description
* worked-file PATH, textbook page num
* associated word docx (optional)  ./docx/chap07/problem/probX_XX.docx
* LTspice folder (optional)   ./LTspice/chap07/probX_XX
* keywords list `YYY ZZZ`(optional)


## Examples
7.1: For the equivalent ...
* example/exam7_01.py, textbook page 483
* .\docx\chap07\example\exam7_01.docx
* keywords: `time_constant`

7.8: Determine the 3 dB frequency of the short-circuit current gain for BJT.
See function Chap07.beta_cutoff_freq(...).
* example/exam7_08.py, textbook page 505
* keywords: `3dB_cutoff_freq`  `beta_cutoff_freq`


## Exercises
X.X: DESCRIPTION.
* exercise/exerX_XX.py, textbook page PP
* keywords: `YYY ZZZ`


## Test Your Understanding
log.omega: Plot the Bode-plot for τ=RC=1.
* test/test7_log_omega.py, see textbook pg 474
* .\docx\chap07\test\test7_log_omega.docx
* keywords: `bode_plot`  `time_constant`  `plot_example`

### Compare semilog vs linear plot
Very obvious why semilog plot is used:

![bode-plot](../../docx/chap07/testunder/bode_plot_tau=RC=1_semilog.png)

![bode-plot](../../docx/chap07/testunder/bode_plot_tau=RC=1_linear.png)

7.1: For the equivalent circuit shown in Figure 7.13, the parameters are:
RS = 1kΩ, rpi = 2kΩ, RL = 4kΩ, gm = 50mA/V, and CC = 1μF.
(a) Determine the expression for the circuit time constant.
* test/test7_01.py, textbook page 483
* .\docx\chap07\example\chap07_exam7_01_timeconst.docx
* keywords: `time_constant`


## Problems
X.X: DESCRIPTION.
* problem/probX_XX.py, textbook page PP


## Blitz
blitz01: Top-left circuit:
Find the total frequency response.
cpi = 5pF, cu = 2pF, Beta = 100, and VA = 150V.
* ./chap07/blitz/Blitz_Sophia_Freq_response_schematics.pdf.
* ./LTspice/chap07/blitz01/.
* ./docx/chap07/blitz/blitz01.docx
* keywords: `time_constant`  `Av`  `20log`

blitz01_HPF: Top-left circuit:
Find the total frequency response.
cpi = 5pF, cu = 2pF, Beta = 100, and VA = 150V.
* ./chap07/blitz/Blitz_Sophia_Freq_response_schematics.pdf.
* ./LTspice/chap07/blitz01/.
* ./docx/chap07/blitz/blitz01.docx
* keywords: `bode_plot`  `time_constant`  `plot_example`



# Notes
* Pg XX: 
