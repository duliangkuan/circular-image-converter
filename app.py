# 圆形图片转换网站
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import base64
import io
from PIL import Image, ImageDraw
import os
import uuid
from datetime import datetime
import requests
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 配置
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
BASE_URL = os.environ.get('BASE_URL', 'https://zhuanhua-9asiwamte-duliangkuans-projects.vercel.app')

# 创建必要的文件夹
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    """检查文件扩展名是否允许"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def download_image_from_url(image_url):
    """从URL下载图片"""
    try:
        # 验证URL格式
        parsed_url = urlparse(image_url)
        if not parsed_url.scheme or not parsed_url.netloc:
            raise Exception("无效的图片URL")
        
        # 设置请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 下载图片
        response = requests.get(image_url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 检查内容类型
        content_type = response.headers.get('content-type', '').lower()
        if not any(img_type in content_type for img_type in ['image/', 'application/octet-stream']):
            raise Exception("URL指向的不是图片文件")
        
        return response.content
    except requests.exceptions.RequestException as e:
        raise Exception(f"下载图片失败: {str(e)}")
    except Exception as e:
        raise Exception(f"处理图片URL失败: {str(e)}")

def save_image_to_file(image, filename):
    """保存图片到文件并返回URL"""
    try:
        # 保存到outputs目录
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        file_path = os.path.join(OUTPUT_FOLDER, filename)
        image.save(file_path, format='PNG')
        # 使用环境变量或默认URL
        base_url = os.environ.get('BASE_URL', 'https://zhuanhua-9asiwamte-duliangkuans-projects.vercel.app')
        return f"{base_url}/download/{filename}"
    except Exception as e:
        raise Exception(f"保存图片失败: {str(e)}")

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
    return jsonify({
        'service': '圆形图片转换服务',
        'version': '2.0',
        'endpoints': {
            'convert': '/api/convert',
            'convert_url': '/api/convert-url',
            'upload': '/api/upload',
            'health': '/api/health'
        },
        'description': '支持多种输入方式的圆形图片转换服务',
        'features': ['base64_input', 'url_input', 'file_upload', 'url_output']
    })

@app.route('/api/convert', methods=['POST'])
def convert_image():
    """API接口：转换图片为圆形（支持base64输入）"""
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

@app.route('/api/convert-url', methods=['POST'])
def convert_image_from_url():
    """API接口：从URL转换图片为圆形（支持URL输入和URL输出）"""
    try:
        # 获取请求数据
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': '请求数据为空'
            }), 400
        
        # 获取参数
        image_url = data.get('image_url', '')
        size = data.get('size', None)  # 可选：指定输出尺寸
        return_type = data.get('return_type', 'url')  # 'url' 或 'base64'
        
        if not image_url:
            return jsonify({
                'success': False,
                'error': '缺少图片URL'
            }), 400
        
        # 从URL下载图片
        try:
            image_data = download_image_from_url(image_url)
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 400
        
        # 转换为圆形图片
        try:
            circular_image = create_circular_image(image_data, size)
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
        
        # 生成唯一文件名
        filename = f"circular_{uuid.uuid4().hex}.png"
        
        # 根据返回类型处理结果
        if return_type == 'url':
            # 保存文件并返回URL
            try:
                image_url_result = save_image_to_file(circular_image, filename)
                
                return jsonify({
                    'success': True,
                    'image_url': image_url_result,
                    'filename': filename,
                    'message': '图片已成功转换为圆形轮廓',
                    'timestamp': datetime.now().isoformat()
                })
            except Exception as e:
                return jsonify({
                    'success': False,
                    'error': f'保存图片失败: {str(e)}'
                }), 500
        else:
            # 返回base64格式
            output_buffer = io.BytesIO()
            circular_image.save(output_buffer, format='PNG')
            output_base64 = base64.b64encode(output_buffer.getvalue()).decode('utf-8')
            
            return jsonify({
                'success': True,
                'image_base64': output_base64,
                'filename': filename,
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
            
            # 转换为base64返回
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
    """下载处理后的图片"""
    try:
        # 检查文件是否存在
        file_path = os.path.join(OUTPUT_FOLDER, filename)
        if not os.path.exists(file_path):
            return jsonify({
                'error': '文件不存在'
            }), 404
        
        # 返回文件
        return send_file(file_path, as_attachment=True, download_name=filename)
    except Exception as e:
        return jsonify({
            'error': f'下载文件失败: {str(e)}'
        }), 500

@app.route('/api/health')
def health_check():
    """健康检查接口"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': '圆形图片转换服务',
        'version': '2.0',
        'features': ['base64_input', 'url_input', 'url_output', 'file_upload', 'file_download']
    })

# 添加错误处理
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': '内部服务器错误',
        'message': str(error)
    }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': '页面未找到',
        'message': str(error)
    }), 404

# Vercel需要这个变量来识别Flask应用
app = app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
