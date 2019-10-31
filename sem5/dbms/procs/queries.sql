/*-----------------------------------------*/
DELIMITER $$
CREATE PROCEDURE usp_get_employees_salary_above(num decimal(14))
    BEGIN
        SELECT FirstName, LastName FROM Employees 
        WHERE Salary >= num
        ORDER BY FirstName, LastName;
    end
$$
DELIMITER ;

CALL usp_get_employees_salary_above(48100);

/*---------------------------------------------*/

DELIMITER $$
CREATE PROCEDURE usp_get_towns_starting_with(letter CHAR(2))
    BEGIN
        SELECT Name FROM Towns
        WHERE Name LIKE concat(letter, '%')
        ORDER BY Name;
   end
$$
DELIMITER ;
call usp_get_towns_starting_with('b');

/*--------------------------------------------*/
DELIMITER $$
CREATE FUNCTION ufn_get_salary_level(Salary integer)
    RETURNS VARCHAR(10)
    BEGIN
        declare SalaryLevel VARCHAR(10);
        if Salary < 30000 THEN
            set  SalaryLevel = 'Low';
        elseif SalaryLevel >= 30000 and Salary <= 50000 THEN
            set SalaryLevel = 'Average';
        ELSE
            set SalaryLevel = 'High';
        end if;
        return SalaryLevel;
    END;
$$
DELIMITER ;

SELECT ufn_get_salary_level(45000);

/*----------------------------------------------*/
DELIMITER $$
create FUNCTION ufn_calculate_future_value(sum INT, rate float, years INT)
    returns FLOAT
    BEGIN   
        DECLARE money FLOAT;
        return sum * POWER(1+rate, years);
    END;
$$
DELIMITER ;

SELECT ufn_calculate_future_value(100,0.08,1);

/*--------------------------------------_*/

DELIMITER $$
CREATE PROCEDURE info (IN dept VARCHAR(20))
    BEGIN
        DECLARE emp_name varchar(32);
        DECLARE done INT DEFAULT 0;
        declare names VARCHAR(100) DEFAULT "";
        DECLARE cur_emp CURSOR FOR SELECT name FROM dep WHERE dep.dept=dept;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;

    OPEN cur_emp;
    
    dept_cur:LOOP
        FETCH cur_emp INTO emp_name;
        IF done=1 THEN 
            LEAVE dept_cur;
        END IF;
        set `names` = CONCAT(names, concat("\n", `emp_name`));
        -- SELECT emp_name;
        END LOOP dept_cur;
        select names;
    CLOSE cur_emp;
END $$
DELIMITER ;

CALL info('IT');
/*******************************************/

DELIMITER $$
    CREATE PROCEDURE changer()
    BEGIN
        DECLARE id INT DEFAULT 0;
        DECLARE prev_sal INT DEFAULT 0;
        DECLARE desig VARCHAR(32);
        DECLARE done INT DEFAULT 0;
        DECLARE cur_sal CURSOR FOR SELECT sal.id FROM sal;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;

    OPEN cur_sal;
    emp_loop:LOOP
        FETCH cur_sal INTO id;
        IF done=1 THEN 
            LEAVE emp_loop;
        END IF;
        SELECT sal.sal INTO prev_sal FROM sal WHERE sal.id=id;
        SELECT sal.desig INTO desig FROM sal WHERE sal.id=id;
        
        IF desig='manager' THEN 
            UPDATE sal SET sal.sal=(20000 + prev_sal) WHERE sal.id=id;
        ELSE 
            UPDATE sal SET sal.sal=(30000 + prev_sal) WHERE sal.id=id;
        
        END IF;

        END LOOP emp_loop;

        CLOSE cur_sal;
    END $$
DELIMITER ;

CALL changer();
SELECT * FROM sal;