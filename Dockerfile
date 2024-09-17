# ------------------------------------------------------------
# Backend builder
# ------------------------------------------------------------
FROM python:3.12-slim-bookworm AS be-builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    \
    # Poetry
    POETRY_VERSION=1.8.3 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false

# Create Poetry directories
RUN mkdir -p /etc/poetry && \
    chgrp -R 0 /etc/poetry && \
    chmod -R g+rw /etc/poetry

# Install core libraries and Poetry
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean && apt-get install -y --no-install-recommends \
    build-essential\
    ca-certificates \
    curl \
    gnupg2 \
    libpq-dev \
    postgresql-client \
    poppler-utils \
    && curl -sSL https://install.python-poetry.org | python

# Add Poetry to path
ENV PATH="${PATH}:${POETRY_HOME}/bin"

# Copy Poetry files
COPY backend/poetry.lock backend/pyproject.toml ./

# Build dependencies
RUN poetry export -f requirements.txt --output requirements.txt && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


# ------------------------------------------------------------
# Frontend builder
# ------------------------------------------------------------
FROM --platform=linux/amd64 node:18-slim AS fe-builder

# Set working directory
WORKDIR /app

# Install dependencies
COPY frontend/package*.json ./
RUN npm install

# Copy the rest of the application code
COPY frontend/ ./

# Build the application
RUN npm run build


# ------------------------------------------------------------
# Backend image
# ------------------------------------------------------------
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /var/www

# Install core libraries
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg2 \
        gunicorn \
        nginx \
        supervisor \
        postgresql-client \
        vim \
    && rm -rf /var/lib/apt/lists/*

# Fix permissions
RUN chgrp -R 0 /var/log/nginx /var/lib/nginx /var/log/gunicorn /var/log/supervisor && \
    chmod -R g+rw /var/log/nginx /var/lib/nginx /var/log/gunicorn && \
    chmod 775 /var/log/supervisor && \
    chmod g+rwx /var/run && \
    chmod -R g=u /etc/passwd && \
    mkdir -p /var/www/html/static && \
    chgrp -R 0 /var/www/html && \
    chmod -R g=u /var/www

# Install backend dependencies
COPY --from=be-builder /wheels /wheels
RUN pip install --no-cache /wheels/*

# Copy project files
COPY backend/ .

# Copy config and scripts
RUN mv .build/nginx/nginx.conf /etc/nginx/ && \
    mv .build/supervisor/supervisor.conf /etc/supervisor/conf.d/ && \
    chmod ug+x ./.build/script/*.sh && \
    mv ./.build/script/* /bin/ && \
    rm -rf .build && \
    rm poetry.lock pyproject.toml

# Copy frontend files
COPY --from=fe-builder /app/dist /var/www/html

# Server
EXPOSE 8080
CMD ["/bin/start_application.sh"]
