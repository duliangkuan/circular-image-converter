#!/bin/bash

echo "========================================"
echo "将域名添加到已部署的Vercel项目"
echo "========================================"
echo ""

# 检查Vercel CLI是否已安装
if ! command -v vercel &> /dev/null; then
    echo "❌ 未检测到Vercel CLI，正在安装..."
    npm install -g vercel
    if [ $? -ne 0 ]; then
        echo "❌ 安装失败，请手动安装：npm install -g vercel"
        exit 1
    fi
    echo "✅ Vercel CLI安装成功！"
else
    echo "✅ Vercel CLI已安装"
fi

echo ""
echo "🔐 请先登录Vercel账户..."
vercel login

echo ""
echo "📋 请输入你的域名信息："
echo ""
read -p "请输入主域名（例如：example.com）: " DOMAIN

if [ -z "$DOMAIN" ]; then
    echo "❌ 域名不能为空"
    exit 1
fi

echo ""
echo "🚀 正在将域名添加到Vercel项目..."
echo ""

# 添加主域名
echo "📍 添加主域名: $DOMAIN"
vercel domains add "$DOMAIN"
if [ $? -eq 0 ]; then
    echo "✅ 主域名添加成功"
else
    echo "⚠️ 主域名添加可能失败，请检查"
fi

echo ""

# 添加www子域名
echo "📍 添加www子域名: www.$DOMAIN"
vercel domains add "www.$DOMAIN"
if [ $? -eq 0 ]; then
    echo "✅ www子域名添加成功"
else
    echo "⚠️ www子域名添加可能失败，请检查"
fi

echo ""

# 添加pic子域名
echo "📍 添加pic子域名: pic.$DOMAIN"
vercel domains add "pic.$DOMAIN"
if [ $? -eq 0 ]; then
    echo "✅ pic子域名添加成功"
else
    echo "⚠️ pic子域名添加可能失败，请检查"
fi

echo ""
echo "========================================"
echo "📊 检查域名状态..."
echo "========================================"
vercel domains ls

echo ""
echo "========================================"
echo "🎉 域名添加完成！"
echo "========================================"
echo ""
echo "📝 已添加的域名："
echo "  • $DOMAIN"
echo "  • www.$DOMAIN"
echo "  • pic.$DOMAIN"
echo ""
echo "⏰ 请等待5-30分钟让DNS解析生效"
echo "🔗 然后访问你的网站测试："
echo "  • https://$DOMAIN"
echo "  • https://www.$DOMAIN"
echo "  • https://pic.$DOMAIN"
echo ""
echo "💡 如需检查域名状态，运行：vercel domains ls"
echo ""

