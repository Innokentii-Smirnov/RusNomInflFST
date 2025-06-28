./run_submodule_alone.sh ParadigmFeatures/UnstableO/GetUnstableO.foma
grep -E 'UnstableO' ParadigmFeatures/UnstableO/out.txt | rev | sort | rev
echo '***'
grep -E -w '^(среда|стена|стрела)' ParadigmFeatures/UnstableO/out.txt
