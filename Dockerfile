FROM python:3.12

ENV TZ=Asia/Bangkok

# 不生成 pyc 文件
ENV PYTHONDONTWRITEBYTECODE=1

# 实时输出日志
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]