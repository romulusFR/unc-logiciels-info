Test installation docker
========================

Versions
--------

```shell
docker --version
Docker version 20.10.7, build f0df350
```

Test minimal
------------

Voir <https://docs.docker.com/get-started/>

```shell
docker info

docker images
docker container ps --all

docker run hello-world
# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# b8dfde127a29: Pull complete 
# ...

docker images
docker container ps --all
# on doit voir l'image et le container arrêté
```