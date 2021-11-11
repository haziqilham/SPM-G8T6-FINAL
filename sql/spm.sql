SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


CREATE DATABASE IF NOT EXISTS `spm_database` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_database`;

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
(1, 'uname1', 'Claudia', 'HR Manager', 'HR Department', 'Administrator'),
-- Trainer users (10)
(2, 'uname2', 'Ann', 'Senior SWE', 'Tech Department', 'Trainers'),
(3, 'uname3', 'Ben', 'Senior SWE', 'Tech department', 'Trainers'),
(4, 'uname4', 'Cindy', 'Senior SWE', 'Tech Department', 'Trainers'),
(5, 'uname5', 'Dane', 'Senior SWE', 'Tech department', 'Trainers'),
(6, 'uname6', 'Eskimo', 'Senior SWE', 'Tech Department', 'Trainers'),
(7, 'uname7', 'Fun', 'Senior Engineer', 'Eng department', 'Trainers'),
(8, 'uname8', 'Gin', 'Senior Engineer', 'Eng Department', 'Trainers'),
(9, 'uname9', 'Henry', 'Senior Engineer', 'Eng department', 'Trainers'),
(10, 'uname10', 'Ipman', 'Senior Engineer', 'Eng Department', 'Trainers'),
(11, 'uname11', 'Joker', 'Senior Engineer', 'Eng department', 'Trainers'),
-- Learner users (20)
(12, 'uname12', 'Amy', 'Junior Engineer', 'Eng department', 'Learners'),
(13, 'uname13', 'Betty', 'Junior Engineer', 'Eng department', 'Learners'),
(14, 'uname14', 'Chad', 'Junior Engineer', 'Eng department', 'Learners'),
(15, 'uname15', 'Daniel', 'Junior Engineer', 'Eng department', 'Learners'),
(16, 'uname16', 'Ethan', 'Junior Engineer', 'Eng department', 'Learners'),
(17, 'uname17', 'Faris', 'Junior Engineer', 'Eng department', 'Learners'),
(18, 'uname18', 'Gaby', 'Junior Engineer', 'Eng department', 'Learners'),
(19, 'uname19', 'Haziq', 'Junior Engineer', 'Eng department', 'Learners'),
(20, 'uname20', 'Immanuel', 'Junior Engineer', 'Eng department', 'Learners'),
(21, 'uname21', 'Jessica', 'Junior Engineer', 'Eng department', 'Learners'),
(22, 'uname22', 'Katy', 'Junior Engineer', 'Eng department', 'Learners'),
(23, 'uname23', 'Lenard', 'Junior Engineer', 'Eng department', 'Learners'),
(24, 'uname24', 'Mady', 'Junior Engineer', 'Eng department', 'Learners'),
(25, 'uname25', 'Nat', 'Junior Engineer', 'Eng department', 'Learners'),
(26, 'uname26', 'Oscar', 'Junior Engineer', 'Eng department', 'Learners'),
(27, 'uname27', 'Perry', 'Junior Engineer', 'Eng department', 'Learners'),
(28, 'uname28', 'Queen', 'Junior Engineer', 'Eng department', 'Learners'),
(29, 'uname29', 'Ray', 'Junior Engineer', 'Eng department', 'Learners'),
(30, 'uname30', 'Shar', 'Junior Engineer', 'Eng department', 'Learners'),
(31, 'uname31', 'Tun', 'Junior Engineer', 'Eng department', 'Learners');

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
-- Table structure for table `Course`
--

DROP TABLE IF EXISTS `course`;
CREATE table IF NOT EXISTS `course`(
    `course_id` INT(11) NOT NULL,
    `course_name` VARCHAR(50) NOT NULL,
    `archive_date` DATETIME NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Course`
--

INSERT INTO `course` (`course_id`, `course_name`, `archive_date`) VALUES
(1, 'E111 Intro to Fujifilm Printers', NULL),
(2, 'E112 Intro to FujiXerox Printers', NULL),
(3, 'E113 Intro to Brother Printers', NULL),
(4, 'E101 Printers Engineering', NULL),
(5, 'E202 Printing Solutions', '2021-09-20 00:00:00'),
(6, 'E203 Servicing Management', '2021-09-15 00:00:00');

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
(3, 3, 2);

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
-- course1
-- started class
(1, 1, 2, 'class 1', 20, '2021-08-17 12:00:00','2021-12-23 15:15:00','2021-07-10 00:00:00','2021-08-16 00:00:00'),
-- enrollment period open
(2, 1, 3, 'class 2', 20, '2021-12-13 12:00:00','2021-12-23 15:15:00','2021-07-10 00:00:00','2021-12-12 00:00:00'),
-- course 2
-- started class
(3, 2, 4, 'class 1', 20, '2021-08-17 12:00:00','2021-12-23 15:15:00','2021-07-10 00:00:00','2021-08-16 00:00:00'),
-- ended class
(4, 2, 5, 'class 2', 20, '2021-07-10 12:00:00','2021-09-10 15:15:00','2021-05-10 00:00:00','2021-07-09 00:00:00'),
-- course 3
-- enrollment period open
(5, 3, 6, 'class 1', 15, '2021-12-13 12:00:00','2021-12-23 15:15:00','2021-07-10 00:00:00','2021-12-12 00:00:00'),
-- started class
(6, 3, 7, 'class 2', 15, '2021-09-17 15:30:00','2021-11-23 18:45:00','2021-07-10 00:00:00','2021-09-15 00:00:00'),
-- course 4
-- class is full
(7, 4, 8, 'class 1', 2, '2021-12-13 12:00:00','2021-12-23 15:15:00','2021-07-10 00:00:00','2021-12-12 00:00:00'),
-- enrollment period open
(8, 4, 9, 'class 2', 20, '2021-11-29 08:15:00','2021-12-20 11:30:00','2021-09-10 00:00:00','2021-11-28 00:00:00'),
-- course 5
-- ended class
(9, 5, 10, 'class 1', 10, '2021-07-10 12:00:00','2021-09-10 15:15:00','2021-05-10 00:00:00','2021-07-09 00:00:00'),
-- ended class
(10, 5, 11, 'class 2', 10, '2021-07-10 12:00:00','2021-09-10 15:15:00','2021-05-10 00:00:00','2021-07-09 00:00:00'),
-- course 6
-- ended class
(11, 6, 11, 'class 1', 20, '2021-07-10 12:00:00','2021-09-10 15:15:00','2021-05-10 00:00:00','2021-07-09 00:00:00'),
-- course 1 
-- ended class
(12, 1, 5, 'class 2', 20, '2021-07-10 12:00:00','2021-09-10 15:15:00','2021-05-10 00:00:00','2021-07-09 00:00:00');

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

INSERT INTO `chapter` (`chapter_id`, `class_id`, `chapter_name`, `order`, `chapter_materials`) VALUES
(1, 1, 'chapter 1', 1, 'Chapter materials here'),
(2, 1, 'chapter 2', 2, 'Chapter materials here'),
(3, 1, 'chapter 3', 3, 'Chapter materials here'),
(4, 2, 'chapter 1', 1, 'Chapter materials here'),
(5, 2, 'chapter 2', 2, 'Chapter materials here'),
(6, 2, 'chapter 3', 3, 'Chapter materials here'),
(7, 3, 'chapter 1', 1, 'Chapter materials here'),
(8, 3, 'chapter 2', 2, 'Chapter materials here'),
(9, 3, 'chapter 3', 3, 'Chapter materials here'),
(10, 4, 'chapter 1', 1, 'Chapter materials here'),
(11, 4, 'chapter 2', 2, 'Chapter materials here'),
(12, 4, 'chapter 3', 3, 'Chapter materials here'),
(13, 5, 'chapter 1', 1, 'Chapter materials here'),
(14, 5, 'chapter 2', 2, 'Chapter materials here'),
(15, 5, 'chapter 3', 3, 'Chapter materials here'),
(16, 6, 'chapter 1', 1, 'Chapter materials here'),
(17, 6, 'chapter 2', 2, 'Chapter materials here'),
(18, 6, 'chapter 3', 3, 'Chapter materials here'),
(19, 7, 'chapter 1', 1, 'Chapter materials here'),
(20, 7, 'chapter 2', 2, 'Chapter materials here'),
(21, 7, 'chapter 3', 3, 'Chapter materials here'),
(22, 8, 'chapter 1', 1, 'Chapter materials here'),
(23, 8, 'chapter 2', 2, 'Chapter materials here'),
(24, 8, 'chapter 3', 3, 'Chapter materials here'),
(25, 9, 'chapter 1', 1, 'Chapter materials here'),
(26, 9, 'chapter 2', 2, 'Chapter materials here'),
(27, 9, 'chapter 3', 3, 'Chapter materials here'),
(28, 10, 'chapter 1', 1, 'Chapter materials here'),
(29, 10, 'chapter 2', 2, 'Chapter materials here'),
(30, 10, 'chapter 3', 3, 'Chapter materials here'),
(31, 11, 'chapter 1', 1, 'Chapter materials here'),
(32, 11, 'chapter 2', 2, 'Chapter materials here'),
(33, 11, 'chapter 3', 3, 'Chapter materials here'),
(34, 12, 'chapter 1', 1, 'Chapter materials here'),
(35, 12, 'chapter 2', 2, 'Chapter materials here'),
(36, 12, 'chapter 3', 3, 'Chapter materials here');

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
    `chapter_id` INT(11) NULL,
    `status` VARCHAR(50) NOT NULL,
    `completion_date` DATETIME NULL,
    `score` INT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'course progression'
--

INSERT INTO `course_progression` (`cc_id`, `user_id`, `course_id`, `class_id`, `chapter_id`, `status`, `completion_date`, `score`) VALUES
-- course 1 prereq for course_id 2, 3
(1, 12, 1, 1, 2, 'ongoing', NULL, NULL),
(2, 13, 1, 1, 1, 'ongoing', NULL, NULL),
(3, 14, 1, 12, 36, 'completed', '2021-09-02 00:00:00', 80),
(4, 15, 1, 12, 36, 'completed', '2021-09-02 00:00:00', 80),
(5, 16, 1, 2, NULL, 'enrolled', NULL, NULL),
(6, 17, 1, 12, 36, 'failed', '2021-09-02 00:00:00', 30),
(7, 18, 1, 12, 36, 'completed', '2021-09-02 00:00:00', 70),
(8, 19, 1, 12, 36, 'completed', '2021-09-02 00:00:00', 90),
-- course 2 prereq for course 3 only user_id= 19 can enroll
(9, 14, 2, 3, NULL, 'ongoing', NULL, NULL),
(10, 15, 2, 4, 12, 'completed', '2021-09-02 00:00:00', 80),
(11, 18, 2, 4, 12, 'completed', '2021-09-02 00:00:00', 90),
-- course 3 only user_id= 15,18 can enroll
(12, 15, 3, 6, 16, 'ongoing', NULL, NULL),
-- course 4 class 7 is full, all can enroll
(13, 15, 4, 7, NULL, 'enrolled', NULL, NULL),
(14, 20, 4, 7, NULL, 'enrolled', NULL, NULL),
-- course 5 ended already
(15, 28, 5, 9, 27, 'completed', '2021-09-02 00:00:00', 80),
(16, 27, 5, 9, 27, 'completed', '2021-09-02 00:00:00', 90),
(17, 24, 5, 10, 27, 'completed', '2021-09-02 00:00:00', 80),
-- course 6 ended already
(18, 29, 6, 11, 33, 'completed', '2021-09-02 00:00:00', 80),
(19, 22, 6, 11, 33, 'completed', '2021-09-02 00:00:00', 90),
(20, 23, 6, 11, 33, 'completed', '2021-09-02 00:00:00', 80),
-- course 1 
(21, 30, 1, 1, 2, 'ongoing', NULL, NULL);
(22, 31, 1, 1, 2, 'ongoing', NULL, NULL);
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
    `passing_mark` INT(11) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'quiz'
--

INSERT INTO `quiz` (`quiz_id`, `chapter_id`, `duration`, `graded`, `passing_mark`) VALUES
-- class 1 started class
(1, 1, 10, 0, NULL),
(2, 2, 20, 0, NULL),
(3, 3, 30, 1, 50),
-- class 2 enrollment period open
(4, 4, 10, 0, NULL),
-- class 3 started class
(5, 7, 10, 0, NULL),
(6, 8, 20, 0, NULL),
(7, 9, 30, 1, 60),
-- class 4 ended class
(8, 10, 10, 0, NULL),
(9, 11, 20, 0, NULL),
(10, 12, 30, 1, 50),
-- class 5 enrollment period open
(11, 13, 10, 0, NULL),
(12, 14, 20, 0, NULL),
-- class 6 started class
(13, 16, 10, 0, NULL),
(14, 17, 20, 0, NULL),
(15, 18, 30, 1, 50),
-- class 7 class is full
(16, 19, 10, 0, NULL),
(17, 20, 20, 0, NULL),
(18, 21, 30, 1, 50),
-- class 8 enrollment period open
(19, 22, 10, 0, NULL),
-- class 9 ended
(20, 25, 10, 0, NULL),
(21, 26, 20, 0, NULL),
(22, 27, 30, 1, 50),
-- class 10 ended
(23, 28, 10, 0, NULL),
(24, 29, 20, 0, NULL),
(25, 30, 30, 1, 50);

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
(3, 0),
(5, 0),
(8, 0),
(10, 0),
(12, 1),
(14, 1),
(17, 1),
(19, 1),
(21, 0),
(24, 0),
(26, 1),
(28, 0),
(30, 1),
(32, 0),
(35, 1),
(37, 0),
(39, 1),
(42, 1);

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
(2),
(4),
(6),
(7),
(9),
(11),
(13),
(15),
(16),
(18),
(20),
(22),
(23),
(25),
(27),
(29),
(31),
(33),
(34),
(36),
(38),
(40),
(41),
(43);

-- --------------------------------------------------------

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
CREATE table `question`(
    `question_id` INT(11) NOT NULL,
    `quiz_id` INT(11) NOT NULL,
    `question` VARCHAR(250) NOT NULL,
    `marks` INT(11) NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'question'
--

INSERT INTO `question` (`question_id`, `quiz_id`, `question`, `marks`) VALUES
-- quiz 1
(1, 1, 'Is it true that sharks have bones?', 10),
(2, 1, 'Which of the following is correct?', 10),
-- quiz 2
(3, 2, 'Is it true that sharks have bones?', NULL),
(4, 2, 'Which of the following is correct?', NULL),
-- quiz 3
(5, 3, 'Is it true that sharks have bones?', 30),
(6, 3, 'Which of the following is correct?', 30),
(7, 3, 'Which of the following is wrong?', 40),
-- quiz 4
(8, 4, 'Is it true that sharks have bones?', 30),
(9, 4, 'Which of the following is wrong?', 40),
-- quiz 5
(10, 5, 'Is it true that sharks have bones?', 10),
(11, 5, 'Which of the following is correct?', 10),
-- quiz 6
(12, 6, 'Is it true that sharks have bones?', NULL),
(13, 6, 'Which of the following is correct?', NULL),
-- quiz 7
(14, 7, 'Is it true that sharks have bones?', 30),
(15, 7, 'Which of the following is correct?', 30),
(16, 7, 'Which of the following is wrong?', 40),
-- quiz 8
(17, 8, 'Is it true that sharks have bones?', 10),
(18, 8, 'Which of the following is correct?', 10),
-- quiz 9
(19, 9, 'Is it true that sharks have bones?', NULL),
(20, 9, 'Which of the following is correct?', NULL),
-- quiz 10
(21, 10, 'Is it true that sharks have bones?', 30),
(22, 10, 'Which of the following is correct?', 30),
(23, 10, 'Which of the following is wrong?', 40),
-- quiz 11
(24, 11, 'Is it true that sharks have bones?', 10),
(25, 11, 'Which of the following is correct?', 10),
-- quiz 12
(26, 12, 'Is it true that sharks have bones?', NULL),
(27, 12, 'Which of the following is correct?', NULL),
-- quiz 13
(28, 13, 'Is it true that sharks have bones?', 10),
(29, 13, 'Which of the following is correct?', 10),
-- quiz 14
(30, 14, 'Is it true that bananas have mouths?', NULL),
(31, 14, 'Which of the following is correct?', NULL),
-- quiz 15
(32, 15, 'Is it true that bananas have mouths?', 30),
(33, 15, 'Which of the following is correct?', 30),
(34, 15, 'Which of the following is wrong?', 40),
-- quiz 16
(35, 16, 'Is it true that bananas have mouths?', 10),
(36, 16, 'Which of the following is correct?', 10),
-- quiz 17
(37, 17, 'Is it true that bananas have mouths?', NULL),
(38, 17, 'Which of the following is correct?', NULL),
-- quiz 18
(39, 18, 'Is it true that bananas have mouths?', 30),
(40, 18, 'Which of the following is correct?', 30),
(41, 18, 'Which of the following is wrong?', 40),
-- quiz 19
(42, 19, 'Is it true that bananas have mouths?', NULL),
(43, 19, 'Which of the following is correct?', NULL);

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
(1, 2, 'A', 0),
(2, 2, 'B', 0),
(3, 2, 'C', 1),
(4, 2, 'D', 0),
(5, 4, 'A', 0),
(6, 4, 'B', 0),
(7, 4, 'C', 1),
(8, 4, 'D', 0),
(9, 6, 'A', 0),
(10, 6, 'B', 1),
(11, 6, 'C', 0),
(12, 6, 'D', 0),
(13, 7, 'A', 0),
(14, 7, 'B', 0),
(15, 7, 'C', 0),
(16, 7, 'D', 1),
(17, 9, 'A', 1),
(18, 9, 'B', 0),
(19, 9, 'C', 0),
(20, 9, 'D', 0),
(21, 11, 'A', 0),
(22, 11, 'B', 0),
(23, 11, 'C', 1),
(24, 11, 'D', 0),
(25, 13, 'A', 0),
(26, 13, 'B', 0),
(27, 13, 'C', 1),
(28, 13, 'D', 0),
(29, 15, 'A', 0),
(30, 15, 'B', 1),
(31, 15, 'C', 0),
(32, 15, 'D', 0),
(33, 16, 'A', 0),
(34, 16, 'B', 0),
(35, 16, 'C', 0),
(36, 16, 'D', 1),
(37, 18, 'A', 0),
(38, 18, 'B', 0),
(39, 18, 'C', 0),
(40, 18, 'D', 1),
(41, 20, 'A', 1),
(42, 20, 'B', 0),
(43, 20, 'C', 0),
(44, 20, 'D', 0),
(45, 22, 'A', 1),
(46, 22, 'B', 0),
(47, 22, 'C', 0),
(48, 22, 'D', 0),
(49, 23, 'A', 0),
(50, 23, 'B', 0),
(51, 23, 'C', 1),
(52, 23, 'D', 0),
(53, 25, 'A', 0),
(54, 25, 'B', 0),
(55, 25, 'C', 1),
(56, 25, 'D', 0),
(57, 27, 'A', 1),
(58, 27, 'B', 0),
(59, 27, 'C', 0),
(60, 27, 'D', 0),
(61, 29, 'A', 0),
(62, 29, 'B', 1),
(63, 29, 'C', 0),
(64, 29, 'D', 0),
(65, 31, 'A', 0),
(66, 31, 'B', 1),
(67, 31, 'C', 0),
(68, 31, 'D', 0),
(69, 33, 'A', 0),
(70, 33, 'B', 0),
(71, 33, 'C', 1),
(72, 33, 'D', 0),
(73, 34, 'A', 0),
(74, 34, 'B', 1),
(75, 34, 'C', 0),
(76, 34, 'D', 0),
(77, 36, 'A', 0),
(78, 36, 'B', 0),
(79, 36, 'C', 0),
(80, 36, 'D', 1),
(81, 38, 'A', 0),
(82, 38, 'B', 0),
(83, 38, 'C', 0),
(84, 38, 'D', 1),
(85, 40, 'A', 0),
(86, 40, 'B', 0),
(87, 40, 'C', 0),
(88, 40, 'D', 1),
(89, 41, 'A', 0),
(90, 41, 'B', 0),
(91, 41, 'C', 0),
(92, 41, 'D', 1),
(93, 43, 'A', 0),
(94, 43, 'B', 0),
(95, 43, 'C', 0),
(96, 43, 'D', 1);
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
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `prerequisites`
--
ALTER TABLE `prerequisites`
  MODIFY `prereq_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `chapter`
--
ALTER TABLE `chapter`
  MODIFY `chapter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `course_progression`
--
ALTER TABLE `course_progression`
  MODIFY `cc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `quiz`
  MODIFY `quiz_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `options`
--
ALTER TABLE `options`
  MODIFY `options_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;


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
