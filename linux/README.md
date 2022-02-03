# Notes installations WSL2/Linux

Liste des paquets dépôts à ajouter et des paquets à installer.

## TODO de base

- vérifier que les mirroirs des depôts NC <http://ubuntu.lagoon.nc/ubuntu/> sont bien utilisés

## Dépôts

```bash
# GCC
sudo add-apt-repository ppa:ubuntu-toolchain-r/test

# Postgres, voir https://www.postgresql.org/download/linux/ubuntu/
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt update
```

## Paquets

Outils système et réseau, PostgreSQL et chaines de compilation C/C++.

```bash
sudo apt install autojump byobu most fonts-powerline
sudo apt install gcc-11 g++-11 clang clang-tidy clang-format llvm lldb cmake  cmake-doc ninja-build gcc-11-locales gcc-11-doc libstdc++-11-doc llvm-10-doc 
sudo apt install tcptraceroute traceroute net-tools iputils-ping iproute2 whois wget curl httpie
sudo apt install postgresql-14 postgresql-contrib postgresql-14-postgis-3 postgresql-14-pgrouting postgresql-14-hypopg pgbadger pgtop


# pour ajouter l'alternative gcc
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 100 --slave /usr/bin/g++ g++ /usr/bin/g++-11 --slave /usr/bin/gcov gcov /usr/bin/gcov-11
```
