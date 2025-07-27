@echo off
if %1 == rebuild (
  run_submodule.bat src\ParadigmFeatures\ParadigmDefects\GetParadigmDefects.foma
)
find "ParDef" src\ParadigmFeatures\ParadigmDefects\out.txt | sort
