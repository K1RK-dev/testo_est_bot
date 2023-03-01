-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: testo_db
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

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
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(40) DEFAULT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `cart` varchar(120) DEFAULT NULL,
  `cart_price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_name` varchar(64) DEFAULT NULL,
  `prize_count` int DEFAULT NULL,
  `enabled` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events_members`
--

DROP TABLE IF EXISTS `events_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events_members` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) DEFAULT NULL,
  `last_attempt_timestamp` timestamp NULL DEFAULT NULL,
  `prize` varchar(64) DEFAULT NULL,
  `attempt_count` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events_members`
--

LOCK TABLES `events_members` WRITE;
/*!40000 ALTER TABLE `events_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `events_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) DEFAULT NULL,
  `order` varchar(150) DEFAULT NULL,
  `order_price` double DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `order_dt` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_menu`
--

DROP TABLE IF EXISTS `product_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_menu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(60) NOT NULL COMMENT 'Название продукта',
  `product_price` varchar(10) NOT NULL,
  `ingredients` varchar(150) DEFAULT NULL,
  `article` varchar(5) NOT NULL,
  `photo_id` varchar(200) DEFAULT NULL,
  `size` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_menu`
--

LOCK TABLES `product_menu` WRITE;
/*!40000 ALTER TABLE `product_menu` DISABLE KEYS */;
INSERT INTO `product_menu` VALUES (1,'Пицца Пеперони','549','Тесто,Томатный соус,Пеперони,Моцарелла','00001','-217833719_457239146','33'),(2,'Пицца Пеперони','699','Тесто,Томатный соус,Пеперони,Моцарелла','00002','-217833719_457239146','40'),(3,'Пицца Грибная','549','Тесто,Соус тар-тар,Шампиньоны,Маринованный лук,Ветчина,Моцарелла','00003','-217833719_457239143','33'),(4,'Пицца Грибная','699','Тесто,Соус тар-тар,Шампиньоны,Маринованный лук,Ветчина,Моцарелла','00004','-217833719_457239143','40'),(5,'Пицца Пикантная','549','Тесто,Фирменный соус,Куриное филе,Пеперони,Халапеньо,Моцарелла,Перец болгарский','00005','-217833719_457239147','33'),(6,'Пицца Пикантная','699','Тесто,Фирменный соус,Куриное филе,Пеперони,Халапеньо,Моцарелла,Перец болгарский','00006','-217833719_457239147','40'),(7,'Пицца Барбекю','549','Тесто,Соус барбекю,Рулет свинной,Курица,Шампиньоны,Моцарелла,Бекон,Укроп','00007','-217833719_457239140','33'),(8,'Пицца Барбекю','699','Тесто,Соус 1000 островов,Рулет свинной,Ветчина,Куриное филе,Тирольские колбаски,Шампиньоны,Маринованный лук,Помидоры,Моцарелла','00008','-217833719_457239140','40'),(9,'Пицца Мясная','549','Тесто,Соус 1000 островов,Рулет свинной,Ветчина,Куриное филе,Тирольские колбаски,Шампиньоны,Маринованный лук,Помидоры,Моцарелла','00009','-217833719_457239144','33'),(10,'Пицца Мясная','699','Тесто,Соус 1000 островов,Рулет свинной,Ветчина,Куриное филе,Тирольские колбаски,Шампиньоны,Маринованный лук,Помидоры,Моцарелла','00010','-217833719_457239144','40'),(11,'Пицца Биг тести','549','Тесто,Соус бургер,Фарш говяжий,Салат,Маринованный лук,Помидоры,Моцарелла,Плавленный сыр','00011','-217833719_457239141','33'),(12,'Пицца Биг тести','699','Тесто,Соус бургер,Фарш говяжий,Салат,Маринованный лук,Помидоры,Моцарелла,Плавленный сыр','00012','-217833719_457239141','40'),(17,'Пицца Нежная','549','Тесто,Соус сливочный,Ветчина,Шампиньоны,Моцарелла','00017','-217833719_457239145','33'),(18,'Пицца Нежная','699','Тесто,Соус сливочный,Ветчина,Шампиньоны,Моцарелла','00018','-217833719_457239145','40'),(19,'Пицца Цезарь','549','Тесто,Соус тар-тар,Куриное филе,Капуста пекинская,Моцарелла,Сыр плавленный,Помидоры','00019','-217833719_457239149','33'),(20,'Пицца Цезарь','699','Тесто,Соус тар-тар,Куриное филе,Капуста пекинская,Моцарелла,Сыр плавленный,Помидоры','00020','-217833719_457239149','40'),(21,'Пицца Сливочная пеперони','549','Тесто,Соус сливочный,Пеперони,Шампиньоны,Моцарелла','00021','-217833719_457239148','33'),(22,'Пицца Сливочная пеперони','699','Тесто,Соус сливочный,Пеперони,Шампиньоны,Моцарелла','00022','-217833719_457239148','40'),(23,'Пицца Гавайская','549','Тесто,Соус сливочный,Ветчина,Рулет свинной,Ананасы,Моцарелла','00023','-217833719_457239142','33'),(24,'Пицца Гавайская','699','Тесто,Соус сливочный,Ветчина,Рулет свинной,Ананасы,Моцарелла','00024','-217833719_457239142','40');
/*!40000 ALTER TABLE `product_menu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-01 23:32:57
