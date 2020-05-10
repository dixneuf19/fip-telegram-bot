FROM python:3.8.2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src

ENV PYTHONPATH=.

CMD ["python", "src/main.py"]