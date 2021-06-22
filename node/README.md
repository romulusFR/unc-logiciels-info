Test installation node
======================

Installation
------------

Préciser le `NODE_PATH` :

```shell
SET NODE_PATH=%AppData%\npm\node_modules

# donne la configuration courante
npm config get

# ; cli configs
# metrics-registry = "https://registry.npmjs.org/"
# scope = ""
# user-agent = "npm/6.14.13 node/v14.17.0 win32 x64"
# 
# ; builtin config undefined
# prefix = "C:\\Users\\rthion\\AppData\\Roaming\\npm"
# 
# ; node bin location = C:\Program Files\nodejs\node.exe
# ; cwd = C:\Users\rthion
# ; HOME = C:\Users\rthion
# ; "npm config ls -l" to show all defaults.
# 
# userconfig = "C:\\Users\\rthion\\.npmrc"
```

Versions
--------

Dans le terminal `Node` (et pas la CLI standard)

```shell
node --version
# v14.17.0

npm --version
# 6.14.13
```

Test minimal
------------

```shell
echo %PATH%
# C:\Users\rthion\AppData\Roaming\npm;...

# affichage hello world
node -e "console.log('hello world');"

# test installation espace utilisateur
npm install -g slugify

# /!\ erreur lors de l'import si NODE_PATH non défini
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
