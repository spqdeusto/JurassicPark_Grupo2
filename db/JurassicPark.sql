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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todoterreno`
--

LOCK TABLES `todoterreno` WRITE;
/*!40000 ALTER TABLE `todoterreno` DISABLE KEYS */;
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

-- Dump completed on 2022-11-15 23:58:52
