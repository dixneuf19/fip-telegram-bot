FROM python:3.14@sha256:e06cc1111ed84189e91866447f562b89faadbfbbb9937cd67e6bf4172cdb45df

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fip_telegram_bot fip_telegram_bot

ENV PYTHONPATH=.

CMD ["python", "fip_telegram_bot/main.py"]
