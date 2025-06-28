clear
if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
echo $1 | lookup src/ParadigmFeatures/GrammRazr/GetGrammRazr.bin -q -flags xLL | \
python python/scripts/get_paradigm_scheme.py | \
lookup src/Morphonology/ConvToOrth/ConvToOrth.bin -q | \
sed /^$/d
