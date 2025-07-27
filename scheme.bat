@echo off
chcp 65001
echo %1 | lookup src\ParadigmFeatures\GrammRazr\GetGrammRazr.bin -q -flags xLL -utf8 | python ParadigmScheme\get_paradigm_scheme.py grammSystem\RusNomInfl | lookup src\Inflection\ParadigmDefects\ParadigmDefects.bin -q -utf8 | findstr /v "^$"
