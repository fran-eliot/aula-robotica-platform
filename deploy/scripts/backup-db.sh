#!/usr/bin/env bash
set -e

BACKUP_DIR="./backups"
mkdir -p "$BACKUP_DIR"

docker compose exec db mariadb-dump \
  -u root \
  -p"$MYSQL_ROOT_PASSWORD" \
  "$MYSQL_DATABASE" > "$BACKUP_DIR/aula_robotica_$(date +%Y%m%d_%H%M%S).sql"