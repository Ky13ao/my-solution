-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hr
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `department_id` int NOT NULL,
  `department_name` varchar(30) DEFAULT NULL,
  `location_id` int DEFAULT NULL,
  PRIMARY KEY (`department_id`),
  KEY `d_index` (`location_id`) USING BTREE,
  KEY `d_index2` (`department_name`) USING BTREE,
  KEY `h_index` (`location_id`),
  KEY `h_index2` (`department_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (20,'Marketing',180),(30,'Purchasing',1700),(40,'Human Resources',2400),(50,'Shipping',1500),(60,'IT',1400),(70,'Public Relations',2700),(80,'Sales',2500),(90,'Executive',1700),(100,'Finance',1700),(110,'Accounting',1700),(120,'Treasury',1700),(130,'Corporate Tax',1700),(140,'Control And Credit',1700),(150,'Shareholder Services',1700),(160,'Benefits',1700),(170,'Payroll',1700);
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(25) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `job_id` varchar(10) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `commission_pct` int DEFAULT NULL,
  `manager_id` int DEFAULT NULL,
  `department_id` int DEFAULT NULL,
  PRIMARY KEY (`employee_id`),
  KEY `fk_deptno` (`department_id`),
  CONSTRAINT `fk_deptno` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (100,'Steven','King','SKING','515.123.4567','1987-06-17','AD_PRES',24000,NULL,NULL,20),(101,'Neena','Kochhar','NKOCHHAR','515.123.4568','1989-11-21','AD_VP',17000,NULL,100,20),(102,'Lex','De Haan','LDEHAAN','515.123.4569','1993-09-12','AD_VP',17000,NULL,100,30),(103,'Alexander','Hunold','AHUNOLD','590.423.4567','1990-09-30','IT_PROG',9000,NULL,102,60),(104,'Bruce','Ernst','BERNST','590.423.4568','1991-05-21','IT_PROG',6000,NULL,103,60),(105,'David','Austin','DAUSTIN','590.423.4569','1997-06-25','IT_PROG',4800,NULL,103,60),(106,'Valli','Pataballa','VPATABAL','590.423.4560','1998-02-05','IT_PROG',4800,NULL,103,40),(107,'Diana','Lorentz','DLORENTZ','590.423.5567','1999-02-09','IT_PROG',4200,NULL,103,40),(108,'Nancy','Greenberg','NGREENBE','515.124.4569','1994-08-17','FI_MGR',12000,NULL,101,100),(109,'Daniel','Faviet','DFAVIET','515.124.4169','1994-08-12','FI_ACCOUNT',9000,NULL,108,170),(110,'John','Chen','JCHEN','515.124.4269','1997-04-09','FI_ACCOUNT',8200,NULL,108,170),(111,'Ismael','Sciarra','ISCIARRA','515.124.4369','1997-02-01','FI_ACCOUNT',7700,NULL,108,160),(112,'Jose Manuel','Urman','JMURMAN','515.124.4469','1998-06-03','FI_ACCOUNT',7800,NULL,108,150),(113,'Luis','Popp','LPOPP','515.124.4567','1999-12-07','FI_ACCOUNT',6900,NULL,108,140),(114,'Den','Raphaely','DRAPHEAL','515.127.4561','1994-11-08','PU_MAN',11000,NULL,100,30),(115,'Alexander','Khoo','AKHOO','515.127.4562','1995-05-12','PU_CLERK',3100,NULL,114,80),(116,'Shelli','Baida','SBAIDA','515.127.4563','1997-12-13','PU_CLERK',2900,NULL,114,70),(117,'Sigal','Tobias','STOBIAS','515.127.4564','1997-09-10','PU_CLERK',2800,NULL,114,30),(118,'Guy','Himuro','GHIMURO','515.127.4565','1998-01-02','PU_CLERK',2600,NULL,114,60),(119,'Karen','Colmenares','KCOLMENA','515.127.4566','1999-04-08','PU_CLERK',2500,NULL,114,130),(120,'Matthew','Weiss','MWEISS','650.123.1234','1996-07-18','ST_MAN',8000,NULL,100,50),(121,'Adam','Fripp','AFRIPP','650.123.2234','1997-08-09','ST_MAN',8200,NULL,100,50),(122,'Payam','Kaufling','PKAUFLIN','650.123.3234','1995-05-01','ST_MAN',7900,NULL,100,40),(123,'Shanta','Vollman','SVOLLMAN','650.123.4234','1997-10-12','ST_MAN',6500,NULL,100,50),(124,'Kevin','Mourgos','KMOURGOS','650.123.5234','1999-11-12','ST_MAN',5800,NULL,100,80),(125,'Julia','Nayer','JNAYER','650.124.1214','1997-07-02','ST_CLERK',3200,NULL,120,50),(126,'Irene','Mikkilineni','IMIKKILI','650.124.1224','1998-11-12','ST_CLERK',2700,NULL,120,50),(127,'James','Landry','JLANDRY','650.124.1334','1999-01-02','ST_CLERK',2400,NULL,120,90),(128,'Steven','Markle','SMARKLE','650.124.1434','2000-03-04','ST_CLERK',2200,NULL,120,50),(129,'Laura','Bissot','LBISSOT','650.124.5234','1997-09-10','ST_CLERK',3300,NULL,121,50),(130,'Mozhe','Atkinson','MATKINSO','650.124.6234','1997-10-12','ST_CLERK',2800,NULL,121,110);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-24  1:01:23