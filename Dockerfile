# Stage 1: Build
FROM python:3.9-slim as builder

WORKDIR /app

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Copy poetry files and install dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root

# Stage 2: Production
FROM python:3.9-slim

WORKDIR /app

# Copy only the necessary files from builder
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/.venv /app/.venv

# Copy application code
COPY app app/
COPY db db/
COPY scripts scripts/
COPY tests tests/
COPY .env.example .env

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/app"

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
