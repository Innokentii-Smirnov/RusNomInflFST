if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
./run_submodule_alone.sh ParadigmFeatures/$1/Get$1.foma
echo $2 | lookup ParadigmFeatures/$1/Get$1.bin -q
