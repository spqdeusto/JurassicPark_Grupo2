#!/bin/bash

@echo off

echo Restoring...

docker exec -i jurassicpark-db mysql -uroot -pexample -h localhost < ../JurassicPark.sql

echo Database restored.