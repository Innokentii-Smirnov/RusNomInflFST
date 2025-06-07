./run_submodule_alone.sh ParadigmFeatures/$1/Get$1.foma
grep -F $2 ParadigmFeatures/$1/out.txt | rev | sort | rev
