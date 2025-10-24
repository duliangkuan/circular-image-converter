# 阿里云DNS子域名配置指南

## 🎯 配置新子域名：api.songgeixiaopengyoudeliwu.icu

### 在阿里云控制台配置DNS记录

1. **登录阿里云控制台**
   - 访问：https://dns.console.aliyun.com
   - 登录你的阿里云账户

2. **进入域名解析页面**
   - 找到域名：`songgeixiaopengyoudeliwu.icu`
   - 点击"解析设置"

3. **添加新的DNS记录**
   
   **点击"添加记录"按钮，然后填写：**
   
   ```
   记录类型：CNAME
   主机记录：api
   解析请求来源：默认
   记录值：cname.vercel-dns.com
   负载策略：轮询
   权重：-
   TTL：10分钟
   ```

4. **保存记录**
   - 点击"确认"保存

### 验证DNS配置

配置完成后，你可以通过以下方式验证：

1. **使用nslookup命令**（在命令行中）：
   ```bash
   nslookup api.songgeixiaopengyoudeliwu.icu
   ```

2. **在线DNS查询工具**：
   - 访问：https://tool.chinaz.com/dns/
   - 输入：`api.songgeixiaopengyoudeliwu.icu`
   - 查看解析结果

3. **等待生效**：
   - DNS解析通常需要5-30分钟生效
   - TTL设置为10分钟，所以最多等待10分钟

## 📋 配置完成后

当DNS记录配置完成并生效后，我们就可以通过Vercel CLI添加这个新域名了！

## 🔄 下一步操作

DNS配置完成后，运行以下命令添加域名：

```bash
vercel domains add api.songgeixiaopengyoudeliwu.icu
```

## 💡 其他可选的子域名

你也可以选择其他子域名，比如：
- `app.songgeixiaopengyoudeliwu.icu`
- `web.songgeixiaopengyoudeliwu.icu`
- `tools.songgeixiaopengyoudeliwu.icu`
- `convert.songgeixiaopengyoudeliwu.icu`

只需要将主机记录改为你想要的名称即可。



