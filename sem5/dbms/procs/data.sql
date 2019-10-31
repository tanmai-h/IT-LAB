use procs;
CREATE TABLE Employees (FirstName VARCHAR(32), LastName VARCHAR(32), Salary FLOAT);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('aaa','AAA',1000);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('ccc','CCC',3000);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('bbb','BBB',2000);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('ddd','DDD',4000);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('eee','EEE',5000);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('fff','FFF',50000);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('abc','ABC',60000);
INSERT INTO Employees (FirstName, LastName, Salary) VALUES ('ab','AB',40000);

CREATE TABLE Towns (Name VARCHAR(32));
INSERT INTO Towns (Name) VALUES ('Bengaluru');
INSERT INTO Towns (Name) VALUES ('Bombay');
INSERT INTO Towns (Name) VALUES ('Delhi');
INSERT INTO Towns (Name) VALUES ('Mangalore');
INSERT INTO Towns (Name) VALUES ('Madikeri');

CREATE TABLE dep (name VARCHAR(32), dept VARCHAR(32));
INSERT INTO dep (name,dept) VALUES ('aaa','IT');
INSERT INTO dep (name,dept) VALUES ('bbb','IT');
INSERT INTO dep (name,dept) VALUES ('ccc','IT');
INSERT INTO dep (name,dept) VALUES ('ddd','CSE');
INSERT INTO dep (name,dept) VALUES ('eee','CSE');

CREATE TABLE sal (id INT, name VARCHAR(32), sal INT(10), desig VARCHAR(32));
INSERT INTO sal (id,name,sal,desig) VALUES (1,'aaa',100,'manager');
INSERT INTO sal (id,name,sal,desig) VALUES (2,'bbb',200,'manager');
INSERT INTO sal (id,name,sal,desig) VALUES (3,'ccc',300,'trainer');
INSERT INTO sal (id,name,sal,desig) VALUES (4,'ddd',400,'trainer');