/*-----------------------------------------*/
Go
CREATE PROCEDURE usp_get_employees_salary_above(@num decimal(14))
    AS
        SELECT FirstName, LastName FROM Employees 
        WHERE Salary >= @num
        ORDER BY FirstName, LastName
    ;
end;

CALL usp_get_employees_salary_above 48100;
/*---------------------------------------------*/
Go
CREATE PROCEDURE usp_get_towns_starting_with(@letter CHAR(2))
    AS
        SELECT Name FROM Towns
        WHERE Name LIKE concate(@letter, '%')
        ORDER BY Name
    ;
END;
/*--------------------------------------------*/
GO
CREATE FUNCTION ufn_get_salary_level(@Salary decimal(18,4))
RETURNS VARCHAR(10) AS
BEGIN
    declare @SalaryLevel VARCHAR(10)
    if(Salary < 30000)
        set  @SalaryLevel = 'Low'
    else if(@SalaryLevel >= 30000 and @Salary <= 50000)
        set @SalaryLevel = 'Average'
    ELSE
        set @SalaryLevel = 'High'

    return @SalaryLevel
END
End;
/*----------------------------------------------*/
create FUNCTION ufn_calculate_future_value(@sum INT, @rate float, @years INT)
returns money as
BEGIN   
    return @sum * POWER(1+@rate, @years)
END;
/*-----------------------------------------------*/

DECLARE emp_info CURSOR
    FOR
        select ID, FirstName, LastName, Salary
        from Employees
        ;
open emp_info;
getInfo: LOOP


