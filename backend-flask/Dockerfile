FROM python:3.12.0a5-slim as builder

WORKDIR /backend-flask

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /backend-flask/wheels -r requirements.txt

FROM python:3.12.0a5-slim

WORKDIR /backend-flask

COPY --from=builder /backend-flask/wheels /wheels
COPY --from=builder /backend-flask/requirements.txt .

RUN apt-get update && apt-get install -y \
  curl \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache /wheels/*

COPY app.py .
COPY services .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]