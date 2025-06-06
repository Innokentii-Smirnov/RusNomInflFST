./run_submodule_alone.sh ParadigmFeatures/NonStandEndings/GetNonStandEndings.foma
clear
grep -F +Soglbch ParadigmFeatures/NonStandEndings/out.txt
grep -w $1 ParadigmFeatures/NonStandEndings/out.txt
