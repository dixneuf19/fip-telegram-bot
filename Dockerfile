FROM python:3.14@sha256:be8ccd085666c34273c9dc5607c9842f8b2e3116128aae45148ce164c07ce09d

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fip_telegram_bot fip_telegram_bot

ENV PYTHONPATH=.

CMD ["python", "fip_telegram_bot/main.py"]
