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

#### 部署到 Railway

1. 连接GitHub仓库到Railway
2. 自动部署，无需额外配置

#### 部署到 Vercel

1. 安装Vercel CLI
```bash
npm i -g vercel
```

2. 部署
```bash
vercel
```

## 🔗 API接口

### 转换图片接口

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

### 文件上传接口

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
  "download_url": "/download/generated_filename.png",
  "message": "图片已成功转换为圆形轮廓"
}
```

### 健康检查接口

**请求地址：** `GET /api/health`

**响应格式：**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00",
  "service": "圆形图片转换服务"
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
     "image_base64": "{{图片base64数据}}"
   }
   ```

3. **处理响应数据：**
   - 从响应中获取 `image_base64` 字段
   - 使用处理后的圆形图片数据

### 示例工作流

```
[图片上传节点] → [HTTP请求节点] → [图片输出节点]
     ↓              ↓              ↓
  上传图片      发送到转换API    显示圆形图片
```

## 🛠️ 技术栈

- **后端**: Python Flask
- **图像处理**: PIL (Pillow)
- **前端**: HTML5 + CSS3 + JavaScript
- **部署**: Heroku/Railway/Vercel

## 📁 项目结构

```
circular-image-converter/
├── app.py                 # Flask应用主文件
├── requirements.txt       # Python依赖
├── Procfile              # Heroku部署配置
├── runtime.txt           # Python版本配置
├── templates/
│   └── index.html        # 前端页面
├── uploads/              # 上传文件目录
├── outputs/              # 输出文件目录
└── README.md             # 项目说明
```

## 🔧 配置说明

### 环境变量

- `FLASK_ENV`: 运行环境 (development/production)
- `PORT`: 服务端口 (默认5000)

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

## 📞 技术支持

如有问题，请提交Issue或联系开发者。

## 📄 许可证

MIT License
