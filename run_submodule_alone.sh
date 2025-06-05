if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
./run_submodule.sh "$1"
