# Procédures de tests des logiciels INFO UNC

Ce projet rassemble les tests à effectuer sur les installations des logiciels demandés par la licence INFO à l'UNC pour en faire la recette.
Complète la liste de la DNSI qui maintient les version installées <https://confluence.unc.nc/display/DI/2021+-+Applications+machines+Horizon>.

Chaque environnement de développement a un sous-dossier où la procédure de test est décrite dans le fichier `README.md`.
Le cas échéant, les fichiers necessaires aux tests sont dans le sous-dossier (e.g., programme minimal Python dont on doit réussir l'exécution).

## Liste des principaux environnements

Voir la liste et l'onglet "Recette" sur le OneDrive (accès restreint, demander par email).
Pour les détails des configuration et tests effectués :

- Java, Tomcat, Maven voir [sous-dossier](java/README.md)
- Docker, voir [sous-dossier](docker/README.md)
- PostgreSQL, psql, PGAdmin voir [sous-dossier](postresql/README.md)
- NodeJS, npm, voir [sous-dossier](node/README.md)
- Python, pip, venv, voir [sous-dossier](python/README.md)
- WSL2/Ubuntu, voir [sous-dossier](linux/README.md)

## Problèmes généraux

### Configuration de profil ad hoc des logiciels

Co-existence de deux chemins différents pour le repertoire utilisateur :

- `C:\Users\rthion`
- `\\sokar.unc.prod\lecteurpersonnel-staff\rthion`

Ceci a pour effet que **toutes les modifications** faites en local dans l'espace utilisateur (e.g., les extensions VScode, les modules `npm` ou `pip`) disparaissent. Pour éviter cela il faut \*\*configurer Horizon pour qu'il maintiennent les configurations dans `%UserProfile%` ou `%AppData%` et possiblement d'autres chemin selon les logiciels.

### Impossible de créer des programmes sur le dossier personnel réseau

**TODO** : une partie des logiciels **refuse** de s'exécuter sur le dosier partagé.

Impossible d'utiliser `npm install` sur le disque réseau, idem pour les `venv` python.

```raw
'\\sokar.unc.prod\lecteurpersonnel-staff\rthion\Documents\tests_logiciels_info\node_express'
CMD.EXE a été démarré avec le chemin d’accès comme répertoire en
cours. Les chemins d’accès UNC ne sont pas prise en charge. Utilisation
du répertoire Windows par défaut.
```

```raw
WARNING: The scripts pip.exe, pip3.9.exe and pip3.exe are installed in 'C:\Users\rthion\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```
