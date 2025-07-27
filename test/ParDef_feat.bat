@echo off
chcp 65001
if %1 == rebuild (
  run_submodule.bat src\ParadigmFeatures\ParadigmDefects\GetParadigmDefects.foma
)
find "ParDef" src\ParadigmFeatures\ParadigmDefects\out.txt | sort
