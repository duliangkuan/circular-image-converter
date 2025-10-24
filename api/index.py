# Vercel Python运行时入口文件
import sys
import os

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

try:
    # 导入Flask应用
    from app import app
    
    # 导出Flask应用实例供Vercel使用
    handler = app
    
except Exception as e:
    # 如果导入失败，创建一个简单的错误处理应用
    from flask import Flask, jsonify
    
    error_app = Flask(__name__)
    
    @error_app.route('/')
    def error_handler():
        return jsonify({
            'error': '应用启动失败',
            'message': str(e)
        }), 500
    
    @error_app.route('/<path:path>')
    def catch_all(path):
        return jsonify({
            'error': '应用启动失败',
            'message': str(e)
        }), 500
    
    handler = error_app