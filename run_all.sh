if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
while read -r line; do
	if [[ $line != *'/'* ]]; then
		filepath=src/ParadigmFeatures/$line/Get$line.foma
	else
		filepath=src/$line.foma
	fi
	echo $filepath
	./run_submodule.sh $filepath
done < compilation_order.txt
