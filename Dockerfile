FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8081

# 使用gunicorn作为WSGI服务器来运行Flask应用
# workers: 根据CPU核心数量设置，一般为(2*CPU核心数+1)
# bind: 绑定的地址和端口
# timeout: 请求超时时间
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:8081", "--timeout=120", "main:app_server"]
