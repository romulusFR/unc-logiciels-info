Test installation java
========================

Installation
------------

- tomcat se lance à la main
- `SET JAVA_HOME="C:\Progra~1\Java\jdk-16.0.1"`
- utiliser le fichier `settings.xml` pour la configuration de Maven via <http://nexus.unc.nc/>
- copier le fichier `setenv.bat`

Versions
--------

```bat
java --version
```

Test minimal
------------

```bat
javac HelloWorld.java
java HelloWorld
```

Application de test (Tomcat, maven)
-----------------------------------

- On définit `SET CATALINA_HOME="C:\apache-tomcat-10.0.6\"` ou `SET CATALINA_HOME="C:\apache-tomcat-9.0.48\"` selon la version.
- Copier le fichier `setenv.bat` dans `%CATALINA_HOME%\bin` (défini `SET JAVA_HOME="C:\Progra~1\Java\jdk-16.0.1\"`)
- Exécuter ensuite `cd %CATALINA_HOME%\bin; startup.bat`

Ensuite, aller sur <http://localhost:8080/> pour voir l'interface de Tomcat s'il est bien lancé.

Pour le test d'une application `war` :

- Copier le fichier <https://tomcat.apache.org/tomcat-9.0-doc/appdev/sample/sample.war> dans `%CATALINA_HOME%\WepApps`
- Visiter <http://localhost:8080/sample>
