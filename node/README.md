Test installation node
======================

Versions
--------

```shell
node --version
# v14.17.0

npm --version
# 6.14.13
```

Test minimal
------------

```shell
# affichage hello world
node -e "console.log('hello world');"

# test installation espace utilisateur
npm install -g eslint
```

Application de test
-------------------

```shell
# dans le dossier des tests node

# téléchargement et installation de express
npm install

# lancement de l'application
node index.js

# on doit pouvoir aller sur http://127.0.0.1:3000/ et voir une page
```
