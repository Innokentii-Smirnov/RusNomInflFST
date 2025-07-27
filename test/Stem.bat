@echo off
chcp 65001
if %1 == hide (
  run_submodule.bat src\ConvRepr\Stem\GetStem.foma
  cls
) else (
  run_submodule.bat src\ConvRepr\Stem\GetStem.foma
)
