SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


CREATE DATABASE IF NOT EXISTS `spm_database` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_database`;

-- --------------------------------------------------------

--
-- Table structure for table `Administrator`
--

DROP TABLE IF EXISTS `administrator`;
CREATE TABLE `administrator` (
    `user_id` INT(11) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Administrator`
--

INSERT INTO `administrator` (`user_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- Table structure for table `Trainers`
--

DROP TABLE IF EXISTS `trainers`;
CREATE TABLE `trainers` (
    `user_id` INT(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Trainers`
--

INSERT INTO `trainers` (`user_id`) VALUES
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11);

-- --------------------------------------------------------

--
-- Table structure for table `Learners`
--

DROP TABLE IF EXISTS `learners`;
CREATE TABLE `learners` (
    `user_id` INT(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Learners`
--

INSERT INTO `learners` (`user_id`) VALUES
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19),
(20),
(21),
(22),
(23),
(24),
(25),
(26),
(27),
(28),
(29),
(30),
(31)
;

-- --------------------------------------------------------

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `user`;
CREATE table IF NOT EXISTS `user`(
    `user_id` INT(11) NOT NULL,
    `user_name` varchar(50) NOT NULL,
    `name` varchar(50) NOT NULL,
    `designation` varchar(50) NOT NULL,
    `department` varchar(50) NOT NULL,
    `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `User`
--

INSERT INTO `user` (`user_id`, `user_name`, `name`, `designation`, `department`, `role`) VALUES
-- Adminstrator user
(1, 'uname1', 'Claudia', 'Claudia', 'HR Department', 'Administrator'),
-- Trainer users (10)
(2, 'uname2', 'Ann', 'Ann', 'Tech Department', 'Trainers'),
(3, 'uname3', 'Ben', 'Ben', 'Tech department', 'Trainers'),
(4, 'uname4', 'Cindy', 'Cindy', 'Tech Department', 'Trainers'),
(5, 'uname5', 'Dane', 'Dane', 'Tech department', 'Trainers'),
(6, 'uname6', 'Eskimo', 'Eskimo', 'Tech Department', 'Trainers'),
(7, 'uname7', 'Fun', 'Fun', 'Eng department', 'Trainers'),
(8, 'uname8', 'Gin', 'Gin', 'Eng Department', 'Trainers'),
(9, 'uname9', 'Henry', 'Henry', 'Eng department', 'Trainers'),
(10, 'uname10', 'Ipman', 'Ipman', 'Eng Department', 'Trainers'),
(11, 'uname11', 'Joker', 'Joker', 'Eng department', 'Trainers'),
-- Learner users (20)
(12, 'uname12', 'Amy', 'Amy', 'Engineer', 'Learners'),
(13, 'uname13', 'Betty', 'Betty', 'Engineer', 'Learners'),
(14, 'uname14', 'Chad', 'Chad', 'Engineer', 'Learners'),
(15, 'uname15', 'Daniel', 'Daniel', 'Engineer', 'Learners'),
(16, 'uname16', 'Ethan', 'Ethan', 'Engineer', 'Learners'),
(17, 'uname17', 'Faris', 'Faris', 'Engineer', 'Learners'),
(18, 'uname18', 'Gaby', 'Gaby', 'Engineer', 'Learners'),
(19, 'uname19', 'Haziq', 'Haziq', 'Engineer', 'Learners'),
(20, 'uname20', 'Immanuel', 'Immanuel', 'Engineer', 'Learners'),
(21, 'uname21', 'Jessica', 'Jessica', 'Engineer', 'Learners'),
(22, 'uname22', 'Katy', 'Katy', 'Engineer', 'Learners'),
(23, 'uname23', 'Lenard', 'Lenard', 'Engineer', 'Learners'),
(24, 'uname24', 'Mady', 'Mady', 'Engineer', 'Learners'),
(25, 'uname25', 'Nat', 'Nat', 'Engineer', 'Learners'),
(26, 'uname26', 'Oscar', 'Oscar', 'Engineer', 'Learners'),
(27, 'uname27', 'Perry', 'Perry', 'Engineer', 'Learners'),
(28, 'uname28', 'Queen', 'Queen', 'Engineer', 'Learners'),
(29, 'uname29', 'Ray', 'Ray', 'Engineer', 'Learners'),
(30, 'uname30', 'Shar', 'Shar', 'Engineer', 'Learners'),
(31, 'uname31', 'Tun', 'Tun', 'Engineer', 'Learners');

-- --------------------------------------------------------

--
-- Table structure for table `Course`
--

DROP TABLE IF EXISTS `course`;
CREATE table IF NOT EXISTS `course`(
    `course_id` INT(11) NOT NULL,
    `course_name` VARCHAR(50) NOT NULL,
    `archive_date` DATE NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Course`
--

INSERT INTO `course` (`course_id`, `course_name`) VALUES
(1, 'IS111 Programming'),
(2, 'IS212 SPM'),
(3, 'CS440 Cybersec'),
(4, 'E101 Engineering'),
(5, 'E202 Printing Solutions');

-- --------------------------------------------------------

--
-- Table structure for table `Prerequisites`
--

DROP TABLE IF EXISTS `prerequisites`;
CREATE table IF NOT EXISTS `prerequisites`(
    `prereq_id` INT(11) NOT NULL,
    `course_id` INT(11) NOT NULL,
    `prereq_course_id` INT(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'Prerequisites'
--

INSERT INTO `prerequisites` (`prereq_id`, `course_id`, `prereq_course_id`) VALUES
(1, 2, 1),
(2, 3, 1),
(3, 5, 4);

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE table IF NOT EXISTS `class`(
    `class_id` INT(11) NOT NULL,
    `course_id` INT(11) NOT NULL,
    `trainer_id` INT(11) NOT NULL,
    `class_name` VARCHAR(50) NOT NULL,
    `capacity` INT(11) NOT NULL,
    `start_DateTime` DATETIME NOT NULL,
    `end_DateTime` DATETIME NOT NULL,
    `start_enrollment` DATETIME NOT NULL,
    `end_enrollment` DATETIME NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'class'
--

INSERT INTO `class` (`class_id`, `course_id`, `trainer_id`, `class_name`, `capacity`, `start_DateTime`, `end_DateTime`, `start_enrollment`, `end_enrollment`) VALUES
(1, 1, 2, 'class 1', 20, '2021-08-17 12:00:00','2021-11-23 15:15:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(2, 1, 3, 'class 2', 20, '2021-08-17 08:15:00','2021-11-23 11:30:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(3, 2, 4, 'class 1', 20, '2021-10-17 08:15:00','2021-11-23 11:30:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(4, 2, 5, 'class 2', 20, '2021-10-17 12:00:00','2021-11-23 15:15:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(5, 3, 6, 'class 1', 15, '2021-10-17 08:15:00','2021-11-23 11:30:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(6, 3, 7, 'class 2', 15, '2021-10-17 15:30:00','2021-11-23 18:45:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(7, 4, 8, 'class 1', 20, '2021-10-17 12:00:00','2021-11-23 15:15:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(8, 4, 9, 'class 2', 20, '2021-10-17 15:30:00','2021-11-23 18:45:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(9, 5, 10, 'class 1', 10, '2021-10-17 08:15:00','2021-11-23 11:30:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
(10, 5, 11, 'class 2', 10, '2021-10-17 15:30:00','2021-11-23 18:45:00','2021-07-10 00:00:00','2021-09-15 00:00:00')
;

-- --------------------------------------------------------

--
-- Table structure for table `chapter`
--

DROP TABLE IF EXISTS `chapter`;
CREATE TABLE IF NOT EXISTS `chapter`(
    `chapter_id` INT(11) NOT NULL,
    `class_id` INT(11) NOT NULL,
    `chapter_name` VARCHAR(50) NOT NULL,
    `order` INT(11) NOT NULL,
    `chapter_materials` VARCHAR(50) NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'chapter'
--

INSERT INTO `chapter` (`chapter_id`, `class_id`, `chapter_name`, `order`) VALUES
(1, 1, 'chapter 1', 1),
(2, 1, 'chapter 2', 2),
(3, 1, 'chapter 3', 3),
(4, 2, 'chapter 1', 1),
(5, 2, 'chapter 2', 2),
(6, 2, 'chapter 3', 3),
(7, 3, 'chapter 1', 1),
(8, 3, 'chapter 2', 2),
(9, 3, 'chapter 3', 3),
(10, 4, 'chapter 1', 1),
(11, 4, 'chapter 2', 2),
(12, 4, 'chapter 3', 3),
(13, 5, 'chapter 1', 1),
(14, 5, 'chapter 2', 2),
(15, 5, 'chapter 3', 3),
(16, 6, 'chapter 1', 1),
(17, 6, 'chapter 2', 2),
(18, 6, 'chapter 3', 3),
(19, 7, 'chapter 1', 1),
(20, 7, 'chapter 2', 2),
(21, 7, 'chapter 3', 3),
(22, 8, 'chapter 1', 1),
(23, 8, 'chapter 2', 2),
(24, 8, 'chapter 3', 3),
(25, 9, 'chapter 1', 1),
(26, 9, 'chapter 2', 2),
(27, 9, 'chapter 3', 3),
(28, 10, 'chapter 1', 1),
(29, 10, 'chapter 2', 2),
(30, 10, 'chapter 3', 3);

-- --------------------------------------------------------

--
-- Table structure for table `course progression`
--

DROP TABLE IF EXISTS `course_progression`;
CREATE table `course_progression`(
    `cc_id` INT(11) NOT NULL,
    `user_id` INT(11) NOT NULL,
    `course_id` INT(11) NOT NULL,
    `class_id` INT(11) NOT NULL,
    `chapter_id` INT(11) NOT NULL,
    `status` VARCHAR(50) NOT NULL,
    `completion_date` DATE NULL,
    `score` INT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'course progression'
--

INSERT INTO `course_progression` (`cc_id`, `user_id`, `course_id`, `class_id`, `chapter_id`, `status`) VALUES
(1, 12, 1, 1, 2, 'ongoing'),
(2, 13, 1, 1, 2, 'ongoing'),
(3, 14, 1, 2, 5, 'ongoing'),
(4, 15, 1, 2, 5, 'ongoing'),
(5, 16, 2, 3, 8, 'ongoing'),
(6, 17, 2, 3, 8, 'ongoing'),
(7, 18, 2, 4, 11, 'ongoing'),
(8, 19, 2, 4, 11, 'ongoing'),
(9, 20, 3, 5, 14, 'ongoing'),
(10, 21, 3, 5, 14, 'ongoing'),
(11, 22, 3, 6, 17, 'ongoing'),
(12, 23, 3, 6, 17, 'ongoing'),
(13, 24, 4, 7, 20, 'ongoing'),
(14, 25, 4, 7, 20, 'ongoing'),
(15, 26, 4, 8, 23, 'ongoing'),
(16, 27, 4, 8, 23, 'ongoing'),
(17, 28, 5, 9, 26, 'ongoing'),
(18, 29, 5, 9, 26, 'ongoing'),
(19, 30, 5, 10, 29, 'ongoing'),
(20, 31, 5, 10, 29, 'ongoing');

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE table `quiz`(
    `quiz_id` INT(11) NOT NULL,
    `chapter_id` INT(11) NOT NULL,
    `duration` INT(11) NOT NULL,
    `graded` BOOLEAN NOT NULL,
    `passing_mark` INT(11)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'quiz'
--

INSERT INTO `quiz` (`quiz_id`, `chapter_id`, `duration`, `graded`, `passing_mark`) VALUES
(1, 1, 10, 0, 50),
(2, 2, 20, 0, 50),
(3, 3, 30, 1, 50),
(4, 4, 10, 0, 50),
(5, 5, 20, 0, 50),
(6, 6, 30, 1, 50),
(7, 7, 10, 0, 50),
(8, 8, 20, 0, 50),
(9, 9, 30, 1, 50),
(10, 10, 10, 0, 50),
(11, 11, 20, 0, 50),
(12, 12, 30, 1, 50),
(13, 13, 10, 0, 50),
(14, 14, 20, 0, 50),
(15, 15, 30, 1, 50),
(16, 16, 10, 0, 50),
(17, 17, 20, 0, 50),
(18, 18, 30, 1, 50),
(19, 19, 10, 0, 50),
(20, 20, 20, 0, 50),
(21, 21, 30, 1, 50),
(22, 22, 10, 0, 50),
(23, 23, 20, 0, 50),
(24, 24, 30, 1, 50),
(25, 25, 10, 0, 50),
(26, 26, 20, 0, 50),
(27, 27, 30, 1, 50),
(28, 28, 10, 0, 50),
(29, 29, 20, 0, 50),
(30, 30, 30, 1, 50);

-- --------------------------------------------------------

--
-- Table structure for table `question_tf`
--

DROP TABLE IF EXISTS `question_tf`;
CREATE TABLE `question_tf` (
    `question_tf_id` INT(11) NOT NULL,
    `corrected_value` BOOLEAN NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `question_tf`
--

INSERT INTO `question_tf` (`question_tf_id`, `corrected_value`) VALUES
(1, 1),
(2, 0),
(3, 0),
(4, 0),
(7, 0),
(8, 1),
(9, 1),
(10, 1),
(13, 1),
(14, 0),
(15, 0),
(16, 1),
(19, 0),
(20, 1),
(21, 0),
(22, 1),
(25, 0),
(26, 1),
(27, 1),
(28, 1),
(31, 0),
(32, 0),
(33, 0),
(34, 1),
(37, 1),
(38, 0),
(39, 1),
(40, 0),
(42, 1),
(43, 0),
(44, 1),
(45, 1),
(48, 1),
(49, 0),
(50, 0),
(51, 0),
(54, 1),
(55, 1),
(56, 1),
(57, 0),
(58, 1)
;

-- --------------------------------------------------------

--
-- Table structure for table `question_mcq`
--

DROP TABLE IF EXISTS `question_mcq`;
CREATE TABLE `question_mcq` (
    `question_mcq_id` INT(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `question_mcq`
--

INSERT INTO `question_mcq` (`question_mcq_id`) VALUES
(5),
(6),
(11),
(12),
(17),
(18),
(23),
(24),
(29),
(30),
(35),
(36),
(41),
(42),
(47),
(48),
(53),
(54),
(59),
(60)
;

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
CREATE table `question`(
    `question_id` INT(11) NOT NULL,
    `quiz_id` INT(11) NOT NULL,
    `question` VARCHAR(250) NOT NULL,
    `marks` INT(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'question'
--

INSERT INTO `question` (`question_id`, `quiz_id`, `question`, `marks`) VALUES
(1, 1, 'Testing tf', 1),
(2, 1, 'testing tf', 1),
(3, 2, 'Testing tf', 1),
(4, 2, 'testing tf', 1),
(5, 3, 'Testing mcq', 2),
(6, 3, 'testing mcq', 2),
(7, 4, 'Testing tf', 1),
(8, 4, 'testing tf', 1),
(9, 5, 'Testing tf', 1),
(10, 5, 'testing tf', 1),
(11, 6, 'Testing mcq', 2),
(12, 6, 'testing mcq', 2),
(13, 7, 'Testing tf', 1),
(14, 7, 'testing tf', 1),
(15, 8, 'Testing tf', 1),
(16, 8, 'testing tf', 1),
(17, 9, 'Testing mcq', 2),
(18, 9, 'testing mcq', 2),
(19, 10, 'Testing tf', 1),
(20, 10, 'testing tf', 1),
(21, 11, 'Testing tf', 1),
(22, 11, 'testing tf', 1),
(23, 12, 'Testing mcq', 2),
(24, 12, 'testing mcq', 2),
(25, 13, 'Testing tf', 1),
(26, 13, 'Testing tf', 1),
(27, 14, 'testing tf', 1),
(28, 14, 'Testing tf', 1),
(29, 15, 'testing mcq', 2),
(30, 15, 'Testing mcq', 2),
(31, 16, 'testing tf', 1),
(32, 16, 'Testing tf', 1),
(33, 17, 'testing tf', 1),
(34, 17, 'Testing tf', 1),
(35, 18, 'testing mcq', 2),
(36, 18, 'Testing mcq', 2),
(37, 19, 'testing tf', 1),
(38, 19, 'Testing tf', 1),
(39, 20, 'testing tf', 1),
(40, 20, 'Testing tf', 1),
(41, 21, 'testing mcq', 2),
(42, 21, 'Testing mcq', 2),
(43, 22, 'testing tf', 1),
(44, 22, 'Testing tf', 1),
(45, 23, 'testing tf', 1),
(46, 23, 'Testing tf', 1),
(47, 24, 'testing mcq', 2),
(48, 24, 'Testing mcq', 2),
(49, 25, 'testing tf', 1),
(50, 25, 'Testing tf', 1),
(51, 26, 'testing tf', 1),
(52, 26, 'Testing tf', 1),
(53, 27, 'testing mcq', 2),
(54, 27, 'Testing mcq', 2),
(55, 28, 'testing tf', 1),
(56, 28, 'Testing tf', 1),
(57, 29, 'testing tf', 1),
(58, 29, 'Testing tf', 1),
(59, 30, 'testing mcq', 2),
(60, 30, 'Testing mcq', 2);


-- --------------------------------------------------------

--
-- Table structure for table `options`
--

DROP TABLE IF EXISTS `options`;
CREATE TABLE `options` (
    `options_id` INT(11) NOT NULL,
    `question_mcq_id` INT(11) NOT NULL,
    `value` VARCHAR(50) NOT NULL,
    `corrected_value` BOOLEAN NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `question_mcq`
--

INSERT INTO `options` (`options_id`, `question_mcq_id`, `value`, `corrected_value`) VALUES

(1, 5, 'A', 0),
(2, 5, 'B', 0),
(3, 5, 'C', 1),
(4, 5, 'D', 0),
(5, 6, 'A', 0),
(6, 6, 'B', 0),
(7, 6, 'C', 1),
(8, 6, 'D', 0),
(9, 11, 'A', 0),
(10, 11, 'B', 1),
(11, 11, 'C', 0),
(12, 11, 'D', 0),
(13, 12, 'A', 0),
(14, 12, 'B', 0),
(15, 12, 'C', 0),
(16, 12, 'D', 1),
(17, 17, 'A', 1),
(18, 17, 'B', 0),
(19, 17, 'C', 0),
(20, 17, 'D', 0),
(21, 18, 'A', 0),
(22, 18, 'B', 0),
(23, 18, 'C', 1),
(24, 18, 'D', 0),
(25, 23, 'A', 0),
(26, 23, 'B', 0),
(27, 23, 'C', 1),
(28, 23, 'D', 0),
(29, 24, 'A', 0),
(30, 24, 'B', 1),
(31, 24, 'C', 0),
(32, 24, 'D', 0),
(33, 29, 'A', 0),
(34, 29, 'B', 0),
(35, 29, 'C', 0),
(36, 29, 'D', 1),
(37, 30, 'A', 0),
(38, 30, 'B', 0),
(39, 30, 'C', 0),
(40, 30, 'D', 1),
(41, 35, 'A', 1),
(42, 35, 'B', 0),
(43, 35, 'C', 0),
(44, 35, 'D', 0),
(45, 36, 'A', 1),
(46, 36, 'B', 0),
(47, 36, 'C', 0),
(48, 36, 'D', 0),
(49, 41, 'A', 0),
(50, 41, 'B', 0),
(51, 41, 'C', 1),
(52, 41, 'D', 0),
(53, 42, 'A', 0),
(54, 42, 'B', 0),
(55, 42, 'C', 1),
(56, 42, 'D', 0),
(57, 47, 'A', 1),
(58, 47, 'B', 0),
(59, 47, 'C', 0),
(60, 47, 'D', 0),
(61, 48, 'A', 0),
(62, 48, 'B', 1),
(63, 48, 'C', 0),
(64, 48, 'D', 0),
(65, 53, 'A', 0),
(66, 53, 'B', 1),
(67, 53, 'C', 0),
(68, 53, 'D', 0),
(69, 54, 'A', 0),
(70, 54, 'B', 0),
(71, 54, 'C', 1),
(72, 54, 'D', 0),
(73, 59, 'A', 0),
(74, 59, 'B', 1),
(75, 59, 'C', 0),
(76, 59, 'D', 0),
(77, 60, 'A', 0),
(78, 60, 'B', 0),
(79, 60, 'C', 0),
(80, 60, 'D', 1)
;
--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `learners`
--
ALTER TABLE `learners`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `trainers`
--
ALTER TABLE `trainers`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `prerequisites`
--
ALTER TABLE `prerequisites`
  ADD PRIMARY KEY (`prereq_id`);

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`class_id`);

--
-- Indexes for table `chapter`
--
ALTER TABLE `chapter`
  ADD PRIMARY KEY (`chapter_id`);

--
-- Indexes for table `course_progression`
--
ALTER TABLE `course_progression`
  ADD PRIMARY KEY (`cc_id`);

--
-- Indexes for table `quiz`
--
ALTER TABLE `quiz`
  ADD PRIMARY KEY (`quiz_id`);

--
-- Indexes for table `question_tf`
--
ALTER TABLE `question_tf`
  ADD PRIMARY KEY (`question_tf_id`);

--
-- Indexes for table `question_mcq`
--
ALTER TABLE `question_mcq`
  ADD PRIMARY KEY (`question_mcq_id`);

--
-- Indexes for table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`question_id`);

--
-- Indexes for table `options`
--
ALTER TABLE `options`
  ADD PRIMARY KEY (`options_id`);


--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `prerequisites`
--
ALTER TABLE `prerequisites`
  MODIFY `prereq_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `chapter`
--
ALTER TABLE `chapter`
  MODIFY `chapter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `course_progression`
--
ALTER TABLE `course_progression`
  MODIFY `cc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `quiz`
  MODIFY `quiz_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `options`
--
ALTER TABLE `options`
  MODIFY `options_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;


--
-- Constraints for dumped tables
--

--
-- Constraints for table `administrator`
--
ALTER TABLE `administrator`
  ADD CONSTRAINT `administrator_fk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `learners`
--
ALTER TABLE `learners`
  ADD CONSTRAINT `learners_fk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `trainers`
--
ALTER TABLE `trainers`
  ADD CONSTRAINT `trainers_fk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `Prerequisites`
--
ALTER TABLE `prerequisites`
  ADD CONSTRAINT `prerequisites_fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `prerequisites_fk_2` FOREIGN KEY (`prereq_course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `class`
--
ALTER TABLE `class`
  ADD CONSTRAINT `class_fk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `class_fk_2` FOREIGN KEY (`trainer_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `chapter`
--
ALTER TABLE `chapter`
  ADD CONSTRAINT `chapter_fk_1` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`);

--
-- Constraints for table `course_progression`
--
ALTER TABLE `course_progression`
  ADD CONSTRAINT `course_progression_fk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `course_progression_fk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`),
  ADD CONSTRAINT `course_progression_fk_3` FOREIGN KEY (`class_id`) REFERENCES `class` (`class_id`),
  ADD CONSTRAINT `course_progression_fk_4` FOREIGN KEY (`chapter_id`) REFERENCES `chapter` (`chapter_id`);

--
-- Constraints for table `quiz`
--
ALTER TABLE `quiz`
  ADD CONSTRAINT `quiz_fk_1` FOREIGN KEY (`chapter_id`) REFERENCES `chapter` (`chapter_id`);

--
-- Constraints for table `question_tf`
--
ALTER TABLE `question_tf`
  ADD CONSTRAINT `question_tf_fk_1` FOREIGN KEY (`question_tf_id`) REFERENCES `question` (`question_id`);

--
-- Constraints for table `question_mcq`
--
ALTER TABLE `question_mcq`
  ADD CONSTRAINT `question_mcq_fk_1` FOREIGN KEY (`question_mcq_id`) REFERENCES `question` (`question_id`);

--
-- Constraints for table `options`
--
ALTER TABLE `options`
  ADD CONSTRAINT `options_fk_1` FOREIGN KEY (`question_mcq_id`) REFERENCES `question` (`question_id`);

--
-- Constraints for table `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_fk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`);
