Procédures de tests des logiciels INFO UNC
==========================================

Ce projet rassemble les tests à effectuer sur les installations des logiciels demandés par la licence INFO à l'UNC pour en faire la recette.

Chaque logiciel a un sous-dossier où la procédure de test est décrite dans le fichier `README.md`. Le cas échéant, les fichiers necessaires aux tests sont dans le sous-dossier (e.g., programme minimal Python dont on doit réusier l'exécution).

Liste des logiciels
-------------------

Voir la liste sur OneDrive :

- Utilitaires
  + Java
  + Notepad++
- Navigateurs
  + Firefox
  + Chrome
  + Opera
- Outils Mathématiques
  + Mathematica (F)
  + Matlab (F)
  + SCILAB
- Informatique
  + Packet Tracer
  + IntelliJ
  + Tomcat 8
  + Python 3 (avec pip), voir [sous-dossier](python/README.md)
    * Jinja et autres modules pip : vérifier l'installation pip
  + Docker
  + Wampserver
  + PostgreSQL, voir [sous-dossier](postresql/README.md)
    * CLI psql
    * PgAdmin
  + VSCode
  + git
  + GitHub Desktop
  + WSL2 avec dernière version Ubuntu LTS (pour avoir notamment le compilateur C gcc)
  + NodeJS, voir [sous-dossier](node/README.md)
  + Koala
  + Wireshark
  + VirtualBox + extensions pack
  + Putty
- Autre
  + un répertoire partagé en écriture pour l’ enseignant  et en lecture seule pour les étudiants afin que ces derniers puissent récupérer des images ISO utilisé en TP pour déployer en autonomie des systèmes



Problème des montages réseau
----------------------------

Il y a un élément dysfonctionnel **majeur** dans la configuration du master, la co-existence de deux chemins différents pour le repertoire utilisateur :

- `C:\Users\rthion`
- `\\sokar.unc.prod\lecteurpersonnel-staff\rthion`

Ceci a pour effet que **toutes les modifications** faites en local dans l'espace utilisateur (e.g., les extensions VScode, les modules `npm` ou `pip`) **DISPARAISSENT APRES LOGOUT**

De plus, une partie des logiciels **refuse** de s'exécuter sur le dosier partagé

### Impossible de créer des programmes Node.js sur le dossier personnel réseau

Impossible d'utiliser `npm install` sur le disque réseau.

```raw
'\\sokar.unc.prod\lecteurpersonnel-staff\rthion\Documents\tests_logiciels_info\node_express'
CMD.EXE a été démarré avec le chemin d’accès comme répertoire en
cours. Les chemins d’accès UNC ne sont pas prise en charge. Utilisation
du répertoire Windows par défaut.
```

### Impossible de créer des programmes python avec venv sur le dossier personnel réseau

La même chose pour les venv python.

```raw
WARNING: The scripts pip.exe, pip3.9.exe and pip3.exe are installed in 'C:\Users\rthion\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

Problème docker
---------------

```raw
C:\Users\rthion\Documents>docker pull node
Using default tag: latest
error during connect: This error may indicate that the docker daemon is not running.: Post "http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/images/create?fromImage=node&tag=latest": open //./pipe/docker_engine: Le fichier spécifié est introuvable.
```

Notes diverses
--------------

Chemin des install (dont node/npm) `cd %AppData%`.
