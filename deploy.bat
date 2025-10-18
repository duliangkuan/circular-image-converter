@echo off
chcp 65001 >nul

echo 🚀 开始部署圆形图片转换器...

echo 📋 检查Python环境...
python --version

echo 🔧 创建虚拟环境...
python -m venv venv

echo ⚡ 激活虚拟环境...
call venv\Scripts\activate.bat

echo 📦 安装依赖包...
pip install -r requirements.txt

echo 📁 创建必要目录...
if not exist uploads mkdir uploads
if not exist outputs mkdir outputs
if not exist templates mkdir templates

echo 🎉 部署完成！启动应用...
echo 📍 访问地址: http://localhost:5000
echo 🔗 API地址: http://localhost:5000/api/convert
echo.
echo 按 Ctrl+C 停止服务

python app.py

pause
