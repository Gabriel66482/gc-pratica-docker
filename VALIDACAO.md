# Validação da entrega

Data: 10/11/2026.

## Executado nesta máquina

- Clone do template indicado no PDF, preservando seu histórico.
- Execução da revisão original da tag `v1.0.0`: subtração -6 e média 12.0, confirmadas por asserções.
- Execução do `main.py` corrigido: subtração 6 e média 8.0.
- `python -m unittest discover -s tests -v`: três testes passaram, cobrindo soma, ordem da subtração e média com listas de um, três e quatro elementos.
- Leitura dos arquivos YAML do workflow e do Compose, e conferência estática das quatro instruções do Dockerfile e das três exclusões exigidas.

As execuções locais usaram o Python 3.12.14 já incluído no ambiente do Codex, sem instalar Python
na máquina. Isso verifica a lógica do programa; não comprova a execução do container Python 3.13.

## Executado no GitHub Actions

- [Execução 42933619786 aprovada](https://github.com/Gabriel66482/gc-pratica-docker/actions/runs/42933619786), em runner Linux com Docker.
- Build e execução de `gc-pratica:1.0.0`, com subtração -6 e média 12.0 confirmadas.
- Conferência de Python 3.13 dentro da imagem.
- Build da Parte 4 e presença de `.git` antes do `.dockerignore`.
- Reconstrução de `gc-pratica:1.1.0`, com subtração 6 e média 8.0 confirmadas.
- Três testes de regressão aprovados dentro do container.
- Listagem de `/app` e asserção de ausência de `.git`, `Dockerfile` e `.dockerignore`.
- Nova execução da imagem 1.0.0, comprovando que ela continua com o defeito original.
- Execução sem `--rm` de três containers, listagem e remoção por seus nomes.
- `docker compose up -d --build`, listagem do serviço e resposta HTTP da página em `localhost:8080`.
- `docker compose down`, remoção das imagens da atividade e listagem final de containers.
- Repositório publicado em https://github.com/Gabriel66482/gc-pratica-docker.
  A publicação usa commits e tags próprios no GitHub, com as mesmas etapas e arquivos da preparação local.

## Ambiente local

Docker e WSL não estão instalados nesta máquina. A validação real dos containers foi concluída
no GitHub Actions; as imagens foram removidas do runner ao final, conforme o exercício.
O README contém o roteiro completo para repetir a prática em uma máquina com Docker.
