@echo off
set filepath="%1"
for /F "delims=" %%i in (%filepath%) do set directory="%%~dpi"
for /F "delims=" %%i in (%filepath%) do set name="%%~ni"
set binary=%name%.bin
set olddir=%cd%
cd %directory%
xfst -utf8 -e "source %name%.foma" -e "push %name%" -e "invert net" -e "save stack %binary%" -e "sigma" -stop
echo "Created Foma binary %binary%."
if exist in.txt (
	set input=in.txt
	lookup %binary% -utf8 < %input% > loc.txt
)
set beginning=%directory:~33,16%
if %beginning% == ParadigmFeatures (
	set input=../../../test_data/lemmata.txt
) else (
	set input=../../../test_data/in.txt
)
lookup %binary% -utf8 < %input% > out.txt
cd "%olddir%"
