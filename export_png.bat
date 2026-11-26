@echo off
chcp 65001 >nul
echo 正在執行單頁教學圖卡高畫質轉檔...

set "PYTHON_EXE=C:\Users\User\Desktop\AI_Knowledge_Workspace\.venv\Scripts\python.exe"
if not exist "%PYTHON_EXE%" (
    set "PYTHON_EXE=python"
)

"%PYTHON_EXE%" "%~dp0scripts\generate_png.py" %*
pause
