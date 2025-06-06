FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y curl && \
    pip install pipx && \
    pipx ensurepath && \
    pipx install uv

RUN uv pip install --system -r requirements.txt

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host=127.0.0.1", "--port=8001"]