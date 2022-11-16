#!/bin/bash

echo Backing up...

docker exec -i jurassicpark-db mysqldump -uroot -pexample --create-options --add-drop-database --databases JurassicPark > ../JurassicPark.sql

echo Backup complete.