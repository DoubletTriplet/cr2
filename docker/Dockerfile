FROM python:3.12 as builder

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry && pip install --upgrade pip && \
    poetry config virtualenvs.create false && \
    poetry install

FROM python:3.12-slim

WORKDIR /app

RUN pip install uvicorn

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "tsc.main:app", "--host", "0.0.0.0", "--port", "8000"]
