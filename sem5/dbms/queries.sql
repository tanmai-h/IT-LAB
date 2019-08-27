select Fname,Lname,Bdate,Address from EMPLOYEE E inner join DEPARTMENT D on E.Dno=D.Dnumber where D.Dname="Administration";

select sum(Salary),max(Salary),min(Salary),avg(Salary) from EMPLOYEE E inner join DEPARTMENT D on E.Dno=D.Dnumber where D.Dname="Research";

select count(Ssn) from EMPLOYEE E inner join DEPARTMENT D on E.Dno=D.Dnumber where D.Dname="Administration";

select Pname,Pnumber,count(w.Pno) from PROJECT p inner join WORKS_ON w on p.Pnumber=w.Pno group by p.Pnumber;

select p.Pnumber,p.Pname, count(*) from WORKS_ON w inner join PROJECT p on w.Pno=p.Pnumber where w.essn in (select ssn from EMPLOYEE where Dno=5) group by p.Pnumber;