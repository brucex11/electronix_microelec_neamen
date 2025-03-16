# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics Chap 05
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.

Figures and notes for all `./subdir` examples, exercises, and problems for this
chapter are contained in MSWord docx located in the `./docx/` folder.
Don't forget to update .gitignore to preclude .docx binaries from repository.

# Search This Document
Use the keywords below for python-code implementations, problems with plots, etc.
When applicable, each problem has keywords that reflect code in that problem.

## Available Keywords
* `Alpha  Beta  reverse_saturation_current  active_region`
* `iE_EQ_iC_plus_iB  KVL_transistor`


# Examples, Exercises, Test Your Understanding, and Problems
All worked sections are listed in order by number in their prospective category.
Here is the format for each problem number (X.XX):

X.X: Description
* worked-file PATH, textbook page XXX
* associated word docx (optional)
* LTspice folder (optional)
* keywords list `YYY ZZZ`(optional)


## Examples
X.X: DESCRIPTION.
* example/examX_XX.py, page XXX
* keywords: `YYY ZZZ`


## Exercises
X.X: DESCRIPTION.
* exercise/exerX_XX.py, page XXX
* keywords: `YYY ZZZ`


## Test Your Understanding
TYU 5.X: Per Exercise EX 1.8, Fig 1.28, determine VD and ID, using the graphical technique.
* ./chap01/testunder/test1_09, pg XXX


## Problems
5.2: A bipolar transistor is biased in the forward-active mode.  Determine
Beta, Alpha, and iB.
* problem/prob5_02.py, page 352
* keywords: `Alpha  Beta`

5.10: An npn transistor has a reverse-saturation current of IS = 5e-15A...
* problem/prob5_10.py, page 353
* keywords: `Alpha  Beta  reverse_saturation_current  active_region`

5.17: For all the transistors in Figure P5.17, β = 75.
* problem/prob5_17.py, page 353
* keywords: `iE_EQ_iC_plus_iB  KVL_transistor`


# Notes
* Pg 287: Since the transistor has two pn junctions, `four possible bias combinations`
may be applied to the device, depending on whether a forward or reverse bias
is applied to each junction.
* Pg 287: For the transistor applied as an amplifying device, the `base–emitter`
`(B–E) junction is forward biased` and the
`base–collector` `(B–C) junction is reverse biased`, in a configuration called
the forward-active operating mode, or simply the `active region`.

![](../../doc/mdimg/chap05_npn_bjt_active_region.png)

* Pg XXX: 
* Pg XXX: 
* Pg XXX: 
* Pg XXX: 
* Pg XXX: 
* Pg XXX: 
