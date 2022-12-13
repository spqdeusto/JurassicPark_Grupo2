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
  PRIMARY KEY (`nombre`),
  KEY `especie` (`especie`),
  CONSTRAINT `dinosaurio_ibfk_1` FOREIGN KEY (`especie`) REFERENCES `especie` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dinosaurio`
--

LOCK TABLES `dinosaurio` WRITE;
/*!40000 ALTER TABLE `dinosaurio` DISABLE KEYS */;
INSERT INTO `dinosaurio` VALUES ('Ainhoa',1,40,240,'H'),('Aitor',1,23,100,'M'),('Alvaro',1,60,300,'M'),('Ana',6,900,967,'H'),('Andrea',5,88,889,'H'),('Ane',2,208,150,'H'),('Anton',3,500,600,'M'),('Aritz',3,10,40,'M'),('Borja',4,5,20,'M'),('Elena',3,15,30,'M'),('Elvira',7,41,245,'H'),('Ester',5,74,770,'H'),('Fonsi',7,18,100,'M'),('Gorka',2,100,220,'M'),('Iker',2,45,130,'H'),('Irati',5,44,766,'H'),('Irene',4,22,240,'H'),('Javier',7,82,666,'M'),('Jose',4,77,383,'M'),('Juan',3,30,87,'M'),('Laura',4,47,99,'H'),('Leire',5,66,400,'H'),('Mamen',4,90,900,'H'),('Maria',6,21,210,'M'),('Mertxe',5,58,98,'H'),('Monica',6,90,240,'H'),('Naroa',1,22,200,'H'),('Olatz',2,400,280,'H'),('Pablo',6,85,765,'M'),('Paloma',7,99,906,'H'),('Paul',3,550,320,'M'),('Ruben',1,300,350,'M'),('Sebastian',6,600,600,'H'),('Tristan',7,11,35,'M'),('Unai',2,70,110,'M');
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
  `es_agresivo` tinyint(1) NOT NULL,
  `recinto` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `recinto` (`recinto`),
  CONSTRAINT `especie_ibfk_1` FOREIGN KEY (`recinto`) REFERENCES `recinto` (`codigo`) ON DELETE CASCADE,
  CONSTRAINT `especie_chk_1` CHECK ((`es_agresivo` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especie`
--

LOCK TABLES `especie` WRITE;
/*!40000 ALTER TABLE `especie` DISABLE KEYS */;
INSERT INTO `especie` VALUES (1,'Dilophosaurus',1,1),(2,'T-Rex',1,2),(3,'Velociraptor',1,3),(4,'Brachiosaurus',0,4),(5,'Parasaulophus',0,4),(6,'Galliminus',0,5),(7,'Triceratops',0,6);
/*!40000 ALTER TABLE `especie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recinto`
--

DROP TABLE IF EXISTS `recinto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recinto` (
  `codigo` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `sis_elec` tinyint(1) NOT NULL,
  PRIMARY KEY (`codigo`),
  CONSTRAINT `recinto_chk_1` CHECK ((`sis_elec` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recinto`
--

LOCK TABLES `recinto` WRITE;
/*!40000 ALTER TABLE `recinto` DISABLE KEYS */;
INSERT INTO `recinto` VALUES (1,'Recinto del Dilophosaurus',0),(2,'Recinto del T-Rex',0),(3,'Recinto de los Velociraptores',1),(4,'Recinto de los Brachiosaurus y de Parasaulophus',0),(5,'Recinto de Galliminus',0),(6,'Recinto de Triceratops',1);
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
  `recinto` int NOT NULL,
  PRIMARY KEY (`codigo`),
  KEY `recinto` (`recinto`),
  CONSTRAINT `todoterreno_ibfk_1` FOREIGN KEY (`recinto`) REFERENCES `recinto` (`codigo`) ON DELETE CASCADE,
  CONSTRAINT `todoterreno_chk_1` CHECK (((`pasajeros` > 1) and (`pasajeros` < 6))),
  CONSTRAINT `todoterreno_chk_2` CHECK ((`ruta` in (0,1))),
  CONSTRAINT `todoterreno_chk_3` CHECK ((`sis_seg` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=1021 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todoterreno`
--

LOCK TABLES `todoterreno` WRITE;
/*!40000 ALTER TABLE `todoterreno` DISABLE KEYS */;
INSERT INTO `todoterreno` VALUES (1000,1,4,1,1),(1001,0,3,1,1),(1002,0,2,1,1),(1003,1,5,1,2),(1004,1,3,1,2),(1005,0,2,1,2),(1006,0,5,1,3),(1007,1,4,1,3),(1008,1,5,1,3),(1009,1,2,0,4),(1010,1,5,0,4),(1011,1,5,0,4),(1012,0,5,0,4),(1013,0,5,0,4),(1014,0,4,0,4),(1015,1,4,0,5),(1016,1,4,0,5),(1017,1,3,0,5),(1018,0,4,0,6),(1019,1,3,0,6),(1020,0,2,0,6);
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

-- Dump completed on 2022-12-13 10:57:34
