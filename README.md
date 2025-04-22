# Google Play Scraper API

一个简单的API，用于从Google Play获取应用信息。

## 功能

- 获取应用标题和描述

## 环境要求

- Python 3.11+
- Flask
- python-dotenv
- requests

## 部署方式

### 本地部署

1. 克隆此仓库
2. 创建虚拟环境并激活
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # 或者
   venv\Scripts\activate     # Windows
   ```
3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
4. 复制环境变量配置
   ```bash
   cp .env.simple .env
   ```
5. 修改.env文件配置
6. 启动服务
   ```bash
   python main.py
   ```

### Docker部署

1. 使用Docker Compose进行部署
   ```bash
   docker-compose up -d
   ```

2. 查看日志
   ```bash
   docker-compose logs -f
   ```

## API使用

### 获取应用信息
```
GET /api/app_info?app_id=<app_id>
```

#### 请求参数

- `app_id`: Google Play应用ID

#### 响应
```json
{
  "success": true,
  "data": {
    "title": "应用标题",
    "description": "应用描述"
  }
}
```

## 环境变量配置

- `PORT`: API服务端口 (默认: 8081)
- `REQUEST_PROXY`: 请求代理设置 (可选)
