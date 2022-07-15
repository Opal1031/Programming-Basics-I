@echo on
setx path "%PATH%;%USERPROFILE%/AppData/Local/Programs/Python/Python310/Scripts"
c:
cd %USERPROFILE%/AppData/Local/Programs/Python/
dir
pause
cd Python310/Scripts
pip list
pip install jupyter notebook
pip install numpy
pip install matplotlib
pause