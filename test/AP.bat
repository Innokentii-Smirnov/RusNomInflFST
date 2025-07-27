@echo off
chcp 65001
if %1 == hide (
  run_submodule.bat src\ParadigmFeatures\AP\GetAP.foma
  cls
) else (
  run_submodule.bat src\ParadigmFeatures\AP\GetAP.foma
)
