FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    \
    # Poetry
    POETRY_VERSION=1.8.3 \
    POETRY_HOME=/opt/poetry \
    POETRY_VIRTUALENVS_CREATE=false

# Install core libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean && apt-get install -y --no-install-recommends \
    build-essential\
    ca-certificates \
    curl \
    gnupg2 \
    libpq-dev \
    postgresql-client \
    poppler-utils \
    unzip \
    && curl -sSL https://install.python-poetry.org | python

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

# https://code.visualstudio.com/docs/remote/containers-advanced#_persist-bash-history-between-runs
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && echo $SNIPPET >> "/root/.bashrc"

# Add Poetry to path
ENV PATH "/opt/poetry/bin:${PATH}"

# Project Files and Settings
ARG PROJECT_DIR=/var/www/

RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

# Server
EXPOSE 8000
STOPSIGNAL SIGINT
