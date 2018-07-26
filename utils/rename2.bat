@echo off
setlocal enableextensions enabledelayedexpansion

for %%f in (*.png) do (
    set FileName=%%~nf
    set FileName=!FileName:_prediction=!
    set FileName=00000!FileName!
    set FileName=!FileName:~-6!
    set FileName=!FileName!_prediction%%~xf
    rename "%%f" "!FileName!"
)