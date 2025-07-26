@echo off
chcp 65001
echo %1 | lookup src\ParadigmFeatures\GrammRazr\GetGrammRazr.bin -q -flags xLL -utf8 | python python\scripts\get_paradigm_scheme.py | lookup src\Morphonology\ConvToOrth\ConvToOrth.bin -q -utf8 | findstr /v "^$"
