Dockerization of flask_blog:

$docker run --name db -e MYSQL_ROOT_PASSWORD=test -d -p 3306:3306 mariadb

$docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mariadb             latest              abcee1d29aac        3 days ago          396MB
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
da9e0874f0bb        mariadb             "docker-entrypoint..."   About a minute ago   Up About a minute   0.0.0.0:3306->3306/tcp   db


$docker run --name mysql-client -it --link db:mysql --rm mariadb sh -c 'exec mysql -uroot -ptest -hmysql'

MariaDB [(none)]> create database test_news;
Query OK, 1 row affected (0.00 sec)

$ docker build -t flask_blog .

$ docker run -id -p 5000:5000 -v /home/nsn/flask_blog:/opt/flask_blog --name blog --link db:mysql flask_blog bash

$ docker exec -it blog bash
root@10309e471b3d:/opt/flask_blog# ls
Dockerfile  app.py  requirements.txt  templates
root@10309e471b3d:/opt/flask_blog# python app.py runserver

open browser http://localhost:5000/
