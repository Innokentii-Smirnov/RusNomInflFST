@echo off
chcp 65001
if %1 == rebuild (
  run_submodule.bat src\Inflection\ParadigmDefects\ParadigmDefects.foma
)
find "ParDef" src\Inflection\ParadigmDefects\out.txt | sort
