@echo off
call %~dp0env.bat
cd %WINPYDIR%
%WINPYDIR%\python.exe %*