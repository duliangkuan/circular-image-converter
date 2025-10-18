# 圆形图片转换网站 - Flask后端
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
import base64
import io
from PIL import Image, ImageDraw
import os
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 配置
UPLOAD_FOLDER = '/tmp/uploads'  # Vercel使用/tmp目录
OUTPUT_FOLDER = '/tmp/outputs'  # Vercel使用/tmp目录
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}

# 创建必要的文件夹（仅在非Vercel环境）
if not os.environ.get('VERCEL'):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_circular_image(image_data, size=None):
    """将图片转换为圆形轮廓"""
    try:
        # 打开图片
        image = Image.open(io.BytesIO(image_data))
        
        # 转换为RGBA模式以支持透明度
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        # 如果指定了尺寸，调整图片大小
        if size:
            image = image.resize((size, size), Image.Resampling.LANCZOS)
        
        # 获取图片尺寸
        width, height = image.size
        
        # 创建圆形遮罩
        mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(mask)
        
        # 计算圆形区域（以图片中心为圆心，取较小边的一半作为半径）
        radius = min(width, height) // 2
        center_x, center_y = width // 2, height // 2
        
        # 绘制白色圆形
        draw.ellipse(
            [center_x - radius, center_y - radius, 
             center_x + radius, center_y + radius], 
            fill=255
        )
        
        # 应用圆形遮罩
        image.putalpha(mask)
        
        return image
    except Exception as e:
        raise Exception(f"图像处理失败: {str(e)}")

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/api/convert', methods=['POST'])
def convert_image():
    """API接口：转换图片为圆形"""
    try:
        # 获取请求数据
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': '请求数据为空'
            }), 400
        
        # 获取图片数据
        image_data = None
        image_base64 = data.get('image_base64', '')
        size = data.get('size', None)  # 可选：指定输出尺寸
        
        if not image_base64:
            return jsonify({
                'success': False,
                'error': '缺少图片数据'
            }), 400
        
        # 解码base64图片数据
        try:
            # 移除data:image前缀（如果有）
            if ',' in image_base64:
                image_base64 = image_base64.split(',')[1]
            
            image_data = base64.b64decode(image_base64)
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'图片数据解码失败: {str(e)}'
            }), 400
        
        # 转换为圆形图片
        try:
            circular_image = create_circular_image(image_data, size)
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
        
        # 将处理后的图片转换为base64
        output_buffer = io.BytesIO()
        circular_image.save(output_buffer, format='PNG')
        output_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
        
        return jsonify({
            'success': True,
            'image_base64': output_base64,
            'message': '图片已成功转换为圆形轮廓',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'服务器内部错误: {str(e)}'
        }), 500

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """文件上传接口"""
    try:
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'error': '没有上传文件'
            }), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': '没有选择文件'
            }), 400
        
        if file and allowed_file(file.filename):
            # 读取文件数据
            file_data = file.read()
            
            # 转换为圆形图片
            try:
                circular_image = create_circular_image(file_data)
            except Exception as e:
                return jsonify({
                    'success': False,
                    'error': str(e)
                }), 500
            
            # 转换为base64返回（Vercel环境不保存文件）
            output_buffer = io.BytesIO()
            circular_image.save(output_buffer, format='PNG')
            output_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
            
            filename = f"{uuid.uuid4()}.png"
            
            return jsonify({
                'success': True,
                'image_base64': output_base64,
                'filename': filename,
                'message': '图片已成功转换为圆形轮廓'
            })
        else:
            return jsonify({
                'success': False,
                'error': '不支持的文件格式'
            }), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'上传处理失败: {str(e)}'
        }), 500

@app.route('/download/<filename>')
def download_file(filename):
    """下载处理后的图片（Vercel环境不支持文件下载）"""
    return jsonify({
        'error': '在Vercel环境中不支持文件下载，请使用API接口获取base64数据'
    }), 501

@app.route('/api/health')
def health_check():
    """健康检查接口"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': '圆形图片转换服务'
    })

# Vercel兼容性
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# 为Vercel提供应用实例
application = app
