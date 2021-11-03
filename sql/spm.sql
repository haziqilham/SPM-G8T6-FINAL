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
(2);

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
(1);

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
(3);

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
(1, 'cuname', 'Claudia', 'Technical boss', 'Tech department', 'Trainers'),
(2, 'muname', 'Marcus', 'Big Boss', 'HR Department', 'Administrator'),
(3, 'huname', 'Haziq', 'Learner', 'Engineer', 'Learners');

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
(3, 'CS440 Cybersec');

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
(2, 3, 1);

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
    `start_Date` DATE NOT NULL,
    `end_Date` DATE NOT NULL,
    `start_Time` TIME NOT NULL,
    `end_Time` TIME NOT NULL,
    `start_enrollment` DATE NOT NULL,
    `end_enrollment` DATE NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table 'class'
--

INSERT INTO `class` (`class_id`, `course_id`, `trainer_id`, `class_name`, `capacity`, `start_Date`, `end_Date`, `start_Time`, `end_Time`, `start_enrollment`, `end_enrollment`) VALUES
(1, 1, 1, 'class 1', 20, '2021-10-27','2021-10-27','00:00:00','00:00:00','2021-10-27','2021-10-27');

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
(3, 1, 'chapter 3', 3);

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
(1, 3, 1, 1, 2, 'ongoing');

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
(1, 1, 20, 1, 50);

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
(1, 1);

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
(2);

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
(2, 1, 'testing mcq', 1);

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
(4, 2, 'D', 0);

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
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `prerequisites`
--
ALTER TABLE `prerequisites`
  MODIFY `prereq_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `chapter`
--
ALTER TABLE `chapter`
  MODIFY `chapter_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `course_progression`
--
ALTER TABLE `course_progression`
  MODIFY `cc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `question`
--
ALTER TABLE `question`
  MODIFY `question_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `options`
--
ALTER TABLE `options`
  MODIFY `options_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;


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
-- Constraints for table `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_fk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`);

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
