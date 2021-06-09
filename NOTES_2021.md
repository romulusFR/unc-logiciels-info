Elements de la recette de l'installation des logiciels info
===========================================================

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
-----

Chemin des install (dont node/npm) `cd %AppData%`.
