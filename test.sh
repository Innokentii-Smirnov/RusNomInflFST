git clean -X
clear
./run_all.sh
cd TestMorph
python evaluate.py "../src/Morphonology/ConvToOrth/out.txt" "../test_data/corr.txt" "../test_result"
