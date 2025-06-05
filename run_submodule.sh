filepath="$1"
directory=$(dirname $filepath)
name=$(basename $filepath .foma)
binary=$name.bin
olddir=$(pwd)
cd $directory
xfst -utf8 -e "source $name.foma" -e "push $name" -e "invert net" -e "save stack $binary" -e "sigma" -stop
echo "Created Foma binary $binary."
if [ -f in.txt ]; then
	input=in.txt
	lookup $binary -utf8 < $input > loc.txt
fi
echo $directory
if [[ $directory == 'ParadigmFeatures'* ]]; then
	input=../../lemmata.txt
else
	input=../../in.txt
fi
lookup $binary -utf8 < $input > out.txt
cd "$olddir"
