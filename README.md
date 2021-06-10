Procédures de tests des logiciels INFO UNC
==========================================

Ce projet rassemble les tests à effectuer sur les installations des logiciels demandés par la licence INFO à l'UNC pour en faire la recette.

Chaque logiciel a un sous-dossier où la procédure de test est décrite dans le fichier `README.md`. Le cas échéant, les fichiers necessaires aux tests sont dans le sous-dossier (e.g., programme minimal Python dont on doit réusier l'exécution).

Liste des logiciels
-------------------

Voir la liste sur OneDrive :

- Utilitaires
  + Java JRE : OK sur MASTER 
  + Notepad++ : OK sur MASTER 
- Navigateurs
  + Firefox : OK sur MASTER 
  + Chrome : OK sur MASTER 
  + Opera : PAS TESTÉ
- Outils Mathématiques
  + Mathematica (F) : PAS TESTÉ
  + Matlab (F) : PAS TESTÉ
  + SCILAB : PAS TESTÉ
- Informatique
  + Packet Tracer : PAS TESTÉ
  + Java
    * IntelliJ CE : OK sur MASTER
    * Tomcat ~~8~~ 10 : OK sur MASTER, dans `C:\apache-tomcat-10.0.6` à lancer à la main (pas en mode service)
    * SDK Oracle 16.0.1 : OK sur MASTER, `JAVA_HOME` défini
    * Maven : PAS TESTÉ, configurer le cache Nexus
  + Python 3, voir [sous-dossier](python/README.md)
    * pip : OK sur MASTER
    * Jinja et autres modules : OK sur MASTER
  + Docker, voir [sous-dossier](docker/README.md)
    * KO, pas possible d'activer Hyper-V dans VM
    * Voir dans l'image Linux et l'intérêt ?
  + Wampserver : PAS TESTÉ
  + PostgreSQL, voir [sous-dossier](postresql/README.md)
    * Dossier `data` : OK sur MASTER
    * CLI psql : OK sur MASTER
    * PgAdmin : OK sur MASTER
  + VSCode : OK sur MASTER
  + Git/Github
    * git : OK sur MASTER
    * GitHub Desktop : : OK sur MASTER, install local portable uniquement (dans `C:\install`)
  + WSL2 avec dernière version Ubuntu LTS (pour avoir notamment le compilateur C gcc)
    * KO, remplacé par une nouvelle image `InfoLinux` Ubuntu 20.04 
  + NodeJS, voir [sous-dossier](node/README.md)
    * node : OK sur MASTER
    * npm : OK sur MASTER, configurer le cache Nexus
  + Koala : PAS TESTÉ
  + Wireshark : OK sur MASTER
    * npcap 1.31 installé sans droits admin
  + VirtualBox + extensions pack : PAS TESTÉ, voir l'intérêt ?
  + Putty : PAS TESTÉ
- Autre
  + un répertoire partagé en écriture pour l’ enseignant  et en lecture seule pour les étudiants afin que ces derniers puissent récupérer des images ISO utilisé en TP pour déployer en autonomie des systèmes

Problème des montages réseau
----------------------------

Co-existence de deux chemins différents pour le repertoire utilisateur :

- `C:\Users\rthion`
- `\\sokar.unc.prod\lecteurpersonnel-staff\rthion`

Ceci a pour effet que **toutes les modifications** faites en local dans l'espace utilisateur (e.g., les extensions VScode, les modules `npm` ou `pip`) disparaissent. Pour éviter cela il faut **configurer Horizon pour qu'il maintiennent les configurations dans `%UserProfile%`.

**Fait sur le Master pour les logiciels identifiés**

### Impossible de créer des programmes Node.js sur le dossier personnel réseau

**TODO** : une partie des logiciels **refuse** de s'exécuter sur le dosier partagé.

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
