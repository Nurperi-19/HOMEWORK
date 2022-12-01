FROM python:3.10

EXPOSE 5050

RUN mkdir /bot
WORKDIR /bot

COPY . /bot

RUN pip install -r requirements.txt

CMD ["python", "/bot/bot.py"]
