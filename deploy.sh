#!/bin/bash

# 因幡巡 AI 聊天系统部署脚本

set -e

echo "🎀 因幡巡 AI 聊天系统 - Docker 部署脚本"
echo "=================================================="

# 检查 Docker 是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose 未安装，请先安装 Docker Compose"
    exit 1
fi

echo "✅ Docker 环境检查通过"

# 创建环境变量文件
if [ ! -f .env ]; then
    echo "📝 创建环境变量文件..."
    cat > .env << EOF
# Django 设置
DEBUG=False
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(50))')

# 数据库设置
POSTGRES_DB=chatbot
POSTGRES_USER=chatbot_user
POSTGRES_PASSWORD=chatbot_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# 智谱 AI API 设置
ZHIPU_API_KEY=4d8ef29268c44cce89a63217e37f3028.PAiEeTyu5nPtq7YR
ZHIPU_BASE_URL=https://open.bigmodel.cn/api/paas/v4
DEFAULT_MODEL=glm-4
EOF
    echo "✅ 环境变量文件创建完成"
else
    echo "ℹ️  环境变量文件已存在"
fi

# 停止现有容器
echo "🛑 停止现有容器..."
docker-compose down

# 构建镜像
echo "🔨 构建 Docker 镜像..."
docker-compose build --no-cache

# 启动服务
echo "🚀 启动服务..."
docker-compose up -d

# 等待服务启动
echo "⏳ 等待服务启动..."
sleep 10

# 检查服务状态
echo "🔍 检查服务状态..."
docker-compose ps

# 运行数据库迁移
echo "🗄️  运行数据库迁移..."
docker-compose exec web python manage.py migrate

# 收集静态文件
echo "📦 收集静态文件..."
docker-compose exec web python manage.py collectstatic --noinput

echo ""
echo "🎉 部署完成！"
echo "=================================================="
echo "📱 访问地址: http://localhost:8080"
echo "🔧 管理命令:"
echo "   - 查看日志: docker-compose logs -f"
echo "   - 停止服务: docker-compose down"
echo "   - 重启服务: docker-compose restart"
echo "   - 更新代码: docker-compose up -d --build"
echo "==================================================" 