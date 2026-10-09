#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

docker compose config
docker compose up -d --build
docker compose ps