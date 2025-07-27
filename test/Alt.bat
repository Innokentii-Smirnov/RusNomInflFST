@echo off
chcp 65001
if %1 == hide (
  run_submodule.bat src\ParadigmFeatures\Alternations\GetAlternations.foma
  cls
) else (
  run_submodule.bat src\ParadigmFeatures\Alternations\GetAlternations.foma
)
