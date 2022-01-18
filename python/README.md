Test installation Python
========================

**TODO** : à passer en 3.10

Installation
------------

- ajout du `PATH`
  - pip config -v list
- chemin de pip
  - dont `C:\Users\rthion\AppData\Roaming\pip\pip.ini`

**TODO** mettre le fichier `.ini` par défaut pour utiliser le dépôt <http://nexus.unc.nc/>.

Dans toute la suite, on désigne par `py` l'exécutable de l'interpréteur Python.

Versions
--------

```shell
py --version
# Python 3.9.1

pip --version
# erreur /!\

py -m pip --version
# pip 20.2.3 from C:\Program Files\Python39\lib\site-packages\pip (python 3.9)

# màj de pip dans l'espace utilisateur
py -m pip install --upgrade pip
# Successfully installed pip-21.1.2

py -m pip cache dir
# c:\users\rthion\appdata\local\pip\cache

py -m pip install python-slugify

py -c "import slugify; s = slugify.slugify('Un, test cet été ?'); print(s)"
```

Modules à installer
-------------------

Voir dans le fichier `requirements.txt`, puis `py -m pip install -r requirements.txt` [syntaxe du fichier](https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format).

Application de test
-------------------

```shell
# serveur web minimaliste
py -m http.server
# on doit pouvoir aller sur http://127.0.0.1:8000/ et voir une page avec la liste des document où on a exécutée la commande

py -m venv .env

# sous PS
.env\Scripts\Activate.ps1

# /!\ erreur
# .\.env\Scripts\Activate.ps1 : Impossible de charger le fichier \\sokar.unc.prod\lecteurpersonnel-staff\rthion\Documents\tests_logiciels_info\python\.env\Scripts\Activate.ps1, car l’exécution de scripts est désactivée sur ce système. Pour plus d’informations, consultez about_Execution_Policies à l’adresse https://go.microsoft.com/fwlink/?LinkID=135170.

# sous CMD
.env\Scripts\activate.bat

# lancer le serveur Flask
python app.py
# aller à l'adresse indiquée

#  pour quitter le venv
deactivate
```
