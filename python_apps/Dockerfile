FROM python:3.11-slim

# Use a non-root user for better security
RUN useradd --create-home appuser

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install dependencies first to leverage Docker layer caching
COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application files after dependencies are installed
COPY . .

RUN chown -R appuser:appuser /app
USER appuser

ENV MYSQL_USER=root  

ENV MYSQL_PASSWORD=your_password

ENV MYSQL_HOST=172.17.0.2

ENV MYSQL_DATABASE=crud_db

EXPOSE 5000

CMD ["python", "app.py"]