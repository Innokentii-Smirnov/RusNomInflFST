if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
while read -r line; do
	if [[ $line != *'/'* ]]; then
		filepath=ParadigmFeatures/$line/Get$line.foma
	else
		filepath=$line.foma
	fi
	echo $filepath
	./run_submodule.sh $filepath
done < compilation_order.txt
