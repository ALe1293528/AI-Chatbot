# 项目结构说明

## 目录结构

```
Chatbot/
├── chatbot/                 # Django 项目主配置
│   ├── __init__.py         # Python 包标识
│   ├── settings.py         # Django 项目设置
│   ├── urls.py            # 主 URL 路由配置
│   ├── wsgi.py            # WSGI 应用入口
│   └── asgi.py            # ASGI 应用入口
├── chat/                   # 聊天应用
│   ├── __init__.py         # Python 包标识
│   ├── apps.py            # Django 应用配置
│   ├── urls.py            # 应用 URL 路由
│   └── views.py           # 视图函数和 API 处理
├── templates/              # HTML 模板目录
│   └── chat/
│       └── chat.html      # 聊天页面模板
├── static/                 # 静态文件目录
│   └── chat/
│       └── chat.js        # 前端 JavaScript 逻辑
├── requirements.txt        # Python 依赖包列表
├── manage.py              # Django 管理脚本
├── run.py                 # 项目启动脚本
├── test_setup.py          # 项目设置测试脚本
├── README.md              # 项目说明文档
├── PROJECT_STRUCTURE.md   # 项目结构说明（本文件）
└── .gitignore             # Git 忽略文件配置
```

## 核心文件说明

### 后端文件

#### `chatbot/settings.py`
- Django 项目的主要配置文件
- 包含数据库、中间件、模板、静态文件等配置
- 配置了智谱 AI API 相关设置：
  - `ZHIPU_API_KEY`: API 密钥
  - `ZHIPU_BASE_URL`: API 基础 URL
  - `DEFAULT_MODEL`: 默认使用的 AI 模型

#### `chatbot/urls.py`
- 项目主 URL 路由配置
- 将根路径重定向到 chat 应用

#### `chat/views.py`
- 核心业务逻辑文件
- `chat_view()`: 渲染聊天页面
- `chat_api()`: 处理聊天 API 请求
- `call_zhipu_api()`: 调用智谱 AI API 获取 AI 回复

#### `chat/urls.py`
- chat 应用的 URL 路由配置
- 定义了两个路由：
  - `/`: 聊天页面
  - `/api/chat/`: 聊天 API 接口

### 前端文件

#### `templates/chat/chat.html`
- 聊天页面的 HTML 模板
- 使用 Tailwind CSS 构建现代化界面
- 包含：
  - 响应式聊天界面
  - 毛玻璃背景效果
  - 打字指示器动画
  - 消息气泡样式

#### `static/chat/chat.js`
- 前端 JavaScript 逻辑
- 实现了 `ChatApp` 类来管理聊天功能
- 功能包括：
  - 消息发送和接收
  - 实时 UI 更新
  - 错误处理
  - 自动滚动
  - 输入框自适应高度

### 工具脚本

#### `run.py`
- 一键启动脚本
- 自动安装依赖、运行数据库迁移、启动服务器
- 提供友好的命令行界面

#### `test_setup.py`
- 项目设置测试脚本
- 验证 Django 配置、模块导入、URL 路由等
- 帮助诊断项目设置问题

## 技术架构

### 后端架构
```
用户请求 → Django URL 路由 → Views 处理 → 智谱 AI API → 返回响应
```

### 前端架构
```
用户输入 → JavaScript 处理 → Ajax 请求 → 后端 API → 更新 UI
```

### 数据流
1. 用户在输入框输入消息
2. JavaScript 捕获输入并发送 Ajax POST 请求
3. Django 后端接收请求并调用智谱 AI API
4. AI 模型生成回复
5. 后端返回 JSON 响应
6. 前端接收响应并更新聊天界面

## 配置说明

### 环境要求
- Python 3.8+
- Django 4.2.7
- requests 2.31.0

### API 配置
- 使用智谱 AI 提供的 API
- 支持 GLM-4、GLM-3-Turbo 等模型
- API Key 已预配置在 settings.py 中

### 部署配置
- 开发环境：`DEBUG = True`
- 生产环境：需要修改 `DEBUG = False` 并配置生产数据库
- 静态文件：使用 `python manage.py collectstatic` 收集

## 扩展说明

### 添加新功能
1. 在 `chat/views.py` 中添加新的视图函数
2. 在 `chat/urls.py` 中添加对应的 URL 路由
3. 在前端 JavaScript 中添加相应的交互逻辑

### 更换 AI 模型
1. 修改 `settings.py` 中的 `DEFAULT_MODEL`
2. 可选模型包括：
   - `glm-4`
   - `glm-3-turbo`
   - 其他智谱 AI 支持的模型

### 自定义样式
1. 修改 `templates/chat/chat.html` 中的 CSS
2. 调整 Tailwind CSS 类名
3. 更换背景图片 URL

## 安全考虑

### 当前配置
- CSRF 保护已启用
- API Key 存储在设置文件中（开发环境）

### 生产环境建议
- 将 API Key 移到环境变量
- 启用 HTTPS
- 配置适当的 CORS 策略
- 添加请求频率限制
- 实现用户认证（如需要） 