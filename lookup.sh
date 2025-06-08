if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
echo $1 | lookup Morphonology/ConvToOrth/ConvToOrth.bin -q
#echo $1 | lookup ParadigmFeatures/AP/GetAP.bin -q
