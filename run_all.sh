if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
cd ParadigmFeatures
while read -r line; do
	if [[ $line != '..'* ]]; then
		filepath=$line/Get$line.foma
	else
		filepath=$line
	fi
	echo $filepath
	../run_submodule.sh $filepath
done < compilation_order.txt
cd "$(dirname "$0")"
