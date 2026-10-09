# Deployment

## Local

```bash
cd deploy

cp .env.example .env

docker compose up -d --build
```

## Production

```bash
docker compose up -d --build
```

Application:

http://SERVER_IP