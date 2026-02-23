CREATE DATABASE company_db;
USE company_db;
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    dept_id INT,
    manager_id INT,
    
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE
);
CREATE TABLE employee_projects (
    emp_id INT,
    project_id INT,
    hours_worked INT DEFAULT 0,
    
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
INSERT INTO departments VALUES
(1, 'IT'),
(2, 'Sales'),
(3, 'HR'),
(4, 'Finance'),
(5, 'Marketing');
INSERT INTO employees VALUES
(101, 'Amit', 60000, '2021-05-10', 1, NULL),
(102, 'Neha', 55000, '2022-07-15', 2, 101),
(103, 'Ravi', 75000, '2019-03-20', 1, 101),
(104, 'Priya', 50000, '2023-01-10', 3, 103),
(105, 'Ankit', 40000, '2020-11-05', 2, 102),
(106, 'Karan', 90000, '2018-02-01', 4, NULL),
(107, 'Asha', 65000, '2022-09-17', 1, 103),
(108, 'Vikram', 48000, '2024-01-01', 5, 106),
(109, 'Meera', 72000, '2020-06-25', 1, 103),
(110, 'Arjun', 53000, '2023-08-10', 2, 102);
INSERT INTO projects VALUES
(1, 'Banking System', '2023-01-01', NULL),
(2, 'E-commerce App', '2022-05-01', NULL),
(3, 'HR Portal', '2021-03-15', NULL);
INSERT INTO employee_projects VALUES
(101,1,120),
(101,2,80),
(102,2,100),
(103,1,200),
(104,3,90),
(105,2,60),
(106,1,150),
(107,1,130),
(107,3,40),
(108,2,70),
(109,1,110),
(110,2,95);
