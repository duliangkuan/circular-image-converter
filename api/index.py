# Vercel Python运行时入口文件
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# 导出Flask应用实例供Vercel使用
handler = app
