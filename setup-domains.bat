@echo off
echo ========================================
echo 自动配置Vercel域名脚本
echo ========================================

REM 检查是否已安装Vercel CLI
vercel --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装Vercel CLI...
    npm install -g vercel
    if %errorlevel% neq 0 (
        echo 错误：无法安装Vercel CLI，请手动安装
        echo 运行命令：npm install -g vercel
        pause
        exit /b 1
    )
)

echo.
echo 请先登录Vercel账户...
vercel login

echo.
echo 请输入你的域名（不含www前缀，例如：example.com）:
set /p DOMAIN=

if "%DOMAIN%"=="" (
    echo 错误：域名不能为空
    pause
    exit /b 1
)

echo.
echo 正在添加域名到Vercel项目...
echo.

REM 添加主域名
echo 添加主域名: %DOMAIN%
vercel domains add %DOMAIN%

REM 添加www子域名
echo.
echo 添加www子域名: www.%DOMAIN%
vercel domains add www.%DOMAIN%

REM 添加pic子域名
echo.
echo 添加pic子域名: pic.%DOMAIN%
vercel domains add pic.%DOMAIN%

echo.
echo ========================================
echo 域名添加完成！
echo ========================================
echo.
echo 已添加的域名：
echo - %DOMAIN%
echo - www.%DOMAIN%
echo - pic.%DOMAIN%
echo.
echo 请等待几分钟让DNS解析生效，然后访问你的网站。
echo.
echo 检查域名状态：
echo vercel domains ls
echo.
pause
