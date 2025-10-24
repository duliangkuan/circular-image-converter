# Vercel Python运行时入口文件
import os
import sys

# 设置Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# 导入Flask应用
from app import app

# 导出给Vercel使用
handler = app