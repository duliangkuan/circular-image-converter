# Vercel Python运行时入口文件
from app import app

# 导出Flask应用实例供Vercel使用
handler = app
