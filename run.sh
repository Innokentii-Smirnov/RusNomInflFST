./run_submodule_alone.sh src/ParadigmFeatures/$1/Get$1.foma
grep -F $2 src/ParadigmFeatures/$1/out.txt | rev | sort | rev
