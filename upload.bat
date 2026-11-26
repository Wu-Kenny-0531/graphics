@echo off
chcp 65001 >nul
echo ==================================================
echo   graphics 教學圖卡專案 - 一鍵同步到 GitHub
echo ==================================================

set "GIT_EXE=C:\Users\User\AppData\Local\GitHubDesktop\app-3.7.0\resources\app\git\cmd\git.exe"
if not exist "%GIT_EXE%" (
    set "GIT_EXE=C:\Users\User\AppData\Local\GitHubDesktop\app-3.6.11\resources\app\git\cmd\git.exe"
)
if not exist "%GIT_EXE%" (
    set "GIT_EXE=git"
)

echo [1/3] 正在加入變更檔案...
"%GIT_EXE%" add .

set /p COMMIT_MSG="請輸入 Commit 訊息 (直接按 Enter 預設為 'update: 更新圖卡專案內容'): "
if "%COMMIT_MSG%"=="" set COMMIT_MSG=update: 更新圖卡專案內容

echo [2/3] 正在提交 Commit: %COMMIT_MSG%
"%GIT_EXE%" commit -m "%COMMIT_MSG%"

echo [3/3] 正在推送到 GitHub...
"%GIT_EXE%" push

echo.
echo ✔ 同步完成！
pause
