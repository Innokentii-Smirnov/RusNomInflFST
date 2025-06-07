clear
./run_submodule_alone.sh ParadigmFeatures/Alternations/GetAlternations.foma
./run_submodule_alone.sh ParadigmFeatures/NonStandEndings/GetNonStandEndings.foma
./run_submodule_alone.sh ConvRepr/Stem/GetStem
./run_submodule_alone.sh ParadigmFeatures/Star/GetStar.foma
./run_submodule_alone.sh ParadigmFeatures/AP/GetAP.foma
./run_submodule_alone.sh ParadigmFeatures/AccentualDeviations/GetAccentualDeviations.foma
./lex.sh 'басня\|башня\|двойня\|пашня\|песня\|спальня\|часовня'
echo '***'
./lex.sh 'барышня\|деревня\|кухня\|клешня\|яблоня'
echo '***'
./lex.sh шестерня
./lookup.sh пешня
echo '***'
./lex.sh 'сажень'
echo '***'
./lex.sh 'кегля\|пакля\|распря'
