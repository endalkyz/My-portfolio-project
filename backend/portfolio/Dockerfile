FROM python:3.10-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# System dependencies (needed for psycopg2)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Koyeb provides PORT dynamically
ENV PORT=8000
EXPOSE 8000

# Run application
CMD ["sh", "-c", "gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT --workers 3"]