-- https://docs.google.com/document/d/1nkGeqs25Ln6bxYMynFQEullZjdVnmr0Z/edit
-- Lab 18.1 – Chuyển đổi mô hình ER sang mô hình quan hệ

-- Ở lab này các bạn sẽ chuyển đổi sang mô hình quan hệ cho các mô hình ER mà các bạn đã thực hiện trong Lab 15 là cơ sở dữ liệu quản lý nhân viên và cơ sở dữ liệu quản lý điểm sinh viên.

-- Yêu cầu 1: Chuyển đổi sang mô hình quan hệ từ mô hình ER cơ sở dữ liệu quản lý nhân viên

CREATE TABLE Department(
  id INT NOT NULL AUTO_INCREMENT, -- ma phong ban
  name VARCHAR(30) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Employee (
  id INT NOT NULL AUTO_INCREMENT, -- ma nhan vien
  first_name VARCHAR(30),
  middle_name VARCHAR(40),
  last_name VARCHAR(30),
  fullname VARCHAR(100) AS (CONCAT_WS(' ', first_name, middle_name, last_name)),
  position VARCHAR(36),
  birthdate DATE,
  age INT,
  PRIMARY KEY (id),
  department_id INT,
  CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES Department(id)
);

SET GLOBAL log_bin_trust_function_creators = 1;
DELIMITER $$
CREATE FUNCTION CalculateAge(birthdate DATE) RETURNS INT
BEGIN
  DECLARE age INT;
  SET age = (YEAR(CURDATE())-YEAR(birthdate)) - (DATEFORMAT(CURDATE(), "%m%d")<DATEFORMAT(birthdate, "%m%d"));
  RETURN age;
END;$$
CREATE TRIGGER tb_insert_employee_age
BEFORE INSERT ON Employee 
FOR EACH ROW
BEGIN
    IF NOT ISNULL(NEW.birthdate) THEN
        SET NEW.age = CalculateAge(NEW.birthdate);
    END IF;
END$$
CREATE TRIGGER tb_update_employee_age
BEFORE UPDATE ON Employee 
FOR EACH ROW
BEGIN
    IF NOT ISNULL(NEW.birthdate) THEN
        SET NEW.age = CalculateAge(NEW.birthdate);
    END IF;
END$$
DELIMITER ;

CREATE TABLE Employee_Addresses(
  id INT NOT NULL AUTO_INCREMENT,
  address TEXT,
  employeeId INT,
  PRIMARY KEY (id),
  FOREIGN KEY (employeeId) REFERENCES Employee(id)
);

CREATE TABLE Project(
  id INT NOT NULL AUTO_INCREMENT, -- ma du an
  name VARCHAR(30) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Employee_Project(
  -- quan he N-M tu model Employee va model Project
  id INT NOT NULL AUTO_INCREMENT,
  employeeId INT,
  projectId INT,
  PRIMARY KEY (id),
  CONSTRAINT fk_employee FOREIGN KEY (employeeId) REFERENCES Employee(id),
  CONSTRAINT fk_project FOREIGN KEY (projectId) REFERENCES Project(id)
);

-- Yêu cầu 2: Chuyển đổi sang mô hình quan hệ từ mô hình ER cơ sở dữ liệu quản lý điểm sinh viên


CREATE TABLE Student (
  id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(30),
  middle_name VARCHAR(40),
  last_name VARCHAR(30),
  fullname VARCHAR(100) AS (CONCAT(first_name, ' ', middle_name, ' ', last_name)),
  position VARCHAR(36),
  birthdate DATE,
  age INT,
  PRIMARY KEY (id),
  classId INT
);

CREATE TABLE Student_Addresses(
  id INT NOT NULL AUTO_INCREMENT,
  address TEXT,
  studentId INT,
  PRIMARY KEY (id),
  FOREIGN KEY (studentId) REFERENCES Student(id)
);
SET GLOBAL log_bin_trust_function_creators = 1;
DELIMITER $$
CREATE FUNCTION CalculateAge(birthdate DATE) RETURNS INT
BEGIN
  DECLARE age INT;
  SET age = (YEAR(CURDATE())-YEAR(birthdate)) - (DATEFORMAT(CURDATE(), "%m%d")<DATEFORMAT(birthdate, "%m%d"));
  RETURN age;
END;$$
CREATE TRIGGER tb_insert_student_age
BEFORE INSERT ON Student 
FOR EACH ROW
BEGIN
    IF NOT ISNULL(NEW.birthdate) THEN
        SET NEW.age = CalculateAge(NEW.birthdate);
    END IF;
END$$
CREATE TRIGGER tb_update_student_age
BEFORE UPDATE ON Student 
FOR EACH ROW
BEGIN
    IF NOT ISNULL(NEW.birthdate) THEN
        SET NEW.age = CalculateAge(NEW.birthdate);
    END IF;
END$$
DELIMITER ;

CREATE TABLE Course(
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  closeDate DATE,
  PRIMARY KEY (id)
);

CREATE TABLE Class(
  id INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (id)
);

ALTER TABLE Student
ADD CONSTRAINT fk_class_id FOREIGN KEY (classId) REFERENCES Class(id);

CREATE TABLE Scores(
  id INT NOT NULL AUTO_INCREMENT,
  studentId INT,
  courseId INT,
  classId INT,
  assessment1 DECIMAL(7, 2),
  assessment2 DECIMAL(7, 2),
  assessment3 DECIMAL(7, 2),
  exam1 DECIMAL(7, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (studentId) REFERENCES Student(id),
  FOREIGN KEY (courseId) REFERENCES Course(id),
  FOREIGN KEY (classId) REFERENCES Class(id)
);