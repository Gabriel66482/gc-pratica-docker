# Estudo autônomo: Compose

Exemplo independente do site da demonstração. Execute nesta pasta:

```bash
docker compose up -d --build
docker compose ps
```

Abra http://localhost:8080 e confira a página. Em seguida:

```bash
docker compose down
docker image rm site:2.0.0
```

`down` remove os containers e a rede do projeto; a imagem é removida pelo comando seguinte.
O exemplo requer a porta 8080 livre.
