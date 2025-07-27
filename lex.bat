chcp 65001
@echo off
echo %1 | lookup src\ParadigmFeatures\AccentualDeviations\GetAccentualDeviations.bin -q -utf8
