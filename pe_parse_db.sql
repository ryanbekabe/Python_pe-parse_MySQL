-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 17, 2020 at 12:02 AM
-- Server version: 5.7.24
-- PHP Version: 7.2.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `pe_parse_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `tbdumplinux`
--

CREATE TABLE `tbdumplinux` (
  `no` int(11) NOT NULL,
  `md5` varchar(50) NOT NULL,
  `dump_string` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tbdumpwindows`
--

CREATE TABLE `tbdumpwindows` (
  `no` int(11) NOT NULL,
  `md5` varchar(50) NOT NULL,
  `dump_string` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbdumplinux`
--
ALTER TABLE `tbdumplinux`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `tbdumpwindows`
--
ALTER TABLE `tbdumpwindows`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbdumplinux`
--
ALTER TABLE `tbdumplinux`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tbdumpwindows`
--
ALTER TABLE `tbdumpwindows`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;
