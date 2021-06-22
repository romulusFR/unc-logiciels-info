Test installation Postgresql
============================

Installation
------------

Autoriser l'utilisateur `postgres` en mode `trust` en modifiant le fichier, `pg_hba.conf`, cf <https://stackoverflow.com/questions/27107557/what-is-the-default-password-for-postgres>

Versions
--------

A exécuter dans l'interface `psql` (lien ad hoc dans le menu Démarrer)

```sql
SELECT version();
```

Test minimal
------------

Exécuter le script suivant

```sql
DROP TABLE IF EXISTS test;
CREATE TABLE test("id" integer PRIMARY KEY, content text);
INSERT INTO test (SELECT i, md5('test' || i::text) FROM generate_series(1, 1000) AS g(i));
SELECT * FROM test ORDER BY random() FETCH FIRST 10 ROWS ONLY;
DROP TABLE test;
VACUUM;
```
