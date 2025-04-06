# Python Project MICROELEC_NEAMEN
# Electronix Microelectronics
Problems from the textbook: Microelectronics Circuit Analysis and Design, 4th Edition by Donald Neamen.


# ENKI2 Laptop
LTspice component models:  C:\Users\OwnerA\AppData\Local\LTspice\lib\cmp\.

## Generate Virtual Env

```
C:\SourceCode\GitHub\electronix\microelec_neamen>py -0p
 -V:3.12 *        C:\TechRoot\py\3.12.0\python.exe

C:\SourceCode\GitHub\electronix\microelec_neamen> py -3.12 -m venv .venvPy3-12-0  <======
```

## Activate the 3.12.0 Environment and Dump Help
See specific config_*.ini file for details on how to run.

```
C:\SourceCode\GitHub\electronix\microelec_neamen> pyactivate_3-12-0.bat  <======

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\microelec_neamen> python --version  <======
Python 3.12.0

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\microelec_neamen> pip --version  <======
pip 23.2.1 from C:\SourceCode\GitHub\electronix\microelec_neamen\.venvPy3-12-0\Lib\site-packages\pip (python 3.12)

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\microelec_neamen> pip freeze  <======

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\microelec_neamen> cd run

(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\microelec_neamen\run> run.py  <====== dump help

```

## Installations

```
(.venvPy3-12-0) C:\SourceCode\GitHub\electronix\microelec_neamen>pip install scikit-learn
Collecting scikit-learn
  Downloading scikit_learn-1.6.1-cp312-cp312-win_amd64.whl.metadata (15 kB)
Requirement already satisfied: numpy>=1.19.5 in C:\SourceCode\GitHub\electronix\microelec_neamen\.venvpy3-12-0\lib\site-packages (from scikit-learn) (2.2.2)
Collecting scipy>=1.6.0 (from scikit-learn)
  Downloading scipy-1.15.1-cp312-cp312-win_amd64.whl.metadata (60 kB)
Collecting joblib>=1.2.0 (from scikit-learn)
  Downloading joblib-1.4.2-py3-none-any.whl.metadata (5.4 kB)
Collecting threadpoolctl>=3.1.0 (from scikit-learn)
  Downloading threadpoolctl-3.5.0-py3-none-any.whl.metadata (13 kB)
Downloading scikit_learn-1.6.1-cp312-cp312-win_amd64.whl (11.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.1/11.1 MB 22.4 MB/s eta 0:00:00
Downloading joblib-1.4.2-py3-none-any.whl (301 kB)
Downloading scipy-1.15.1-cp312-cp312-win_amd64.whl (43.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.6/43.6 MB 34.7 MB/s eta 0:00:00
Downloading threadpoolctl-3.5.0-py3-none-any.whl (18 kB)
Installing collected packages: threadpoolctl, scipy, joblib, scikit-learn
Successfully installed joblib-1.4.2 scikit-learn-1.6.1 scipy-1.15.1 threadpoolctl-3.5.0

```
