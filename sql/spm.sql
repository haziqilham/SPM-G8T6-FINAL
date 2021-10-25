SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `spm_database` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_database`;


------"User" table-----

DROP TABLE IF EXISTS 'user';
CREATE table IF NOT EXISTS 'user'(
    'user_id' char(50) NOT NULL,
    'user_name' varchar(50) NOT NULL,
    'designation' char (50) NOT NULL,
    'department' char(50) NOT NULL,
    'role' char(50) NOT NULL,

    PRIMARY KEY ('user_id')

)ENGINE=InnoDB DEFAULT CHARSET=utf8;


----"Prerequisites" table--------
DROP TABLE IF EXISTS 'prerequisites';
CREATE table IF NOT EXISTS 'prerequisites'(
    'prereq_id' int NOT NULL,
    -- 'course_id' int NOT NULL,
    'prereq_course_id' int NOT NULL,

    PRIMARY KEY ('prereq_id') 
)ENGINE=InnoDB DEFAULT CHARSET=utf8;



-----"Course" table------
DROP TABLE IF EXISTS 'course';
CREATE table IF NOT EXISTS 'course'(
    'course_id' int NOT NULL,
    'course_name' char(50) NOT NULL,
    'archive_date' date,

    PRIMARY KEY ('course_id') 
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


----"Class" table----

DROP TABLE IF EXISTS 'class'
CREATE TABLE IF NOT EXISTS 'class'(
    'class_id' int NOT NULL,
    'class_name' varchar(50) NOT NULL,
    'capacity' int NOT NULL,
    'start_Date' date NOT NULL,
    'end_Date' date NOT NULL,
    'start_Time' time NOT NULL,
    'end_Time' time NOT NULL,
    'start_enrollment' date NOT NULL,
    'end_enrollment' date NOT NULL,

    PRIMARY KEY ('class_id')

)ENGINE=InnoDB DEFAULT CHARSET=utf8;



----"Chapter" table ----
DROP TABLE IF EXISTS 'chapter';
CREATE TABLE IF NOT EXISTS 'chapter'(
    'chapter_id' int NOT NULL,
    'chapter_name' varchar(50) NOT NULL,
    'order' int NOT NULL,
    ----see sql filestream for info---
    -- 'chapter_materials' 
    PRIMARY KEY ('chapter_id')
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


-----"Quiz" table-----
DROP TABLE IF EXISTS 'quiz';
CREATE TABLE IF NOT EXISTS 'quiz'(
    'quiz_id' int NOT NULL,
    'duration' time NOT NULL,
    ----boolean value in the form of 0 & 1
    'graded?' bit NULL DEFAULT 0,

    PRIMARY KEY('quiz_id')
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


-----"Question" table-----
DROP TABLE IF EXISTS 'question';
CREATE TABLE IF NOT EXISTS 'question'(
    'question_id' int NOT NULL,
    'question' varchar NOT NULL,
    'marks' int NOT NULL,

    PRIMARY KEY ('question_id')
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


----KIV-----
---"Question_TF" table----
DROP TABLE IF EXISTS 'question_TF';
CREATE TABLE IF NOT EXISTS 'question_TF'(
    'question_TF_id' int NOT NULL,
    'correct_value?'
)




------KIV----
----"Enrolled Course" table

CREATE table 'enrolled_course'(
    -- unsure if we want to set a limit for id
    'cc_id' int(10) NOT NULL,
    'status' char(50) NOT NULL,
    'completion_date' date,
    'grade' int NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

