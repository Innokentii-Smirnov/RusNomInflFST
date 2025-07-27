@echo off
cls
chcp 65001
echo %1 | lookup src\ParadigmFeatures\NonStandEndings\GetNonStandEndings.bin -q -flags xLL -utf8
