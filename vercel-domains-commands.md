# Vercel CLI 域名配置命令

## 🚀 快速配置步骤

### 1. 安装Vercel CLI（如果未安装）
```bash
npm install -g vercel
```

### 2. 登录Vercel账户
```bash
vercel login
```

### 3. 添加域名到项目

假设你的域名是 `example.com`，运行以下命令：

```bash
# 添加主域名
vercel domains add example.com

# 添加www子域名
vercel domains add www.example.com

# 添加pic子域名
vercel domains add pic.example.com
```

### 4. 检查域名状态
```bash
vercel domains ls
```

### 5. 查看项目信息
```bash
vercel ls
```

## 📋 常用命令

### 查看所有域名
```bash
vercel domains ls
```

### 查看特定域名详情
```bash
vercel domains inspect example.com
```

### 删除域名
```bash
vercel domains rm example.com
```

### 查看项目部署状态
```bash
vercel ls
```

### 重新部署项目
```bash
vercel --prod
```

## ⚠️ 注意事项

1. **确保已登录**：运行域名命令前必须先登录Vercel
2. **域名格式**：不要包含协议（http://或https://）
3. **DNS生效时间**：添加域名后需要等待DNS解析生效（5-30分钟）
4. **SSL证书**：Vercel会自动为域名配置SSL证书

## 🔍 故障排除

### 如果域名添加失败：
1. 检查域名是否已在其他Vercel项目中
2. 确认DNS解析配置正确
3. 等待DNS传播完成

### 如果域名验证失败：
1. 检查DNS记录是否正确指向Vercel
2. 确认TTL值设置合理
3. 使用 `nslookup` 验证DNS解析

## 📞 获取帮助
```bash
vercel domains --help
vercel --help
```
