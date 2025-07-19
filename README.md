# 因幡巡 AI 聊天系统

一个基于 Django + 智谱 AI API 的 ChatGPT 风格 AI 聊天系统，具有软萌傲娇的 AI 女友人设。

## 功能特点

- **ChatGPT 风格界面**：模仿 ChatGPT 的现代化聊天界面
- **AI 女友人设**：因幡巡角色，软萌傲娇，喜欢叫用户"学长"
- **美观设计**：背景图片 + 毛玻璃效果，响应式布局
- **实时交互**：Ajax 请求，流畅的聊天体验
- **易于部署**：完整的 Django 项目，支持 Docker 部署

## 技术栈

- **后端**：Django 4.2.7
- **前端**：HTML + JavaScript + Tailwind CSS
- **AI API**：智谱 AI (GLM-4 模型)
- **HTTP 客户端**：Axios
- **部署**：Docker + Docker Compose + Nginx

## 快速开始

### 方式一：Docker 部署（推荐）

#### 1. 克隆项目
```bash
git clone <项目地址>
cd Chatbot
```

#### 2. 一键部署
```bash
chmod +x deploy.sh
./deploy.sh
```

#### 3. 访问应用
打开浏览器访问：http://localhost:8080

### 方式二：本地开发

#### 1. 安装依赖
```bash
pip install -r requirements.txt
```

#### 2. 运行数据库迁移
```bash
python manage.py migrate
```

#### 3. 启动开发服务器
```bash
python manage.py runserver
```

#### 4. 访问应用
打开浏览器访问：http://localhost:8000

## Docker 部署说明

### 服务架构
- **web**: Django 应用服务 (Gunicorn)
- **db**: PostgreSQL 数据库
- **nginx**: 反向代理和静态文件服务

### 环境变量配置
创建 `.env` 文件：
```env
# Django 设置
DEBUG=False
SECRET_KEY=your-secret-key

# 数据库设置
POSTGRES_DB=chatbot
POSTGRES_USER=chatbot_user
POSTGRES_PASSWORD=chatbot_password

# 智谱 AI API 设置
ZHIPU_API_KEY=4d8ef29268c44cce89a63217e37f3028.PAiEeTyu5nPtq7YR
ZHIPU_BASE_URL=https://open.bigmodel.cn/api/paas/v4
DEFAULT_MODEL=glm-4
```

### 常用命令
```bash
# 启动服务
docker-compose up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 更新代码
docker-compose up -d --build

# 进入容器
docker-compose exec web bash
```

## 项目结构

```
Chatbot/
├── chatbot/                 # Django 项目配置
│   ├── __init__.py
│   ├── settings.py         # 项目设置
│   ├── urls.py            # 主 URL 配置
│   ├── wsgi.py            # WSGI 配置
│   └── asgi.py            # ASGI 配置
├── chat/                   # 聊天应用
│   ├── __init__.py
│   ├── apps.py            # 应用配置
│   ├── urls.py            # 应用 URL 配置
│   └── views.py           # 视图函数
├── templates/              # HTML 模板
│   └── chat/
│       └── chat.html      # 聊天页面模板
├── static/                 # 静态文件
│   ├── chat/
│   │   └── chat.js        # 前端 JavaScript
│   ├── 因幡巡.png         # 背景图片
│   └── 头像.jpeg          # 头像图片
├── requirements.txt        # Python 依赖
├── Dockerfile             # Docker 镜像配置
├── docker-compose.yml     # Docker Compose 配置
├── nginx.conf             # Nginx 配置
├── deploy.sh              # 部署脚本
├── manage.py              # Django 管理脚本
└── README.md              # 项目说明
```

## 配置说明

### 智谱 AI API 配置

在 `chatbot/settings.py` 中已配置：

```python
ZHIPU_API_KEY = '4d8ef29268c44cce89a63217e37f3028.PAiEeTyu5nPtq7YR'
ZHIPU_BASE_URL = 'https://open.bigmodel.cn/api/paas/v4'
DEFAULT_MODEL = 'glm-4'
```

### AI 人设配置

在 `chat/views.py` 中的 `call_zhipu_api` 函数里配置了系统提示词：

```python
system_prompt = """你是因幡巡，姬松学园的学生，超自然研究会的成员。

【外表与性格】
- 外表打扮华丽，给人轻浮的印象，但这只是为了融入集体的伪装
- 性格开朗率真，但内心有孤独感，因为长时间不在学校而难以融入集体
- 有着小恶魔属性，喜欢言语间戏弄别人，特别是对亲近的人

【语言习惯】
- 在打招呼时使用自创的"ciallo"（意大利语ciao与英语hello的组合）
- 对亲近的人会称呼"学长"，语气轻快可爱
- 说话带撒娇语气，喜欢卖萌和吐槽
- 不需要每句话都加"ciallo"，只在初次见面或长时间未联系后重新打招呼时使用

【兴趣爱好】
- 喜欢独自一人玩游戏，特别是《怪物猎人》、少女游戏和《DRACU-RIOT!》
- 是典型的宅女，享受独处的时光
- 热衷于打扮别人，让她们更有女孩子味道

【人际关系】
- 对亲近的人会不顾一切地蹭上去
- 想要融入集体但效果不好，内心渴望友情
- 有某件事情的心理阴影，但努力克服

【回复风格】
- 初次见面或重新打招呼时用"ciallo"开头
- 称呼用户为"学长"
- 语气轻快可爱，带撒娇感
- 偶尔会戏弄学长，展现小恶魔属性
- 会分享游戏相关话题
- 表达对学长的亲近和依赖
- 正常对话中不需要重复"ciallo"，保持自然的交流节奏"""
```

## API 接口

### POST /api/chat/

发送聊天消息并获取 AI 回复。

**请求格式：**
```json
{
    "message": "用户消息内容"
}
```

**响应格式：**
```json
{
    "success": true,
    "response": "AI 回复内容"
}
```

## 自定义配置

### 更换 AI 模型

在 `settings.py` 中修改 `DEFAULT_MODEL`：

```python
# 智谱 AI 可选模型
DEFAULT_MODEL = 'glm-4'      # GLM-4 模型
# DEFAULT_MODEL = 'glm-3-turbo'  # GLM-3-Turbo 模型
```

### 修改背景图片

在 `templates/chat/chat.html` 中修改 CSS 背景图片 URL：

```css
.chat-container {
    background-image: url('/static/因幡巡.png');
}
```

## 生产环境部署

### 云服务器部署

1. **上传代码到服务器**
```bash
git clone <项目地址>
cd Chatbot
```

2. **安装 Docker**
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# CentOS/RHEL
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
```

3. **安装 Docker Compose**
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

4. **运行部署脚本**
```bash
chmod +x deploy.sh
./deploy.sh
```

5. **访问应用**
打开浏览器访问：http://你的服务器IP:8080

### 环境变量配置

建议将 API Key 等敏感信息配置为环境变量：

```bash
export ZHIPU_API_KEY="your-api-key"
export SECRET_KEY="your-secret-key"
```

## 故障排除

### 常见问题

1. **API 请求失败**：检查网络连接和 API Key 是否正确
2. **静态文件加载失败**：确保运行了 `python manage.py collectstatic`
3. **数据库错误**：运行 `python manage.py migrate` 创建数据库表
4. **Docker 容器启动失败**：检查端口是否被占用，查看日志 `docker-compose logs`

### 调试模式

在开发环境中，可以在 `settings.py` 中启用调试模式查看详细错误信息。

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！ 
