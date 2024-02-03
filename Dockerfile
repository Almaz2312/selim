FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

COPY . .

EXPOSE 8000

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
