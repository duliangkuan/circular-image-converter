@echo off
chcp 65001 >nul

echo ========================================
echo Vercel域名配置脚本
echo ========================================
echo.

REM 检查Vercel CLI
vercel --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Vercel CLI未安装，正在安装...
    npm install -g vercel
    if %errorlevel% neq 0 (
        echo ❌ 安装失败，请手动安装：npm install -g vercel
        pause
        exit /b 1
    )
    echo ✅ Vercel CLI安装成功！
) else (
    echo ✅ Vercel CLI已安装
)

echo.
echo 🔐 请先登录Vercel账户...
vercel login

echo.
echo 📋 请输入域名信息：
echo.
set /p DOMAIN="请输入完整域名（例如：api.example.com）: "

if "%DOMAIN%"=="" (
    echo ❌ 域名不能为空
    pause
    exit /b 1
)

echo.
echo 🚀 正在添加域名到Vercel项目...
echo.
vercel domains add %DOMAIN%

if %errorlevel% equ 0 (
    echo.
    echo ✅ 域名添加成功！
    echo.
    echo 📊 检查域名状态：
    vercel domains ls
    echo.
    echo 🎉 配置完成！你的网站现在可以通过以下地址访问：
    echo    https://%DOMAIN%
    echo.
    echo 💡 如果域名无法访问，请检查DNS配置并等待解析生效
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
