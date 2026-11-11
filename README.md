# Atividade prática - Aula 05: Docker

Gerência de Configuração - UNIGRAN - 10/11/2026.
Base: https://github.com/ezefferth/gc-pratica-pr. As etapas da atividade foram registradas em commits e tags.
O projeto usa o template indicado no PDF; não é preciso instalar Python para rodar os containers.

## Entrega

- `Dockerfile`: Python 3.13 slim, pasta `/app`, cópia do projeto e CMD em lista.
- `calculadora.py`: subtração `a - b` e média por `len(numeros)`.
- `.dockerignore`: exclui `.git`, `Dockerfile`, `.dockerignore`, caches e configurações locais.
- Tags Git: `v1.0.0`, `v1.1.0-antes-dockerignore` e `v1.1.0`.
- Testes de regressão e workflow do GitHub Actions para conferir as etapas com Docker.

A saudação `Olá, nome!` foi preservada: a Parte 4 pede corrigir apenas os dois defeitos da calculadora.
Tags Git identificam revisões do código. As imagens Docker só existem depois dos builds abaixo.

## Pré-requisito

Docker instalado e em execução, configurado para containers Linux. Confira `docker info`.
Execute os comandos na raiz deste repositório. Use diretórios irmãos ainda inexistentes para os worktrees.

## Partes 1 a 3: versão original

O modelo já foi clonado. Reproduza a versão com os defeitos sem alterar o código atual:

```bash
git worktree add --detach ../gc-pratica-1.0.0 v1.0.0
docker build -t gc-pratica:1.0.0 ../gc-pratica-1.0.0
docker images gc-pratica
docker run --rm gc-pratica:1.0.0
docker run --rm gc-pratica:1.0.0 python --version
```

Saída esperada do programa:

```text
Hello, World!
Olá, nome!
2 + 3 = 5
10 - 4 = -6
média de 6, 8 e 10 = 12.0
```

O último comando mostra Python 3.13 seguido da versão de correção. `--rm` remove o container ao terminar.

## Parte 4: corrigir e montar outra imagem

A correção já está na revisão atual. A imagem antiga continua mostrando os defeitos:

```bash
docker run --rm gc-pratica:1.0.0
git worktree add --detach ../gc-pratica-parte4 v1.1.0-antes-dockerignore
docker build -t gc-pratica:1.1.0 ../gc-pratica-parte4
docker run --rm gc-pratica:1.1.0
docker run --rm gc-pratica:1.0.0
```

A 1.1.0 mostra `10 - 4 = 6` e `média de 6, 8 e 10 = 8.0`.
A 1.0.0 continua mostrando -6 e 12.0. Editar o código local não altera uma imagem já montada.

## Parte 5: excluir arquivos do contexto

Antes do `.dockerignore`, confira a presença de `.git` em `/app`:

```bash
docker run --rm gc-pratica:1.1.0 ls -a /app
```

No worktree, `.git` é um arquivo de referência; em um clone comum, é uma pasta.
Agora use a raiz atual, que contém o `.dockerignore`, e reconstrua a mesma tag, como pede a atividade:

```bash
docker build -t gc-pratica:1.1.0 .
docker run --rm gc-pratica:1.1.0 ls -a /app
docker run --rm gc-pratica:1.1.0
docker run --rm gc-pratica:1.1.0 python -m unittest discover -s tests -v
```

`.git`, `Dockerfile` e `.dockerignore` não aparecem na listagem final.
O Docker lê os dois arquivos de configuração, mas o `COPY . .` não os copia para `/app`.

## Respostas para discussão

1. **A versão 1.0.0 continuar errada é esperado?** Sim. Ela preserva o que foi empacotado naquele build, inclusive os defeitos. A correção exige outro build. Uma tag pode ser reposicionada; o digest identifica o conteúdo imutável de uma imagem.
2. **O que `python --version` esclarece?** Qual versão do interpretador executa dentro do container, independentemente do Python do computador. Isso elimina uma diferença comum no “funciona na minha máquina”, mas não comprova sozinho que dependências e entradas são iguais.
3. **`python:latest` produz o mesmo ambiente daqui a um ano?** Não há garantia: a tag muda. `python:3.13-slim` limita a linha e a variante, mas também recebe atualizações. Fixar o digest é necessário para fixar exatamente a imagem-base.

## Exercícios opcionais

Python interativo, saindo com `exit()`:

```bash
docker run -it --rm python:3.13-slim python
```

Três containers sem `--rm`, com nomes explícitos para remover apenas os desta prática:

```bash
docker run --name gc-aula05-1 gc-pratica:1.1.0
docker run --name gc-aula05-2 gc-pratica:1.1.0
docker run --name gc-aula05-3 gc-pratica:1.1.0
docker ps -a
docker rm gc-aula05-1 gc-aula05-2 gc-aula05-3
```

Dockerfile e `.dockerignore` já foram versionados.
A seção de Compose do PDF usa outro projeto, o site da demonstração. Um exemplo independente
com `compose.yaml`, Dockerfile e página HTML está em `estudo-compose/`, com instruções próprias.

## Limpeza ao terminar

```bash
docker image rm gc-pratica:1.0.0 gc-pratica:1.1.0
docker ps -a
git worktree remove ../gc-pratica-1.0.0
git worktree remove ../gc-pratica-parte4
```

Remova somente containers que você criou. Preserve as imagens `python`, `nginx` e `hello-world`.

## Verificação e publicação

Veja `VALIDACAO.md` para os testes efetivamente executados.
O workflow `.github/workflows/docker.yml` verificou com sucesso as imagens em um runner Linux com Docker:
[execução aprovada](https://github.com/Gabriel66482/gc-pratica-docker/actions/runs/42933619786).
Foram conferidos os resultados das duas versões, o Python 3.13, as exclusões do contexto, os testes e o Compose.

Repositório da entrega: https://github.com/Gabriel66482/gc-pratica-docker.
Para baixar a entrega com seu histórico e suas tags:

```bash
git clone https://github.com/Gabriel66482/gc-pratica-docker.git
cd gc-pratica-docker
```

O template do professor é somente a referência de origem; use o repositório acima para a entrega.

## Estrutura

| Arquivo | O que é |
|---|---|
| `saudacao.py` | mensagens: hello world, saudação e despedida |
| `calculadora.py` | operações: somar, subtrair e média |
| `main.py` | o programa: chama as funções e mostra o resultado |

## Referência: regras da aula 04

As regras abaixo pertencem ao exercício anterior, preservadas como referência do modelo.
A entrega desta aula registra a sequência Docker em commits e tags.

- Toda mudança começa por uma **issue**, com o que acontece hoje, o que deveria acontecer e o
  critério de aceite.
- O trabalho é feito em um **ramo por issue**, nomeado `tipo/numero-descricao` (`fix/1-saudacao`).
- As mensagens de commit seguem o padrão **Conventional Commits**: `tipo: resumo`, com `Refs #N` no
  rodapé quando houver corpo.
- Nada entra no `main` sem **pull request** revisado por outra pessoa. A descrição do PR traz
  `Closes #N`, e é o merge que fecha a issue.
