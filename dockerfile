# 使用官方 Python 运行时作为父图像
FROM python:3.8-slim

# 设置工作目录为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 中的容器中
COPY . /app

# 安装 flask
RUN pip install Flask

# 使端口 8000 可供此容器外的环境使用
EXPOSE 8000

# 定义环境变量
ENV FLASK_APP=web.py

# 在容器启动时运行 web.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
