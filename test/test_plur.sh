clear
./run_submodule_alone.sh ParadigmFeatures/Alternations/GetAlternations.foma
./run_submodule_alone.sh ParadigmFeatures/NonStandEndings/GetNonStandEndings.foma
./run_submodule_alone.sh ConvRepr/Stem/GetStem
./run_submodule_alone.sh ParadigmFeatures/Star/GetStar.foma
./run_submodule_alone.sh ParadigmFeatures/AP/GetAP.foma
./run_submodule_alone.sh ParadigmFeatures/AccentualDeviations/GetAccentualDeviations.foma
grep -E -w '^(камень|повод|полоз)'  ParadigmFeatures/AccentualDeviations/out.txt
