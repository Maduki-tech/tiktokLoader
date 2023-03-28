FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt update && apt upgrade -y
RUN pip install --no-cache-dir -r requirements.txt
RUN apt install ffmpeg -y

COPY . .

CMD [ "gunicorn", "main:app" ]
