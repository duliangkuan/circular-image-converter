@echo off
echo 正在重新部署到Vercel...
echo.

echo 1. 提交代码更改...
git add .
git commit -m "修复配置问题并添加公开访问设置"
echo.

echo 2. 推送到远程仓库...
git push origin main
echo.

echo 3. 触发Vercel重新部署...
vercel --prod
echo.

echo 部署完成！请检查Vercel控制台确认部署状态。
echo 如果仍有身份验证问题，请在Vercel项目设置中关闭"部署保护"。
pause
