clear
./run_submodule_alone.sh ParadigmFeatures/MorphGender/GetMorphGender.foma
grep -F 'bch' ParadigmFeatures/MorphGender/out.txt
echo "***"
grep -F 'еро+' ParadigmFeatures/MorphGender/out.txt
echo "***"
grep -w '.*дцать' ParadigmFeatures/MorphGender/out.txt
echo "***"
grep -w '.*десят' ParadigmFeatures/MorphGender/out.txt
echo "***"
grep -w '.*сот' ParadigmFeatures/MorphGender/out.txt
