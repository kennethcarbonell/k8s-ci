FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffering logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install basic runtime deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Install FastAPI + Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn

# Copy the app
COPY app.py/ ./

# Expose FastAPI default port
EXPOSE 8000

# Run it
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
