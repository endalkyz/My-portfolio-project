
FROM python:3.10

# Set working directory
WORKDIR /app

# Prevent .pyc files + ensure stdout/stderr works
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
# RUN python manage.py collectstatic --noinput

# Use dynamic port provided by Railway
ENV PORT 8000
EXPOSE $PORT

# Run Gunicorn using dynamic port
CMD ["sh", "-c", "gunicorn portfolio.wsgi:application --bind 0.0.0.0:$PORT --workers 3"]


