#!/bin/bash

echo "========================================"
echo "自动配置Vercel域名脚本"
echo "========================================"

# 检查是否已安装Vercel CLI
if ! command -v vercel &> /dev/null; then
    echo "正在安装Vercel CLI..."
    npm install -g vercel
    if [ $? -ne 0 ]; then
        echo "错误：无法安装Vercel CLI，请手动安装"
        echo "运行命令：npm install -g vercel"
        exit 1
    fi
fi

echo ""
echo "请先登录Vercel账户..."
vercel login

echo ""
read -p "请输入你的域名（不含www前缀，例如：example.com）: " DOMAIN

if [ -z "$DOMAIN" ]; then
    echo "错误：域名不能为空"
    exit 1
fi

echo ""
echo "正在添加域名到Vercel项目..."
echo ""

# 添加主域名
echo "添加主域名: $DOMAIN"
vercel domains add "$DOMAIN"

# 添加www子域名
echo ""
echo "添加www子域名: www.$DOMAIN"
vercel domains add "www.$DOMAIN"

# 添加pic子域名
echo ""
echo "添加pic子域名: pic.$DOMAIN"
vercel domains add "pic.$DOMAIN"

echo ""
echo "========================================"
echo "域名添加完成！"
echo "========================================"
echo ""
echo "已添加的域名："
echo "- $DOMAIN"
echo "- www.$DOMAIN"
echo "- pic.$DOMAIN"
echo ""
echo "请等待几分钟让DNS解析生效，然后访问你的网站。"
echo ""
echo "检查域名状态："
echo "vercel domains ls"
echo ""
