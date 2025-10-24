# 🔄 圆形图片转换器

一个简单易用的圆形图片转换网站，可以将矩形图片一键转换为圆形轮廓。

## ✨ 功能特点

- 🎯 **一键转换**：上传图片即可获得圆形轮廓
- 🌐 **Web界面**：美观易用的网页界面
- 🔗 **API接口**：支持程序化调用
- 📱 **响应式设计**：支持各种设备访问
- 🚀 **高性能**：基于Flask和PIL，处理速度快

## 🚀 快速开始

### 本地运行

1. **克隆项目**
```bash
git clone <your-repo-url>
cd circular-image-converter
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行应用**
```bash
python app.py
```

4. **访问网站**
打开浏览器访问：http://localhost:5000

### 部署到云平台

#### 部署到 Vercel（推荐）

1. **安装Vercel CLI**
```bash
npm i -g vercel
```

2. **部署**
```bash
vercel
```

3. **配置自定义域名**（可选）
```bash
# 运行域名配置脚本
setup-domain-simple.bat
```

#### 部署到 Heroku

1. **创建Heroku应用**
```bash
heroku create your-app-name
```

2. **部署代码**
```bash
git add .
git commit -m "Initial commit"
git push heroku main
```

3. **访问应用**
```bash
heroku open
```

#### 本地部署

运行本地部署脚本：
```bash
deploy-simple.bat
```

## 🔗 API接口

### 1. Base64图片转换接口

**请求地址：** `POST /api/convert`

**请求参数：**
```json
{
  "image_base64": "base64编码的图片数据",
  "size": 400  // 可选，指定输出尺寸
}
```

**响应格式：**
```json
{
  "success": true,
  "image_base64": "处理后的圆形图片base64数据",
  "message": "图片已成功转换为圆形轮廓",
  "timestamp": "2024-01-01T12:00:00"
}
```

### 2. URL图片转换接口

**请求地址：** `POST /api/convert-url`

**请求参数：**
```json
{
  "image_url": "图片URL地址",
  "size": 400,  // 可选，指定输出尺寸
  "return_type": "url"  // "url" 或 "base64"
}
```

**响应格式：**
```json
{
  "success": true,
  "image_url": "处理后的图片下载链接",
  "filename": "generated_filename.png",
  "message": "图片已成功转换为圆形轮廓",
  "timestamp": "2024-01-01T12:00:00"
}
```

### 3. 文件上传接口

**请求地址：** `POST /api/upload`

**请求格式：** `multipart/form-data`

**请求参数：**
- `file`: 图片文件

**响应格式：**
```json
{
  "success": true,
  "image_base64": "处理后的圆形图片base64数据",
  "filename": "generated_filename.png",
  "message": "图片已成功转换为圆形轮廓"
}
```

### 4. 文件下载接口

**请求地址：** `GET /download/{filename}`

**响应：** 直接返回图片文件

### 5. 健康检查接口

**请求地址：** `GET /api/health`

**响应格式：**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "service": "圆形图片转换服务",
  "version": "2.0",
  "features": ["base64_input", "url_input", "url_output", "file_upload", "file_download"]
}
```

## 🎯 在扣子工作流中使用

### 配置HTTP请求节点

1. **添加HTTP请求节点**到扣子工作流
2. **配置请求参数：**
   - **URL**: `https://your-domain.com/api/convert`
   - **方法**: `POST`
   - **请求头**: `Content-Type: application/json`
   - **请求体**:
   ```json
   {
     "image_base64": "{{图片base64数据}}",
     "size": 400
   }
   ```

3. **处理响应数据：**
   - 从响应中获取 `image_base64` 字段
   - 使用处理后的圆形图片数据

### 使用URL输入方式

如果扣子工作流中有图片URL，可以使用URL转换接口：

```json
{
  "image_url": "{{图片URL}}",
  "size": 400,
  "return_type": "base64"
}
```

### 示例工作流

```
[图片上传节点] → [HTTP请求节点] → [图片输出节点]
     ↓              ↓              ↓
  上传图片      发送到转换API    显示圆形图片
```

### 支持的输入方式

- **Base64数据**: 直接传入图片的base64编码
- **图片URL**: 传入图片的网络地址
- **文件上传**: 通过multipart/form-data上传文件

## 🛠️ 技术栈

- **后端**: Python Flask 3.0.0
- **图像处理**: PIL (Pillow) 10.1.0
- **前端**: HTML5 + CSS3 + JavaScript
- **部署**: Vercel (推荐) / Heroku / Railway
- **Python版本**: 3.11.9

## 📁 项目结构

```
circular-image-converter/
├── app.py                    # Flask应用主文件
├── api/
│   └── index.py             # Vercel入口文件
├── requirements.txt          # Python依赖
├── vercel.json              # Vercel部署配置
├── runtime.txt              # Python版本配置
├── templates/
│   └── index.html           # 前端页面
├── uploads/                 # 上传文件目录
├── outputs/                 # 输出文件目录
├── deploy-simple.bat        # 本地部署脚本
├── setup-domain-simple.bat  # 域名配置脚本
├── redeploy-simple.bat      # 重新部署脚本
└── README.md                # 项目说明
```

## 🔧 配置说明

### 环境变量

- `FLASK_ENV`: 运行环境 (development/production)
- `VERCEL`: Vercel部署标识
- `BASE_URL`: 服务基础URL（可选，会自动检测）

### 支持的文件格式

- PNG
- JPG/JPEG
- GIF
- BMP
- WebP

## 🚨 注意事项

1. **文件大小限制**: 建议上传文件不超过10MB
2. **并发处理**: 支持多用户同时使用
3. **安全性**: 建议在生产环境中添加适当的访问控制
4. **性能优化**: 大量使用时建议添加缓存机制
5. **域名配置**: 使用自定义域名时请确保DNS解析正确
6. **Vercel限制**: 注意Vercel的免费额度限制

## 📞 技术支持

如有问题，请提交Issue或联系开发者。

## 📄 许可证

MIT License
