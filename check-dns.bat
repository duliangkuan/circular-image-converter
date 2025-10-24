@echo off
chcp 65001 >nul
echo ========================================
echo DNS解析检查工具
echo ========================================
echo.

set /p SUBDOMAIN="请输入要检查的子域名（例如：api.songgeixiaopengyoudeliwu.icu）: "

if "%SUBDOMAIN%"=="" (
    echo ❌ 子域名不能为空
    pause
    exit /b 1
)

echo.
echo 🔍 正在检查DNS解析...
echo.

echo 📋 使用nslookup检查：
nslookup %SUBDOMAIN%

echo.
echo 📋 使用ping检查：
ping -n 4 %SUBDOMAIN%

echo.
echo ========================================
echo 检查完成！
echo ========================================
echo.
echo 💡 如果看到IP地址，说明DNS解析正常
echo ⏰ 如果解析失败，请等待几分钟后重试
echo.
pause



