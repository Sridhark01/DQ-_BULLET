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
