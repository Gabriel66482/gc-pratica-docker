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

## Pendente por limitação do ambiente

- Docker e WSL não estão instalados: builds, execução dos containers, versão de Python dentro
  da imagem, listagem real de `/app`, Compose e limpeza de imagens não foram executados.
- O workflow está configurado, mas ainda não rodou no GitHub.
- Repositório publicado em https://github.com/Gabriel66482/gc-pratica-docker.
  A publicação usa commits e tags próprios no GitHub, com as mesmas etapas e arquivos da preparação local.

O README contém o roteiro completo para executar com Docker e os comandos de publicação.
Os resultados Docker descritos no roteiro são expectativas do exercício, não evidências de execução.
