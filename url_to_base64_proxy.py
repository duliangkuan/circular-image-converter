# URL转base64代理服务 - 为国内API添加URL输入支持
import requests
import base64
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def download_image_from_url(image_url):
    """从URL下载图片并转换为base64"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(image_url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # 转换为base64
        image_base64 = base64.b64encode(response.content).decode('utf-8')
        return f"data:image/jpeg;base64,{image_base64}"
    except Exception as e:
        raise Exception(f"下载图片失败: {str(e)}")

@app.route('/api/convert-url', methods=['POST'])
def convert_url_to_circular():
    """URL输入转圆形图片的代理接口"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': '请求数据为空'
            }), 400
        
        image_url = data.get('image_url', '')
        size = data.get('size', 400)
        
        if not image_url:
            return jsonify({
                'success': False,
                'error': '缺少图片URL'
            }), 400
        
        # 下载图片并转换为base64
        try:
            image_base64 = download_image_from_url(image_url)
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 400
        
        # 调用国内API进行转换
        try:
            api_url = "https://api.songgeixiaopengyoudeliwu.icu/api/convert"
            payload = {
                "image_base64": image_base64,
                "size": size
            }
            
            response = requests.post(api_url, json=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get('success'):
                return jsonify({
                    'success': True,
                    'image_base64': result.get('image_base64'),
                    'message': '图片已成功转换为圆形轮廓（通过URL输入）',
                    'original_url': image_url,
                    'size': size
                })
            else:
                return jsonify({
                    'success': False,
                    'error': result.get('error', '转换失败')
                }), 500
                
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'调用转换API失败: {str(e)}'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'服务器内部错误: {str(e)}'
        }), 500

@app.route('/api/health')
def health_check():
    """健康检查"""
    return jsonify({
        'status': 'healthy',
        'service': 'URL转base64代理服务',
        'target_api': 'https://api.songgeixiaopengyoudeliwu.icu/api/convert'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
