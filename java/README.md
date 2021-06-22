Test installation java
========================

Installation
------------

- tomcat se lance à la main
- `SET JAVA_HOME="C:\Progra~1\Java\jdk-16.0.1"`
- utiliser le fichier `settings.xml` pour la configuration de Maven via <http://nexus.unc.nc/>

Versions
--------

```shell
java --version
```

Test minimal
------------

```shell
javac HelloWorld.java
java HelloWorld
```

Application de test (Tomcat, maven)
-----------------------------------

```shell
cd C:\apache-tomcat\...
startup.bat
```

Ensuite, aller sur <http://localhost:8080/> pour voir l'interface


cd c:\apache-tomcat-10.0.6

https://tomcat.apache.org/tomcat-10.0-doc/appdev/sample/

https://tomcat.apache.org/tomcat-10.0-doc/appdev/sample/sample.war

A mettre dans CATALINA_BASE/webapps directory

SET JAVA_HOME="C:\Progra~1\Java\jdk-16.0.1\"
SET CATALINA_HOME="C:\apache-tomcat-10.0.6\"

http://localhost:8080/sample