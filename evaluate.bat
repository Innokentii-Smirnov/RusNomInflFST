@echo off
set olddir=%cd%
cd TestMorph
python evaluate.py "../src/Morphonology/ConvToOrth/out.txt" "../test_data/corr.txt" "../test_result"
cd %olddir%
