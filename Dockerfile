FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       default-libmysqlclient-dev \
       build-essential \
       pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Tạo tài khoản riêng để chạy ứng dụng, không sử dụng root
RUN groupadd --system django \
    && useradd --system --gid django --create-home django

COPY --chown=django:django . .

# Chuyển sang tài khoản không có quyền root
USER django

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]