-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 27, 2024 at 05:42 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `exim_device`
--

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `brand_id` int(11) NOT NULL,
  `brand_name` varchar(40) NOT NULL,
  `description` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `device_model` varchar(50) NOT NULL,
  `serial_number` varchar(50) NOT NULL,
  `mac_address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`brand_id`, `brand_name`, `description`, `created_at`, `updated_at`, `deleted_at`, `device_model`, `serial_number`, `mac_address`) VALUES
(1, 'acer', '', NULL, '2024-06-26 15:42:00', NULL, '', '', ''),
(2, 'dell', '', NULL, '2024-06-24 12:05:48', NULL, '', '', ''),
(3, 'de5', '5', NULL, NULL, '2024-06-24 13:20:55', '', '', ''),
(4, 'lenovo', 'Com brand', NULL, NULL, NULL, '', '', ''),
(5, 'asus', 'PC, Laptop', NULL, '2024-06-24 12:06:22', NULL, '', '', ''),
(6, 'predator', 'PC', '2024-06-24 00:00:00', NULL, NULL, '', '', ''),
(7, 'MacBook', 'laptop', NULL, NULL, NULL, 'SN1592D', 'SN95V5EFV48G4REG', '127SS'),
(8, 'hp', 'laptop', '2024-06-24 12:03:23', NULL, NULL, '', '', ''),
(9, 'asus', 'PC, Laptop', '2024-06-24 12:06:12', NULL, NULL, '', '', ''),
(10, 'asus', 'PC, Laptop', '2024-06-26 13:39:42', NULL, NULL, '', '', ''),
(11, 'asus', 'PC, Laptop', '2024-06-26 13:41:10', NULL, '2024-06-26 13:42:04', '', '', ''),
(12, 'asus', 'PC, Laptop', '2024-06-26 13:42:07', NULL, NULL, '', '', ''),
(13, 'asus', 'PC, Laptop', '2024-06-26 15:03:20', NULL, NULL, '', '', ''),
(14, 'ROG', 'ko', '2024-06-26 15:03:30', '2024-06-27 01:06:20', NULL, '', '', ''),
(15, 'asus', 'PC, Laptop', '2024-06-26 22:18:52', NULL, NULL, '', '', ''),
(16, 'asus', 'PC, Laptop', '2024-06-26 22:19:28', NULL, NULL, '', '', ''),
(17, 'predator', '5', '2024-06-27 00:47:18', '2024-06-27 01:04:41', '2024-06-27 01:06:04', '', '', ''),
(18, 'Korea', '00', '2024-06-27 01:06:22', '2024-06-27 01:09:54', '2024-06-27 01:10:04', '', '', ''),
(19, 'Korea', '00', '2024-06-27 01:10:01', NULL, NULL, '', '', ''),
(20, 'acer', 'a', NULL, NULL, '2024-07-02 08:47:56', 'SN1592D', 'SN95V5EFV48G4REG', '127SS');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL,
  `category_name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`category_id`, `category_name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Computer', 'Comunicate Technology', '2024-06-26 11:20:30', NULL, NULL),
(2, 'UPS', 'Comunicate Technology', '2024-06-26 11:33:03', '2024-06-26 13:26:08', NULL),
(3, 'Phone', 'Comunicate 123', '2024-06-26 11:33:29', '2024-06-26 11:50:07', '2024-06-26 11:50:22'),
(4, 'Adapter', 'Comunicate Technology', '2024-06-26 13:45:08', '2024-06-26 14:42:40', NULL),
(5, 'COM', '54', '2024-06-27 01:29:13', '2024-06-27 01:29:20', '2024-06-27 01:29:28');

-- --------------------------------------------------------

--
-- Table structure for table `companies`
--

CREATE TABLE `companies` (
  `company_id` int(11) NOT NULL DEFAULT 0,
  `company_name` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `companies`
--

INSERT INTO `companies` (`company_id`, `company_name`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'EXIM_LOGISTIC', 'New company ', NULL, '2024-06-24 23:42:27', NULL),
(2, 'EXIM_CO', '', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `id` bigint(20) UNSIGNED NOT NULL DEFAULT 0,
  `name_la` varchar(255) DEFAULT NULL,
  `name_en` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`id`, `name_la`, `name_en`, `created_at`, `updated_at`, `deleted_at`, `company_id`, `supervisor_id`) VALUES
(1, 'Board Management', 'Board Management', NULL, NULL, NULL, NULL, NULL),
(2, 'IT', 'IT', NULL, '2024-05-16 07:09:47', NULL, NULL, 8),
(3, 'Finance', 'Finance', NULL, '2024-05-16 07:11:00', NULL, NULL, 60),
(4, 'Customer Service', 'Customer Service', NULL, NULL, NULL, NULL, NULL),
(5, 'Automotive & Document', 'Automotive & Document', NULL, NULL, NULL, NULL, NULL),
(6, 'HR - Admin', 'HR - Admin', NULL, NULL, NULL, NULL, NULL),
(7, 'Operations', 'Operations', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `devices`
--

CREATE TABLE `devices` (
  `device_id` int(20) NOT NULL,
  `device_model` varchar(50) DEFAULT NULL,
  `serial_number` varchar(50) DEFAULT NULL,
  `mac_address` varchar(50) DEFAULT NULL,
  `device_remark` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `brand_id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `device_location_id` int(11) DEFAULT NULL,
  `used_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `devices`
--

INSERT INTO `devices` (`device_id`, `device_model`, `serial_number`, `mac_address`, `device_remark`, `created_at`, `updated_at`, `deleted_at`, `supplier_id`, `brand_id`, `category_id`, `status_id`, `user_id`, `device_location_id`, `used_by`) VALUES
(27, 'Acer001', 'AC123KL256', '123.456.85201', 'Laptop', '2024-07-27 21:18:15', NULL, NULL, 3, 1, 1, 4, 1, 1, 1),
(28, 'dell 002', 'DL123KL852GGX', '321.654.8520.1.2', 'WIFI', '2024-07-27 21:20:24', NULL, NULL, 1, 2, 4, 4, 1, 1, 1),
(29, 'lenovo 001', 'LN456LO45F', '963.123.584.1', 'WiFi', '2024-07-27 21:22:25', NULL, NULL, 1, 4, 4, 5, 2, 1, 6),
(30, 'hp 001', 'hp123lk4545', '123.85.123.54', '', '2024-07-27 21:42:52', NULL, NULL, 2, 8, 2, 4, 2, 2, 7),
(31, 'pre 002', 'PR456KP25589DKS3', '123.456.789.21.1', '', '2024-07-27 21:47:27', NULL, NULL, 3, 6, 1, 3, 2, 1, 24);

-- --------------------------------------------------------

--
-- Table structure for table `device_example`
--

CREATE TABLE `device_example` (
  `id` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `device_example`
--

INSERT INTO `device_example` (`id`, `brand_id`) VALUES
(2, 5),
(3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `device_locations`
--

CREATE TABLE `device_locations` (
  `device_location_id` int(11) NOT NULL,
  `device_location_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `device_locations`
--

INSERT INTO `device_locations` (`device_location_id`, `device_location_name`, `address`, `description`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Zone A', '55', 'Upstair Floor 2', '2024-06-27 01:33:21', '2024-06-27 02:01:15', NULL),
(2, 'Canteen', 'jkygukyuk', 'Upstair Floor 2', '2024-06-27 01:38:41', '2024-06-27 02:01:04', NULL),
(3, 'Restaurant', '', 'Upstair Floor 2', '2024-06-27 01:38:44', '2024-06-27 01:50:01', '2024-06-27 08:47:30'),
(4, 'Restaurant', '55', 'Upstair Floor 2', '2024-06-27 01:55:03', NULL, '2024-06-27 01:55:06');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_id` bigint(20) UNSIGNED NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `surname` varchar(255) DEFAULT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `department_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `position_id` int(20) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `emp_code` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `email_verified_at` timestamp NULL DEFAULT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`emp_id`, `name`, `surname`, `nickname`, `address`, `department_id`, `company_id`, `position_id`, `email`, `gender`, `emp_code`, `phone_number`, `email_verified_at`, `remember_token`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'LANLA', 'PHOMKHANXAY', 'LANLA', 'Laos', 3, 2, 15, '', 'F', 'AAEERRFF', '02095567822', NULL, NULL, NULL, NULL, NULL),
(3, 'PHONEMALA', 'DOUANGPHACHANPHENG', 'PHONEMALA', NULL, 7, 1, 9, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'BOUDDA', 'SYPHOMSAI', 'BOUDDA', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'SAYSANA', 'SAYALARTH', 'SAYSANA', NULL, 1, 1, 7, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'CHANTHAVISOUK', 'LOUANGLATH', 'CHANTHAVISOUK', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'SULISAN', 'PHIMVONGXAY', 'SULISAN', NULL, 5, 1, 22, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(8, 'VANSAVANG', 'THONGPASEUTH', 'VANSAVANG', NULL, 2, 1, 11, 'lang@exim.la', 'M', '', NULL, NULL, 'nmYiG2HtHlhVsNmB8Db2HlauULYbjStSnl3KQlFB18TS31MsYLEwhBFUJgEa', NULL, NULL, NULL),
(9, 'NITHSAKHONE', 'CHOUNTHASIM', 'NITHSAKHONE', NULL, 4, 1, 18, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(11, 'XAYSANA', 'PHAISANE', 'XAYSANA', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(12, 'PHONESAVATH', 'LASAPHANGTHONG', 'PHONESAVATH', NULL, 4, 1, 17, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(13, 'SOMPONG', 'DOUANGXAI', 'SOMPONG', NULL, 4, 1, 17, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(14, 'SITTHIDETH', 'SYHAVONG', 'SITTHIDETH', NULL, 3, 1, 15, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(15, 'THONGLAI', 'CHANTHAVONGSA', 'THONGLAI', NULL, 4, 1, 18, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(16, 'SOULINTHONE', 'LATTANAVICHIT', 'SOULINTHONE', NULL, 6, 1, 26, 'jimmie@exim.la', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(17, 'CHINOUH', 'XIONG', 'CHINOUH', NULL, 4, 1, 18, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(18, 'SOUTHAT', 'PHOMMASENG', 'SOUTHAT', NULL, 5, 1, 20, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(19, 'SOUDALATH', 'CHANTHASOTO', 'SOUDALATH', NULL, 4, 1, 17, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(20, 'SINTHANA', 'PHOMMALAY', 'SINTHANA', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(21, 'DALAVONE', 'LUANGLATH', 'DALAVONE', NULL, 5, 1, 22, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(22, 'OUPEAKHA', 'SOYDARA', 'OUPEAKHA', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(23, 'TONTARN', 'XAYALATH', 'TONTARN', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(24, 'ADO', 'ONDUANGDY', 'ADO', NULL, 4, 1, 17, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(25, 'PHOUTHONE', 'XAYABOUTSY', 'PHOUTHONE', NULL, 6, 1, 29, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(26, 'HATTHAPHONE', 'PHATHOUMPHONE', 'HATTHAPHONE', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(27, 'DAOAUNGKHARN', 'THIKEO', 'DAOAUNGKHARN', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(28, 'LINA', 'THONGPASEUTH', 'LINA', NULL, 3, 1, 15, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(29, 'SOMSY', 'LARTSAVONG', 'SOMSY', NULL, 6, 1, 32, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(30, 'RPISONE', 'VONGKHAMCHANH', 'RPISONE', NULL, 4, 1, 17, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(31, 'PERN', 'SIPHONGXAY', 'PERN', NULL, 2, 1, 36, 'itsupport@exim.la', 'M', '', NULL, NULL, NULL, NULL, '2024-05-16 08:39:10', NULL),
(32, 'ANOUSAK', 'PHILANGAM', 'ANOUSAK', NULL, 1, 1, 2, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(33, 'SOULIYA', 'SIPHOMXAY', 'SOULIYA', NULL, 7, 1, 24, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(34, 'KHAMTOM', 'DUANGPHUKDY', 'KHAMTOM', NULL, 4, 1, 17, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(35, 'SOUPHAVADY', 'BOUBPHAVONG', 'SOUPHAVADY', NULL, 5, 1, 20, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(36, 'PALIYA', 'PHENGKHAMSAY', 'PALIYA', NULL, 4, 1, 17, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(37, 'MEKSAVANH', 'LOMBOUNPHENG', 'MEKSAVANH', NULL, 5, 1, 20, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(38, 'KHAMPAN', 'SAIDUANGSONE', 'KHAMPAN', NULL, 5, 1, 22, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(40, 'SOUKSIYNAMBOUN', 'VONGSA', 'SOUKSIYNAMBOUN', NULL, 6, 1, 33, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(41, 'VILAVANH', 'INTHASOMBATH', 'VILAVANH', NULL, 4, 1, 17, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(42, 'PHETVILAY', 'MALAKHAM', 'PHETVILAY', NULL, 4, 1, 17, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(43, 'AMPHAVANH', 'THIRAKOUNE', 'AMPHAVANH', NULL, 3, 1, 15, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(45, 'SYSOUPHAN', 'XAYASOUK', 'SYSOUPHAN', NULL, 3, 1, 16, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(46, 'INTHILA', 'FONGSAVANH', 'INTHILA', NULL, 3, 1, 16, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(47, 'JONENY', 'VERNKHAM', 'JONENY', NULL, 6, 1, 32, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(48, 'Moukky', 'SOTHISAY', 'Moukky', NULL, 3, 1, 15, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(49, 'Vilayvone', 'SOUKSAKHONE', 'Vilayvone', NULL, 3, 1, 16, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(50, 'Phoupasert', 'XAYYASEANG', 'Phoupasert', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(51, 'Phet', 'SYSOMPHAN', 'Phet', NULL, 6, 1, 28, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(52, 'Latsame', 'KOUNSAVEANG', 'Latsame', NULL, 6, 1, 28, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(53, 'SOULIXAY', 'TAKOUNTHONG', 'SOULIXAY', NULL, 4, 1, 18, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(54, 'Heanly', 'PHANYAVONG', 'Heanly', NULL, 6, 1, 32, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(55, 'Phanmaly', 'LATSAVONG', 'Phanmaly', NULL, 6, 1, 34, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(56, 'Khamman', 'BOUNYAVONG', 'Khamman', NULL, 6, 1, 35, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(57, 'Pheang', 'KHAMPHET', 'Pheang', NULL, 6, 1, 34, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(58, 'BOUAKHAM', 'YOISAYKHAM', 'BOUAKHAM', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(59, 'OUNVONGSA', 'PHENGLASAK', 'OUNVONGSA', NULL, 7, 1, 25, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(60, 'Kaysone', 'SOULIYASAK', 'Kaysone', NULL, 1, 1, 3, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(61, 'NOLA', 'CHANTHALA', 'NOLA', NULL, 5, 1, 19, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(63, 'THONGDAM', 'SOUNDALA', 'THONGDAM', NULL, 6, 1, 31, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(64, 'VIDAPHONE', 'PHAISANE', 'VIDAPHONE', NULL, 3, 1, 13, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(65, 'XAYSANA', 'INTHICHACK', 'XAYSANA', NULL, 3, 1, 14, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(66, 'THANONGSIN', 'SAYYASENG', 'THANONGSIN', NULL, 1, 1, 5, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(67, 'SANGCHAN', 'SOMBOULEE', 'SANGCHAN', NULL, 7, 1, 25, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(68, 'VITHAYA', 'VONGKHAMSOUK', 'VITHAYA', NULL, 5, 1, 21, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(69, 'SENGSOULIYA', 'SIMONGKOUN', 'SENGSOULIYA', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(70, 'SADALATH', 'VONGSOMPHOU', 'SADALATH', NULL, 5, 1, 22, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(71, 'BOUNPHENG', 'NORASING', 'BOUNPHENG', NULL, 3, 1, 8, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(72, 'DALAPHONE', 'VONGXAY', 'DALAPHONE', NULL, 4, 1, 17, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(73, 'LADDAVANH', 'PHONSILAKONE', 'LADDAVANH', NULL, 6, 1, 27, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(74, 'SISOMPHET', 'CHANTHAVONG', 'SISOMPHET', NULL, 3, 1, 15, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(75, 'INPANE', 'PHOMMACHANH', 'INPANE', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(76, 'Xaysana', 'Phommavongsay', 'Xaysana', NULL, 1, 1, 4, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(77, 'SUPATTRA', 'INTANAM', 'SUPATTRA', NULL, 1, 1, 6, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(78, 'VONGPHIEN', 'PHILAVANH', 'VONGPHIEN', NULL, 6, 1, 28, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(79, 'BOUNMY', 'VONGSUKDA', 'BOUNMY', NULL, 4, 1, 12, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(80, 'BOUNCHAN', 'SIMMANIVONG', 'BOUNCHAN', NULL, 6, 1, 28, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(81, 'SOUCHINDA', 'INTHICHACK', 'SOUCHINDA', NULL, 5, 1, 10, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(82, 'CHANTHALA', 'KEODOUANGDY', 'CHANTHALA', NULL, 5, 1, 20, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(83, 'KHANTHAVIXAY', 'DALASENG', 'KHANTHAVIXAY', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(84, 'SOMPHAVANH', 'PHOMMALIN', 'SOMPHAVANH', NULL, 5, 1, 22, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(85, 'THIDALATH', 'SOUKSOMBOUN', 'THIDALATH', NULL, 4, 1, 18, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(86, 'ANAN', 'PADITH', 'ANAN', NULL, 6, 1, 32, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(87, 'KHAMLEK', 'DUANGMALYOUT', 'KHAMLEK', NULL, 5, 1, 20, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(88, 'SOMMAY', 'BOUALAVONG', 'SOMMAY', NULL, 7, 1, 25, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(89, 'Orlaya', 'PHENGSAVANH', 'Orlaya', NULL, 6, 1, 30, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(90, 'KHAMLA', 'NANTHALATH', 'KHAMLA', NULL, 5, 1, 22, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(92, 'King', 'PHEANGKHAMPHAT', 'King', NULL, 6, 1, 28, '', 'F', '', NULL, NULL, NULL, NULL, NULL, NULL),
(93, 'Khonesanit', 'XAYSOMPHAN', 'Khonesanit', NULL, 6, 1, 32, '', 'M', '', NULL, NULL, NULL, NULL, NULL, NULL),
(94, 'Phoutsady', 'Khamphoumy', 'pou', NULL, 2, 1, 27, 'phoutsadykhamphoumy@gmail.com', 'M', '', NULL, NULL, NULL, '2024-05-17 05:16:42', '2024-05-17 05:16:42', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `positions`
--

CREATE TABLE `positions` (
  `position_id` int(20) NOT NULL,
  `company_id` int(11) NOT NULL,
  `name_la` varchar(255) NOT NULL,
  `name_en` varchar(255) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `positions`
--

INSERT INTO `positions` (`position_id`, `company_id`, `name_la`, `name_en`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 1, 'Chairman', 'Chairman', NULL, NULL, NULL),
(2, 1, 'Managing Director', 'Managing Director', NULL, NULL, NULL),
(3, 1, 'Finance Director', 'Finance Director', NULL, NULL, NULL),
(4, 1, 'Corporate Development', 'Corporate Development', NULL, NULL, NULL),
(5, 1, 'Government Relations', 'Government Relations', NULL, NULL, NULL),
(6, 1, 'Business Development', 'Business Development', NULL, NULL, NULL),
(7, 1, 'General Manager', 'General Manager', NULL, NULL, NULL),
(8, 1, 'Finance Manager', 'Finance Manager', NULL, NULL, NULL),
(9, 1, 'Operations Manager', 'Operations Manager', NULL, NULL, NULL),
(10, 1, 'A&D Manager', 'A&D Manager', NULL, NULL, NULL),
(11, 1, 'IT Manager', 'IT Manager', NULL, NULL, NULL),
(12, 1, 'CS Manager', 'CS Manager', NULL, NULL, NULL),
(13, 1, 'Finance Supervisor', 'Finance Supervisor', NULL, NULL, NULL),
(14, 1, 'Finance Staff', 'Finance Staff', NULL, NULL, NULL),
(15, 1, 'Billing Staff', 'Billing Staff', NULL, NULL, NULL),
(16, 1, 'Accounting Staff', 'Accounting Staff', NULL, NULL, NULL),
(17, 1, 'Customer Service Advisor', 'Customer Service Advisor', NULL, NULL, NULL),
(18, 1, 'Customer Service senior', 'Customer Service senior', NULL, NULL, NULL),
(19, 1, 'Automotive Supervisor', 'Automotive Supervisor', NULL, NULL, NULL),
(20, 1, 'Automotive Staff', 'Automotive Staff', NULL, NULL, NULL),
(21, 1, 'Documentation Supervisor', 'Documentation Supervisor', NULL, NULL, NULL),
(22, 1, 'Document Staff', 'Document Staff', NULL, NULL, NULL),
(23, 1, 'Automotive Staff', 'Automotive Staff', NULL, NULL, NULL),
(24, 1, 'Operation Supervisor', 'Operation Supervisor', NULL, NULL, NULL),
(25, 1, 'Border Staff', 'Border Staff', NULL, NULL, NULL),
(26, 1, 'HR Supervisor', 'HR Supervisor', NULL, NULL, NULL),
(27, 1, 'Admin Supervisor', 'Admin Supervisor', NULL, NULL, NULL),
(28, 1, 'Maid', 'Maid', NULL, NULL, NULL),
(29, 1, 'chef', 'chef', NULL, NULL, NULL),
(30, 1, 'Receptionist - Admin', 'Receptionist - Admin', NULL, NULL, NULL),
(31, 1, 'Housekeeper', 'Housekeeper', NULL, NULL, NULL),
(32, 1, 'Driver Staff', 'Driver Staff', NULL, NULL, NULL),
(33, 1, 'Security guard', 'Security guard', NULL, NULL, NULL),
(34, 1, 'Kitchen Assistant', 'Kitchen Assistant', NULL, NULL, NULL),
(35, 1, 'Gardener', 'Gardener', NULL, NULL, NULL),
(36, 1, 'IT Support', 'IT Support', NULL, NULL, NULL),
(37, 1, 'Trainer System Assistant', 'Trainer System Assistant', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `status_id` int(11) NOT NULL,
  `status_name` varchar(50) NOT NULL,
  `remark` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`status_id`, `status_name`, `remark`, `created_at`, `updated_at`, `deleted_at`) VALUES
(3, 'paeng u', '', '2024-06-26 16:33:34', '2024-06-26 16:33:59', NULL),
(4, 'Varng', '', '2024-06-27 08:52:18', NULL, NULL),
(5, 'br varng', '', '2024-06-27 08:52:25', NULL, NULL),
(6, 'phey leo', '', '2024-06-27 08:56:43', NULL, NULL),
(7, 'Shouldn\'t Show', '', '2024-06-27 08:56:47', '2024-06-27 09:03:46', '2024-06-27 09:03:51');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `supplier_id` int(11) NOT NULL,
  `supplier_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `fax` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `other_detail` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`supplier_id`, `supplier_name`, `address`, `phone`, `fax`, `email`, `other_detail`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'Lenovo Corporation', 'DongDok', '020 99988875', '021 357945', 'Pepsi@email.la', 'Drinks Service', '2024-06-26 23:05:13', '2024-06-26 23:11:10', NULL),
(2, 'ACER CO', 'America', '020 95175323', '021 5685585', 'COKEKACOLA@MAIL.LA', 'Drink Service', '2024-06-27 01:08:31', '2024-06-27 01:08:46', NULL),
(3, 'Rog Corporation', 'Sibounhueang,Vientiane,Laos', '021 555159', '', '', '', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `last_login` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `name`, `password`, `last_login`, `deleted_at`, `created_at`, `updated_at`) VALUES
(1, 'pou', 'Pou', '$2b$12$ITJhj6582I3vcPQvNv.N7ug7/XvsFvWFIU9818CmbydXd2L02oVGC', NULL, NULL, '2024-07-10 04:14:11', '2024-07-10 04:14:11'),
(2, 'alexthedark', 'alex', '$2b$12$DFoKn2OWv6O0BwRclCHJBup/M6vkR7iVLxro2SyJMbtjiIvfcL.Ju', NULL, NULL, '2024-07-11 02:57:40', '2024-07-11 02:57:40'),
(3, 'a', 'alex', '$2b$12$vxfobl8Gq5bAzXxmJ13kzOQ7umGONR9VCqsgDHAWD.vOy92x61PUW', NULL, NULL, '2024-07-12 02:53:39', '2024-07-12 02:53:39'),
(4, 'a', 'a', '$2b$12$aJDjn873zzp/bebpJ/Is7O/QXNWgAGOZx9E3BX.sVcGHPhTC784Lu', NULL, NULL, '2024-07-12 04:35:53', '2024-07-12 04:35:53'),
(5, 'a', 'aa', '$2b$12$Jf6St2apZT5pjg2EzXUuYeNzJUFYSdOA8WhvsRxr3TR8GAkVd1WSC', NULL, NULL, '2024-07-12 04:36:10', '2024-07-12 04:36:10'),
(6, 'pou', 'Pou', '$2b$12$ppHqqdmMXz3ok4tMadJYlOd6zXSzkpX3E4wMhdgFTp/bGu58CP3m.', NULL, NULL, '2024-07-18 05:03:51', '2024-07-18 05:03:51');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brands`
--
ALTER TABLE `brands`
  ADD PRIMARY KEY (`brand_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`category_id`);

--
-- Indexes for table `devices`
--
ALTER TABLE `devices`
  ADD PRIMARY KEY (`device_id`);

--
-- Indexes for table `device_example`
--
ALTER TABLE `device_example`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `device_locations`
--
ALTER TABLE `device_locations`
  ADD PRIMARY KEY (`device_location_id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `positions`
--
ALTER TABLE `positions`
  ADD PRIMARY KEY (`position_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`status_id`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`supplier_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `brand_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `category_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `devices`
--
ALTER TABLE `devices`
  MODIFY `device_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `device_example`
--
ALTER TABLE `device_example`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `device_locations`
--
ALTER TABLE `device_locations`
  MODIFY `device_location_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `emp_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=95;

--
-- AUTO_INCREMENT for table `positions`
--
ALTER TABLE `positions`
  MODIFY `position_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `status_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `supplier_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
