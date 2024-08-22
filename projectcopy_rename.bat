@echo off
set "SCRIPT_NAME=projectcopy_rename.py"
set "SCRIPT_PATH=%~dp0%SCRIPT_NAME%"

if not exist "%SCRIPT_PATH%" (
    echo Error: Cannot find %SCRIPT_NAME% in the same directory as this batch file.
    echo Please ensure that %SCRIPT_NAME% is in the same folder as this .bat file.
    pause
    exit /b 1
)

python "%SCRIPT_PATH%" %*
if %errorlevel% neq 0 (
    echo An error occurred. Error code: %errorlevel%
    pause
) else (
    echo Script completed successfully.
    pause
)