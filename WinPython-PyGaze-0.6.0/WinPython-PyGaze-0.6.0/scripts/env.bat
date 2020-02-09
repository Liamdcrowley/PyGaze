@echo off
set WINPYDIR=%~dp0..\python-2.7.3
set WINPYVER=2.7.3.3
set HOME=%WINPYDIR%\..\settings
set PATH=%WINPYDIR%\Lib\site-packages\PyQt4;%WINPYDIR%\;%WINPYDIR%\DLLs;%WINPYDIR%\Scripts;%WINPYDIR%\..\tools;%WINPYDIR%\..\tools\gnuwin32\bin;%WINPYDIR%\..\tools\mingw32\bin;%PATH%;%WINPYDIR%\..\tools\TortoiseHg