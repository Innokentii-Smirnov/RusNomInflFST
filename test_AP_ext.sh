./run_submodule_alone.sh ParadigmFeatures/Alternations/GetAlternations.foma
./run_submodule_alone.sh ParadigmFeatures/NonStandEndings/GetNonStandEndings.foma
./run_submodule_alone.sh ConvRepr/Stem/GetStem
./run_submodule_alone.sh ParadigmFeatures/Star/GetStar.foma
./run_submodule_alone.sh ParadigmFeatures/AP/GetAP.foma
grep -E -w '^(клок|кол|копыл|крюк|лист|лоскут|прут|сук)' ParadigmFeatures/AP/out.txt
