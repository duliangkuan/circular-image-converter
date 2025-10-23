#!/bin/bash

echo "========================================"
echo "Vercel域名自动化配置脚本"
echo "========================================"
echo

read -p "请输入您的完整子域名 (例如: api.yourdomain.com): " DOMAIN
echo

echo "正在添加域名到Vercel项目..."
vercel domains add $DOMAIN

echo
echo "获取DNS配置信息..."
vercel domains inspect $DOMAIN

echo
echo "========================================"
echo "配置完成！请在阿里云DNS中配置以下信息："
echo "========================================"
echo
echo "记录类型: CNAME"
echo "主机记录: api (或您想要的子域名前缀)"
echo "记录值: cname.vercel-dns.com"
echo "TTL: 600"
echo
echo "配置完成后，请运行验证命令："
echo "vercel domains verify $DOMAIN"
echo


