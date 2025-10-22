'''
#FROM python:3.10-slim-buster
FROM python:3.10-slim
RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /DQ-_BULLET
WORKDIR /DQ-_BULLET
COPY . .

CMD ["python3", "bot.py"]
'''
# 🧩 Base image: use Python 3.10.14 (stable & compatible with Motor, Pyrogram, etc.)
FROM python:3.10.14-slim

# 🕐 Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 📦 Install required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 🏗️ Create app directory
WORKDIR /app

# 🧾 Copy all files
COPY . /app

# 🔧 Upgrade pip and install all Python dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install -U -r requirements.txt && \
    pip install --upgrade motor pymongo

# 🪄 Make start script executable
RUN chmod +x start.sh

# 🔑 Default environment variable placeholders (values will be set in Choreo Console)
ENV BOT_TOKEN=""
ENV API_ID=""
ENV API_HASH=""
ENV DATABASE_URI=""
ENV DATABASE_NAME="Telegram"
ENV COLLECTION_NAME="channel_files"
ENV ADMINS=""

# 🚀 Start the bot
CMD ["bash", "start.sh"]
