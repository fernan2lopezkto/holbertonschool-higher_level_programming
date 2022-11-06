SQL_introduction

======================
|                    |
|  spanish version:  |
======================

<h1>----> Proyecto introductorio a gestion de bases de datos.</h1>

en este proyecto mediante scripts sql aprenderemos los conceptos basicos en MySQL Server.

<h1>----> Notas propias de conocimientos aprendidos</h1>

->Cómo instalar MySQL en Ubuntu 20.04 ???


INSTALAR MYSQL

sudo apt update
sudo apt-cache search mysql-server
sudo apt install mysql-server-8.0

CREAR USUARIO Y CONTRASEÑA

sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
exit

CONFIGURACIÓN

sudo systemctl start mysql.service
sudo mysql_secure_installation
sudo systemctl is-enabled mysql.service

---- comandos basicos -----

-  para ver todas las bases de datos existentes escribimos el siguiente comando.
 SHOW DATABASES;

<a href="https://conclase.net/mysql/curso/sqlsen/SHOW">
 SHOW proporciona información sobre bases de datos, tablas, columnas o información de estado sobre el servidor.</a>

- CREATE DATABASE crea una base de datos con el nombre dado. Para usar CREATE DATABASE se necesita el privilegio CREATE en la base de datos.
CREATE DATABASE [nombre_de_la_nueva_base_de_datos];
si la base de datos no existe se puede aregar [IF NOT EXISTS] para evitar que nos de un error

- para borrar una base de datos usamos:
DROP DATABASE IF EXISTS [nombre_de_la_base_de_datos];

- CREATE efectivamente es para crear como en el caso a continuacion una tabla por ejemplo
<pre><code>
CREATE TABLE IF NOT EXISTS [mombre_de_la_nueva_tabla] (
    id INT, 
    name VARCHAR(256)
)
</code></pre>