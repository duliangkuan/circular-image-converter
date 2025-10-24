@echo off
chcp 65001 >nul

echo ========================================
echo 重新部署到Vercel
echo ========================================
echo.

echo 📝 提交代码更改...
git add .
git commit -m "优化代码并清理无用文件"

echo.
echo 🚀 推送到远程仓库...
git push origin main

echo.
echo 🔄 触发Vercel重新部署...
vercel --prod

echo.
echo ✅ 部署完成！请检查Vercel控制台确认部署状态。
echo.

pause
