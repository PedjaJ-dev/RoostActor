-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 26, 2025 at 04:50 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `roostactor`
--

-- --------------------------------------------------------

--
-- Table structure for table `angazovanjetima`
--

CREATE TABLE `angazovanjetima` (
  `IDK` int(11) NOT NULL,
  `BrojAngazovanja` int(11) DEFAULT NULL,
  `UkupnoVreme` int(11) DEFAULT NULL,
  `BrojSati` int(11) DEFAULT NULL,
  `DoprinosRazvoju` float DEFAULT NULL,
  `OdgovoranZaRezultat` float DEFAULT NULL,
  `KvalitetSaradnje` float DEFAULT NULL,
  `UticajNaUspeh` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `demografija`
--

CREATE TABLE `demografija` (
  `IDP` int(11) NOT NULL,
  `NazivP` varchar(100) DEFAULT NULL,
  `StarosnaGrupa` float NOT NULL,
  `Pol` varchar(10) NOT NULL,
  `BrojZemalja` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `korisnik`
--

CREATE TABLE `korisnik` (
  `IDK` int(11) NOT NULL,
  `Ime` varchar(50) DEFAULT NULL,
  `Prezime` varchar(50) DEFAULT NULL,
  `Uloga` varchar(50) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Telefon` varchar(20) DEFAULT NULL,
  `PoslednjaPrijava` datetime DEFAULT NULL,
  `Lozinka` varchar(255) DEFAULT NULL,
  `Status` varchar(20) DEFAULT NULL,
  `Datum_Prijave` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `korisnik`
--

INSERT INTO `korisnik` (`IDK`, `Ime`, `Prezime`, `Uloga`, `Email`, `Telefon`, `PoslednjaPrijava`, `Lozinka`, `Status`, `Datum_Prijave`) VALUES
(6, 'Marko', 'Markovici', 'Administrator', 'marko.markovic@example.com', '123-456', '2025-01-01 10:00:00', 'scrypt:32768:8:1$wEBRbvCTSV9ATPlD$0c89a059bff169a3c9f4eac608e5305576d8e1607a845cbdb47fa912bdc06e2267aa7920e09b514b1e2dec51ec2e30c8ca17cf826421885887b39d5546b1cfce', 'Aktivan', '2025-01-01 00:00:00'),
(7, 'Ana', 'Anic', 'Korisnik', 'ana.anic@example.com', '987-654', '2025-01-02 11:00:00', 'scrypt:32768:8:1$1nKXk3gYYFvmv9nv$14639e0c9f74d3a94e9b28f003df9ab29ed303ca24b4559c7f220829e8e29dfeb450db2bc72f76e9d876beb930089251e827f3954d1dd70cbc2106f16d9875d2', 'Aktivan', '2025-01-02 00:00:00'),
(10, 'Mika', 'Mikic', 'Korisnik', 'mika.mikic@example.com', '123456', NULL, 'scrypt:32768:8:1$hnMZIiZ8qReygrnA$215ee356b7289796c7c5847c323d6a6134571401441efe1580d5bb1c4f800c6ae1dffd443e5808235a487e69fbad7dc9a8536e3640acc96d7f6133a0373f41df', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `kritikenagrade`
--

CREATE TABLE `kritikenagrade` (
  `IDP` int(11) NOT NULL,
  `NazivP` varchar(100) DEFAULT NULL,
  `ProsecneOcene` float DEFAULT NULL,
  `OsvojeneNagrade` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `popularnostprojekta`
--

CREATE TABLE `popularnostprojekta` (
  `IDP` int(11) NOT NULL,
  `Gledanost` int(11) DEFAULT NULL,
  `Prihodi` decimal(15,2) DEFAULT NULL,
  `Ocena` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `popularnostprojekta`
--

INSERT INTO `popularnostprojekta` (`IDP`, `Gledanost`, `Prihodi`, `Ocena`) VALUES
(3, 50000, 150000.50, 4.5),
(4, 75000, 300000.00, 4.8);

-- --------------------------------------------------------

--
-- Table structure for table `produkcija`
--

CREATE TABLE `produkcija` (
  `IDP` int(11) NOT NULL,
  `NazivP` varchar(100) DEFAULT NULL,
  `Trajanje` time DEFAULT NULL,
  `Lokacije` text DEFAULT NULL,
  `Tim` varchar(100) DEFAULT NULL,
  `Budzet` decimal(15,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projekat`
--

CREATE TABLE `projekat` (
  `IDP` int(11) NOT NULL,
  `Naziv` varchar(100) DEFAULT NULL,
  `Tip` varchar(50) DEFAULT NULL,
  `Status` varchar(50) DEFAULT NULL,
  `Poceo` date DEFAULT NULL,
  `Zavrsio` date DEFAULT NULL,
  `Progres` int(11) DEFAULT NULL,
  `Slika` varchar(255) DEFAULT NULL,
  `Opis` text DEFAULT NULL,
  `Tim` varchar(100) DEFAULT NULL,
  `Raspored` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `projekat`
--

INSERT INTO `projekat` (`IDP`, `Naziv`, `Tip`, `Status`, `Poceo`, `Zavrsio`, `Progres`, `Slika`, `Opis`, `Tim`, `Raspored`) VALUES
(3, 'Projekt A', 'Serija', 'U toku', '2024-12-01', '0000-00-00', 50, 'slikaA.jpg', 'Opis projekta A', 'Tim A', 'Raspored A'),
(4, 'Ladna voda se kupa u bunar', 'Serija', 'Zavrsen', '2023-06-01', '2024-01-01', 100, 'slikaB.jpg', 'Opis projekta B', 'Tim B', 'Raspored B'),
(6, 'Mrtva baba po federi skace', 'Serija', 'U toku', '2025-01-22', '0000-00-00', 43, NULL, 'Opis C', 'Tim C', NULL),
(7, 'Celavi se sisaju', 'Film', 'Zavrsen', '2025-01-24', '2026-04-30', 35, NULL, 'OpisD', 'TimD', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `scena`
--

CREATE TABLE `scena` (
  `IDS` int(11) NOT NULL,
  `NazivS` varchar(100) DEFAULT NULL,
  `Datum` date DEFAULT NULL,
  `Lokacija` varchar(100) DEFAULT NULL,
  `Mapa` text DEFAULT NULL,
  `StatusS` varchar(50) DEFAULT NULL,
  `IDP` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `uloge`
--

CREATE TABLE `uloge` (
  `IDU` int(11) NOT NULL,
  `IDK` int(11) DEFAULT NULL,
  `Ime` varchar(50) DEFAULT NULL,
  `Prezime` varchar(50) DEFAULT NULL,
  `Uloga` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `angazovanjetima`
--
ALTER TABLE `angazovanjetima`
  ADD PRIMARY KEY (`IDK`);

--
-- Indexes for table `demografija`
--
ALTER TABLE `demografija`
  ADD PRIMARY KEY (`IDP`,`StarosnaGrupa`,`Pol`);

--
-- Indexes for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD PRIMARY KEY (`IDK`),
  ADD UNIQUE KEY `Email` (`Email`);

--
-- Indexes for table `kritikenagrade`
--
ALTER TABLE `kritikenagrade`
  ADD PRIMARY KEY (`IDP`);

--
-- Indexes for table `popularnostprojekta`
--
ALTER TABLE `popularnostprojekta`
  ADD PRIMARY KEY (`IDP`);

--
-- Indexes for table `produkcija`
--
ALTER TABLE `produkcija`
  ADD PRIMARY KEY (`IDP`);

--
-- Indexes for table `projekat`
--
ALTER TABLE `projekat`
  ADD PRIMARY KEY (`IDP`);

--
-- Indexes for table `scena`
--
ALTER TABLE `scena`
  ADD PRIMARY KEY (`IDS`),
  ADD KEY `IDP` (`IDP`);

--
-- Indexes for table `uloge`
--
ALTER TABLE `uloge`
  ADD PRIMARY KEY (`IDU`),
  ADD KEY `IDK` (`IDK`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `korisnik`
--
ALTER TABLE `korisnik`
  MODIFY `IDK` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `projekat`
--
ALTER TABLE `projekat`
  MODIFY `IDP` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `scena`
--
ALTER TABLE `scena`
  MODIFY `IDS` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `uloge`
--
ALTER TABLE `uloge`
  MODIFY `IDU` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `angazovanjetima`
--
ALTER TABLE `angazovanjetima`
  ADD CONSTRAINT `angazovanjetima_ibfk_1` FOREIGN KEY (`IDK`) REFERENCES `korisnik` (`IDK`) ON DELETE CASCADE;

--
-- Constraints for table `demografija`
--
ALTER TABLE `demografija`
  ADD CONSTRAINT `demografija_ibfk_1` FOREIGN KEY (`IDP`) REFERENCES `projekat` (`IDP`);

--
-- Constraints for table `kritikenagrade`
--
ALTER TABLE `kritikenagrade`
  ADD CONSTRAINT `kritikenagrade_ibfk_1` FOREIGN KEY (`IDP`) REFERENCES `projekat` (`IDP`);

--
-- Constraints for table `popularnostprojekta`
--
ALTER TABLE `popularnostprojekta`
  ADD CONSTRAINT `fk` FOREIGN KEY (`IDP`) REFERENCES `projekat` (`IDP`);

--
-- Constraints for table `produkcija`
--
ALTER TABLE `produkcija`
  ADD CONSTRAINT `produkcija_ibfk_1` FOREIGN KEY (`IDP`) REFERENCES `projekat` (`IDP`);

--
-- Constraints for table `scena`
--
ALTER TABLE `scena`
  ADD CONSTRAINT `scena_ibfk_1` FOREIGN KEY (`IDP`) REFERENCES `projekat` (`IDP`);

--
-- Constraints for table `uloge`
--
ALTER TABLE `uloge`
  ADD CONSTRAINT `uloge_ibfk_1` FOREIGN KEY (`IDK`) REFERENCES `korisnik` (`IDK`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
