FROM python:3.10@sha256:c10791e6f69086d5216f7b5d3b839929c454e24305867ed9bc5152f0355b5423

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY fip_telegram_bot fip_telegram_bot

ENV PYTHONPATH=.

CMD ["python", "fip_telegram_bot/main.py"]
