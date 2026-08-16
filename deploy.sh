#!/usr/bin/env bash
# Deploy de produção do site estático (docs/) no Server 2 via Portainer API.
#
#   ./deploy.sh              # build+push (arm64) + criar/atualizar stack
#   SKIP_BUILD=1 ./deploy.sh # só (re)deploy do stack
#
# Segredos vêm de ~/projetos/infra/.env (chaves *_SERVER2). Nada de credencial aqui.
# Pré-requisitos: docker buildx, jq, DNS de tapilang.com apontando p/ o servidor.
set -euo pipefail
cd "$(dirname "$0")"

ENV_FILE="${ENV_FILE:-$HOME/projetos/infra/.env}"
[ -f "$ENV_FILE" ] || { echo "ERRO: $ENV_FILE ausente"; exit 1; }
set -a; . "$ENV_FILE"; set +a

command -v jq >/dev/null || { echo "ERRO: jq necessário"; exit 1; }

PURL="${PORTAINER_URL_SERVER2:?}"; PURL="${PURL%/}"
ENDPOINT="${ENDPOINT_ID_SERVER2:-3}"
REG_HOST="$(printf '%s' "${REGISTRY_URL_SERVER2:?}" | sed -E 's#^https?://##')"
PLATFORM="${PLATFORM:-linux/arm64}"   # servidor é aarch64
STACK_NAME="tapilang"
IMAGE="$REG_HOST/tapilang:latest"

if [ "${SKIP_BUILD:-0}" != "1" ]; then
  echo "== docker login $REG_HOST =="
  printf '%s' "${REGISTRY_PASS_SERVER2:?}" \
    | docker login -u "${REGISTRY_USER_SERVER2:?}" --password-stdin "$REG_HOST"

  echo "== build+push $IMAGE ($PLATFORM) =="
  docker buildx build --platform "$PLATFORM" -t "$IMAGE" --push .
fi

echo "== deploy stack '$STACK_NAME' via Portainer =="
CONTENT="$(cat infra/stack.prod.yml)"

api() { curl -fsS -H "X-API-Key: ${PORTAINER_API_KEY_SERVER2:?}" "$@"; }

STACK_ID="$(api "$PURL/api/stacks" | jq -r --arg n "$STACK_NAME" '.[]|select(.Name==$n)|.Id' | head -1)"

if [ -n "$STACK_ID" ] && [ "$STACK_ID" != "null" ]; then
  echo "atualizando stack id=$STACK_ID (prune+pull)"
  jq -n --arg c "$CONTENT" '{stackFileContent:$c, env:[], prune:true, pullImage:true}' \
    | api -X PUT -H "Content-Type: application/json" \
        "$PURL/api/stacks/$STACK_ID?endpointId=$ENDPOINT" -d @- >/dev/null
else
  echo "criando stack novo"
  jq -n --arg n "$STACK_NAME" --arg c "$CONTENT" '{name:$n, stackFileContent:$c, env:[]}' \
    | api -X POST -H "Content-Type: application/json" \
        "$PURL/api/stacks/create/standalone/string?endpointId=$ENDPOINT" -d @- >/dev/null
fi

echo "== OK =="
echo "  https://www.tapilang.com"
echo "  https://tapilang.com -> 301 para www"
echo "Obs.: 1º acesso pode levar ~1min p/ o Let's Encrypt emitir o cert."
