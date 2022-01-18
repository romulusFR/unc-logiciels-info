# Notes installations WSL2/Linux

Liste des paquets dépôts à ajouter et des paquets à installer.

**ONGOING WORK**

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

Outils système, PostgreSQL et chaines de compilation C/C++

```bash
sudo apt install autojump byobu most fonts-powerline
sudo apt install gcc-10 g++-10 clang clang-tidy clang-format llvm lldb cmake
sudo apt htop iotop
sudo apt install tcptraceroute traceroute net-tools iputils-ping iproute2 whois
sudo apt install postgresql-14 postgresql-contrib postgresql-14-postgis-3 postgresql-14-pgrouting pgbadger pgtop


# pour ajouter l'alternative gcc
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave /usr/bin/g++ g++ /usr/bin/g++-10 --slave /usr/bin/gcov gcov /usr/bin/gcov-10
```
