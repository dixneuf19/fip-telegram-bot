FROM python:3.14@sha256:12d187a59ecdeb95df0a78cd6107a84398455365a66cc2183db2be42b6067d33

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fip_telegram_bot fip_telegram_bot

ENV PYTHONPATH=.

CMD ["python", "fip_telegram_bot/main.py"]
