Elements de la recette de l'installation des logiciels info
===========================================================

Montage réseau
--------------

**LES INSTALLS "locales" dans le user space (e.g., les extensions VScode, les module node ou pip) DISPARAISSENT APRES LOGOUT**

racine du mal _C:\Users\rthion versus  \\sokar.unc.prod\lecteurpersonnel-staff\rthion_


'\\sokar.unc.prod\lecteurpersonnel-staff\rthion\Documents\tests_logiciels_info\node_express'
CMD.EXE a été démarré avec le chemin d’accès comme répertoire en
cours. Les chemins d’accès UNC ne sont pas prise en charge. Utilisation
du répertoire Windows par défaut.

>>> impossible de faire npm install sur le disque réseau

**idem venv python**

C:\Users\rthion\Documents>docker pull node
Using default tag: latest
error during connect: This error may indicate that the docker daemon is not running.: Post "http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.24/images/create?fromImage=node&tag=latest": open //./pipe/docker_engine: Le fichier spécifié est introuvable.


WARNING: The scripts pip.exe, pip3.9.exe and pip3.exe are installed in 'C:\Users\rthion\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

Notes
-----

Chemin des install (dont node/npm)
cd %AppData%
