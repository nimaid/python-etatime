@echo off

set ENVNAME=etatime

set ORIGDIR=%CD%
set TESTDIR=%ORIGDIR%\tests

call conda activate %ENVNAME%

echo Running tests...
python -m pytest
if errorlevel 1 goto ERROR

goto DONE

:ERROR
cd %ORIGDIR%
call conda deactivate
echo Tests failed!
exit /B 1

:DONE
cd %ORIGDIR%
call conda deactivate
echo Tests passed!
exit /B 0
