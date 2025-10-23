@echo off
chcp 65001 >nul
echo ========================================
echo 添加新子域名到Vercel
echo ========================================
echo.

REM 检查Vercel CLI
vercel --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Vercel CLI未安装，正在安装...
    npm install -g vercel
)

echo ✅ Vercel CLI已准备就绪
echo.

set /p SUBDOMAIN="请输入完整的子域名（例如：api.songgeixiaopengyoudeliwu.icu）: "

if "%SUBDOMAIN%"=="" (
    echo ❌ 域名不能为空
    pause
    exit /b 1
)

echo.
echo 🔍 先检查DNS解析是否生效...
echo.
nslookup %SUBDOMAIN%
echo.

set /p CONTINUE="DNS解析是否正常？(y/n): "
if /i not "%CONTINUE%"=="y" (
    echo ⏰ 请等待DNS解析生效后再运行此脚本
    pause
    exit /b 1
)

echo.
echo 🚀 正在添加域名到Vercel...
echo.

vercel domains add %SUBDOMAIN%

if %errorlevel% equ 0 (
    echo.
    echo ✅ 域名添加成功！
    echo.
    echo 📊 检查域名状态：
    vercel domains ls
    echo.
    echo 🎉 配置完成！你的网站现在可以通过以下地址访问：
    echo    https://%SUBDOMAIN%
    echo.
) else (
    echo.
    echo ❌ 域名添加失败，可能的原因：
    echo    1. DNS解析尚未生效
    echo    2. 域名已被其他项目使用
    echo    3. 域名格式不正确
    echo.
    echo 💡 请检查DNS配置后重试
)

echo.
pause


