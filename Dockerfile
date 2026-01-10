# Base image
FROM python:3.13.5-slim

# Ish papkasini yaratish
WORKDIR /app

# Dependency fayllarni nusxalash va o‘rnatish
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani konteynerga nusxalash
COPY . .

RUN python manage.py collectstatic --noinput

# Portni ochish
EXPOSE 8000

# Django serverini ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
