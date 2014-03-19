-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.5.30 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             8.3.0.4694
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for proscrp
DROP DATABASE IF EXISTS `proscrp`;
CREATE DATABASE IF NOT EXISTS `proscrp` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `proscrp`;


-- Dumping structure for table proscrp.html_page
DROP TABLE IF EXISTS `html_page`;
CREATE TABLE IF NOT EXISTS `html_page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_url_id` int(11) DEFAULT NULL,
  `page_content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table proscrp.html_page: ~0 rows (approximately)
/*!40000 ALTER TABLE `html_page` DISABLE KEYS */;
/*!40000 ALTER TABLE `html_page` ENABLE KEYS */;


-- Dumping structure for table proscrp.keyword_relevant_pages
DROP TABLE IF EXISTS `keyword_relevant_pages`;
CREATE TABLE IF NOT EXISTS `keyword_relevant_pages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page1_index` int(11) DEFAULT NULL,
  `page2_index` int(11) DEFAULT NULL,
  `keyword` varchar(255) DEFAULT NULL,
  `matching_score` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table proscrp.keyword_relevant_pages: ~0 rows (approximately)
/*!40000 ALTER TABLE `keyword_relevant_pages` DISABLE KEYS */;
/*!40000 ALTER TABLE `keyword_relevant_pages` ENABLE KEYS */;


-- Dumping structure for table proscrp.page_urls
DROP TABLE IF EXISTS `page_urls`;
CREATE TABLE IF NOT EXISTS `page_urls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_link` varchar(512) DEFAULT NULL,
  `fetching_done` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table proscrp.page_urls: ~0 rows (approximately)
/*!40000 ALTER TABLE `page_urls` DISABLE KEYS */;
/*!40000 ALTER TABLE `page_urls` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
