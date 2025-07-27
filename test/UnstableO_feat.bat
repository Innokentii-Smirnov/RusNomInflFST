@echo off
if %1 == rebuild (
  run_submodule.bat src\ParadigmFeatures\UnstableO\GetUnstableO.foma
)
find "UnstableO" src\ParadigmFeatures\UnstableO\out.txt | sort
