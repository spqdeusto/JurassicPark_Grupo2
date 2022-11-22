-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: JurassicPark
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `JurassicPark`
--

/*!40000 DROP DATABASE IF EXISTS `JurassicPark`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `JurassicPark` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `JurassicPark`;

--
-- Table structure for table `dinosaurio`
--

DROP TABLE IF EXISTS `dinosaurio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dinosaurio` (
  `nombre` varchar(100) NOT NULL,
  `especie` int NOT NULL,
  `edad` int DEFAULT NULL,
  `peso` int DEFAULT NULL,
  `sexo` varchar(2) DEFAULT NULL,
  `es_agresivo` tinyint(1) NOT NULL,
  `recinto` varchar(100) NOT NULL,
  PRIMARY KEY (`nombre`),
  KEY `especie` (`especie`),
  KEY `recinto` (`recinto`),
  CONSTRAINT `dinosaurio_ibfk_1` FOREIGN KEY (`especie`) REFERENCES `especie` (`id`) ON DELETE CASCADE,
  CONSTRAINT `dinosaurio_ibfk_2` FOREIGN KEY (`recinto`) REFERENCES `recinto` (`nombre`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dinosaurio`
--

LOCK TABLES `dinosaurio` WRITE;
/*!40000 ALTER TABLE `dinosaurio` DISABLE KEYS */;
INSERT INTO `dinosaurio` VALUES ('Ainhoa',1,40,240,'H',1,'Recinto del Dilophosaurus'),('Aitor',1,23,100,'M',1,'Recinto del Dilophosaurus'),('Alvaro',1,60,300,'M',1,'Recinto del Dilophosaurus'),('Ana',6,900,967,'H',0,'Recinto de Galliminus'),('Andrea',5,88,889,'H',0,'Recinto de Parasaulophus'),('Ane',2,208,150,'H',1,'Recinto del T-Rex'),('Anton',3,500,600,'M',1,'Recinto de los Velociraptores'),('Aritz',3,10,40,'M',1,'Recinto de los Velociraptores'),('Borja',4,5,20,'M',0,'Recinto de Brachiosaurus'),('Elena',3,15,30,'M',1,'Recinto de los Velociraptores'),('Elvira',7,41,245,'H',0,'Recinto de Triceratops'),('Ester',5,74,770,'H',0,'Recinto de Parasaulophus'),('Fonsi',7,18,100,'M',0,'Recinto de Triceratops'),('Gorka',2,100,220,'M',1,'Recinto del T-Rex'),('Iker',2,45,130,'H',1,'Recinto del T-Rex'),('Irati',5,44,766,'H',0,'Recinto de Parasaulophus'),('Irene',4,22,240,'H',0,'Recinto de Brachiosaurus'),('Javier',7,82,666,'M',0,'Recinto de Triceratops'),('Jose',4,77,383,'M',0,'Recinto de Brachiosaurus'),('Juan',3,30,87,'M',1,'Recinto de los Velociraptores'),('Laura',4,47,99,'H',0,'Recinto de Brachiosaurus'),('Leire',5,66,400,'H',0,'Recinto de Parasaulophus'),('Mamen',4,90,900,'H',0,'Recinto de Brachiosaurus'),('Maria',6,21,210,'M',0,'Recinto de Galliminus'),('Mertxe',5,58,98,'H',0,'Recinto de Parasaulophus'),('Monica',6,90,240,'H',0,'Recinto de Galliminus'),('Naroa',1,22,200,'H',1,'Recinto del Dilophosaurus'),('Olatz',2,400,280,'H',1,'Recinto del T-Rex'),('Pablo',6,85,765,'M',0,'Recinto de Galliminus'),('Paloma',7,99,906,'H',0,'Recinto de Triceratops'),('Paul',3,550,320,'M',1,'Recinto de los Velociraptores'),('Ruben',1,300,350,'M',1,'Recinto del Dilophosaurus'),('Sebastian',6,600,600,'H',0,'Recinto de Galliminus'),('Tristan',7,11,35,'M',0,'Recinto de Triceratops'),('Unai',2,70,110,'M',1,'Recinto del T-Rex');
/*!40000 ALTER TABLE `dinosaurio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especie`
--

DROP TABLE IF EXISTS `especie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especie` (
  `id` int NOT NULL AUTO_INCREMENT,
  `especie` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especie`
--

LOCK TABLES `especie` WRITE;
/*!40000 ALTER TABLE `especie` DISABLE KEYS */;
INSERT INTO `especie` VALUES (1,'Dilophosaurus'),(2,'T-Rex'),(3,'Velociraptor'),(4,'Brachiosaurus'),(5,'Parasaulophus'),(6,'Galliminus'),(7,'Triceratops');
/*!40000 ALTER TABLE `especie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recinto`
--

DROP TABLE IF EXISTS `recinto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recinto` (
  `nombre` varchar(100) NOT NULL,
  `especie` int NOT NULL,
  `sis_elec` tinyint(1) NOT NULL,
  PRIMARY KEY (`nombre`),
  KEY `especie` (`especie`),
  CONSTRAINT `recinto_ibfk_1` FOREIGN KEY (`especie`) REFERENCES `especie` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recinto`
--

LOCK TABLES `recinto` WRITE;
/*!40000 ALTER TABLE `recinto` DISABLE KEYS */;
INSERT INTO `recinto` VALUES ('Recinto de Brachiosaurus',4,0),('Recinto de Galliminus',6,0),('Recinto de los Velociraptores',3,1),('Recinto de Parasaulophus',5,0),('Recinto de Triceratops',7,0),('Recinto del Dilophosaurus',1,1),('Recinto del T-Rex',2,1);
/*!40000 ALTER TABLE `recinto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `todoterreno`
--

DROP TABLE IF EXISTS `todoterreno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `todoterreno` (
  `codigo` int NOT NULL AUTO_INCREMENT,
  `ruta` tinyint(1) NOT NULL,
  `pasajeros` int DEFAULT NULL,
  `sis_seg` tinyint(1) NOT NULL,
  `recinto` varchar(100) NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `recinto` (`recinto`),
  CONSTRAINT `todoterreno_ibfk_1` FOREIGN KEY (`recinto`) REFERENCES `recinto` (`nombre`) ON DELETE CASCADE,
  CONSTRAINT `todoterreno_chk_1` CHECK (((`pasajeros` > 1) and (`pasajeros` < 6)))
) ENGINE=InnoDB AUTO_INCREMENT=1021 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todoterreno`
--

LOCK TABLES `todoterreno` WRITE;
/*!40000 ALTER TABLE `todoterreno` DISABLE KEYS */;
INSERT INTO `todoterreno` VALUES (1000,1,4,1,'Recinto del Dilophosaurus'),(1001,0,3,1,'Recinto del Dilophosaurus'),(1002,0,2,1,'Recinto del Dilophosaurus'),(1003,1,5,1,'Recinto del T-Rex'),(1004,1,3,1,'Recinto del T-Rex'),(1005,0,2,1,'Recinto del T-Rex'),(1006,0,5,1,'Recinto de los Velociraptores'),(1007,1,4,1,'Recinto de los Velociraptores'),(1008,1,5,1,'Recinto de los Velociraptores'),(1009,1,2,0,'Recinto de Brachiosaurus'),(1010,1,5,0,'Recinto de Brachiosaurus'),(1011,1,5,0,'Recinto de Brachiosaurus'),(1012,0,5,0,'Recinto de Parasaulophus'),(1013,0,5,0,'Recinto de Parasaulophus'),(1014,0,4,0,'Recinto de Parasaulophus'),(1015,1,4,0,'Recinto de Galliminus'),(1016,1,4,0,'Recinto de Galliminus'),(1017,1,3,0,'Recinto de Galliminus'),(1018,0,4,0,'Recinto de Triceratops'),(1019,1,3,0,'Recinto de Triceratops'),(1020,0,2,0,'Recinto de Triceratops');
/*!40000 ALTER TABLE `todoterreno` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-22 19:02:48
