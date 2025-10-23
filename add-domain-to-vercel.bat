@echo off
chcp 65001 >nul
echo ========================================
echo 将域名添加到已部署的Vercel项目
echo ========================================
echo.

REM 检查Vercel CLI是否已安装
vercel --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未检测到Vercel CLI，正在安装...
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
echo 📋 请输入你的域名信息：
echo.
set /p DOMAIN="请输入主域名（例如：example.com）: "

if "%DOMAIN%"=="" (
    echo ❌ 域名不能为空
    pause
    exit /b 1
)

echo.
echo 🚀 正在将域名添加到Vercel项目...
echo.

REM 添加主域名
echo 📍 添加主域名: %DOMAIN%
vercel domains add %DOMAIN%
if %errorlevel% equ 0 (
    echo ✅ 主域名添加成功
) else (
    echo ⚠️ 主域名添加可能失败，请检查
)

echo.
REM 添加www子域名
echo 📍 添加www子域名: www.%DOMAIN%
vercel domains add www.%DOMAIN%
if %errorlevel% equ 0 (
    echo ✅ www子域名添加成功
) else (
    echo ⚠️ www子域名添加可能失败，请检查
)

echo.
REM 添加pic子域名
echo 📍 添加pic子域名: pic.%DOMAIN%
vercel domains add pic.%DOMAIN%
if %errorlevel% equ 0 (
    echo ✅ pic子域名添加成功
) else (
    echo ⚠️ pic子域名添加可能失败，请检查
)

echo.
echo ========================================
echo 📊 检查域名状态...
echo ========================================
vercel domains ls

echo.
echo ========================================
echo 🎉 域名添加完成！
echo ========================================
echo.
echo 📝 已添加的域名：
echo   • %DOMAIN%
echo   • www.%DOMAIN%
echo   • pic.%DOMAIN%
echo.
echo ⏰ 请等待5-30分钟让DNS解析生效
echo 🔗 然后访问你的网站测试：
echo   • https://%DOMAIN%
echo   • https://www.%DOMAIN%
echo   • https://pic.%DOMAIN%
echo.
echo 💡 如需检查域名状态，运行：vercel domains ls
echo.
pause

