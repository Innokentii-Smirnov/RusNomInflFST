./run_submodule_alone.sh ParadigmFeatures/NonStandEndings/GetNonStandEndings.foma
clear
grep -F +Soglbch ParadigmFeatures/NonStandEndings/out.txt
grep -w ^четыре ParadigmFeatures/NonStandEndings/out.txt
