@echo off
chcp 65001
run_submodule.bat src\ParadigmFeatures\NonStandEndings\GetNonStandEndings.foma
if %1 == hide (
  cls
)
