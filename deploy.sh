#!/bin/bash

# 圆形图片转换器 - 一键部署脚本

echo "🚀 开始部署圆形图片转换器..."

# 检查Python版本
echo "📋 检查Python环境..."
python3 --version

# 创建虚拟环境
echo "🔧 创建虚拟环境..."
python3 -m venv venv

# 激活虚拟环境
echo "⚡ 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📦 安装依赖包..."
pip install -r requirements.txt

# 创建必要的目录
echo "📁 创建必要目录..."
mkdir -p uploads
mkdir -p outputs
mkdir -p templates

# 设置权限
echo "🔐 设置文件权限..."
chmod +x app.py

# 启动应用
echo "🎉 部署完成！启动应用..."
echo "📍 访问地址: http://localhost:5000"
echo "🔗 API地址: http://localhost:5000/api/convert"
echo ""
echo "按 Ctrl+C 停止服务"

python app.py
