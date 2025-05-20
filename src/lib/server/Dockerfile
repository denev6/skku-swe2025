FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y curl && \
    pip install pipx && \
    pipx ensurepath && \
    pipx install uv

RUN uv pip install --system -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]