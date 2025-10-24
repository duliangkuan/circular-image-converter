@echo off
chcp 65001 >nul

echo ========================================
echo 圆形图片转换器 - 一键部署脚本
echo ========================================
echo.

echo 📋 检查Python环境...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python未安装或未添加到PATH
    pause
    exit /b 1
)

echo.
echo 🔧 创建虚拟环境...
python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ 创建虚拟环境失败
    pause
    exit /b 1
)

echo.
echo ⚡ 激活虚拟环境...
call venv\Scripts\activate.bat

echo.
echo 📦 安装依赖包...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ 安装依赖失败
    pause
    exit /b 1
)

echo.
echo 📁 创建必要目录...
if not exist uploads mkdir uploads
if not exist outputs mkdir outputs

echo.
echo 🎉 部署完成！启动应用...
echo 📍 访问地址: http://localhost:5000
echo 🔗 API地址: http://localhost:5000/api/convert
echo.
echo 按 Ctrl+C 停止服务
echo.

python app.py

pause
