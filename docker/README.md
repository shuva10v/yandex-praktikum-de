# Workshop по Docker

## Демонстрация

### Сборка простого образа

В папке [simple_dockerfile](./simple_dockerfile):
```
docker build . -t simple_app
docker run --rm simple_app
docker images 
docker rmi
```

### docker-compose

В папке [simple_docker_compose](./simple_docker_compose):

```
python -c "from random import choice; print('SECURE_PASSWORD=' + ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_)') for i in range(10)]))"  > .env
cd visualisation
docker build . -t visualisation
cd ../
docker compose build
docker compose up -d
docker compose logs --tail=10 -f
```

### Пример сборки через gradle

В папке [gradle_sample](./gradle_sample):

```
./gradlew docker
docker run --rm gradle_sample
```