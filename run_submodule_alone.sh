if [[ ":$PATH:" != *":~/xfst:"* ]]; then
	export PATH=~/xfst:$PATH
fi
filepath="$1"
directory=$(dirname $filepath)
name=$(basename $filepath .foma)
binary=$name.bin
olddir=$(pwd)
cd $directory
xfst -utf8 -e "source $name.foma" -e "push $name" -e "invert net" -e "save stack $binary" -e "sigma" -stop
echo "Created Foma binary $binary."
lookup $binary -utf8 < in.txt > out.txt
cd "$olddir"
