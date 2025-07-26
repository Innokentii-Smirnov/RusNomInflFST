@echo off
for /f %%l in (compilation_order_backslash.txt) do (
	if exist src\%%l.foma (
		run_submodule.bat src\%%l.foma
	) else (
    run_submodule.bat src\ParadigmFeatures\%%l\Get%%l.foma
  )
)
