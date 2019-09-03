use COMPANY;

-- query 1--
select E.Fname,E.Lname,E.Bdate,D.Dname, Address from EMPLOYEE E inner join DEPARTMENT D on E.Dno=D.Dnumber where D.Dname="Administration";

-- query 2--
select sum(Salary),max(Salary),min(Salary),avg(Salary) from EMPLOYEE E inner join DEPARTMENT D on E.Dno=D.Dnumber where D.Dname="Research";

-- query 3--
select count(Ssn) from EMPLOYEE E inner join DEPARTMENT D on E.Dno=D.Dnumber where D.Dname="Administration";

-- query 4--
select Pname,Pnumber,count(w.Pno) from PROJECT p inner join WORKS_ON w on p.Pnumber=w.Pno group by p.Pnumber;

-- query 5--
select p.Pnumber,p.Pname, count(*) from WORKS_ON w inner join PROJECT p on w.Pno=p.Pnumber where w.essn in (select ssn from EMPLOYEE where Dno=5) group by p.Pnumber;

-- query 6--
select Pnumber,Dnum,Lname,Address from PROJECT as P inner join DEPARTMENT as D on P.Dnum=D.Dnumber inner join EMPLOYEE as E on Mgr_Ssn=Ssn and Plocation="Houston";

-- query 7--
select Fname,Lname,Pno,Dnumber from EMPLOYEE as E inner join WORKS_ON as W on E.Ssn=W.Essn inner join DEPARTMENT as D on D.Dnumber=E.Dno order by Dnumber,Fname,Lname;

-- query 8--
select concat(Fname," ",Lname) as Name from EMPLOYEE where Super_Ssn is null;

-- query 9--
select concat(A.Fname," ",A.Lname) as Name from EMPLOYEE as A inner join EMPLOYEE as B on A.Super_Ssn=B.Ssn and B.Super_Ssn=987654321;

-- query 10--
select Dname,concat(Fname," ",Lname) as Name,Salary from DEPARTMENT as D inner join EMPLOYEE as E on D.Mgr_Ssn=E.Ssn;

-- query 11--
select concat(A.Fname," ",A.Lname) as Name,concat(B.Fname," ",B.Lname) as Supervisor,A.salary from EMPLOYEE as A inner join EMPLOYEE as B on A.Super_Ssn=B.Ssn inner join DEPARTMENT as D on D.Dnumber=A.Dno and Dname="Research";

-- query 12--
select Pname,Dname,count(Pno),sum(hours) from PROJECT as P inner join WORKS_ON as W on P.Pnumber=W.Pno inner join DEPARTMENT as D on D.Dnumber=P.Dnum group by Pno;

-- query 13--
select Pname,Dname,count(Pno),sum(hours) from PROJECT as P inner join WORKS_ON as W on P.Pnumber=W.Pno inner join DEPARTMENT as D on D.Dnumber=P.Dnum group by Pno having count(Pno)>1;

-- query 14--
-- select concat(Fname," ",Lname) as Name from PROJECT as P inner join WORKS_ON as W on W.Pno=P.Pnumber inner join EMPLOYEE as E on E.Ssn=W.Essn and P.Dnum=5 group by Name;
select concat(Fname," ",Lname) as name from EMPLOYEE where Dno=5 order by name;

-- query 15--
select concat(Fname," ",Lname) as Name from PROJECT as P inner join WORKS_ON as W on W.Pno=P.Pnumber inner join EMPLOYEE as E on E.Ssn=W.Essn where E.Dno=5 and P.Pname="ProductX" group by Ssn having sum(Hours)>10;
select concat(Fname," ", Lname) from EMPLOYEE where Ssn in (select Essn from WORKS_ON where Essn in (select Ssn from EMPLOYEE where dno=5) AND Pno=1 group by (Essn) having sum(Hours)>10);
-- select concat(Fname," ",Lname) as Name from PROJECT as P inner join DEPARTMENT as D on P.Dnum=D.Dnumber inner join WORKS_ON as W on W.Pno=P.Pnumber inner join EMPLOYEE as E on E.Ssn=W.Essn where E.Dno=5 and P.Pname="ProductX" group by Ssn having sum(Hours)>10;

-- query 16--
select concat(Fname," ",Lname) as Name from EMPLOYEE as E inner join DEPENDENT as D on E.Ssn=D.Essn and E.Fname=D.Dependent_name;

-- query 17--
-- select concat(A.Fname," ",A.Lname) as Name from EMPLOYEE as A inner join EMPLOYEE as B on A.Super_Ssn=B.Ssn and B.Fname="Franklin" and B.Lname="Wong";
select concat(Fname," ",Lname) from EMPLOYEE where Super_ssn in (select e.Ssn from EMPLOYEE e where e.Fname="Franklin");

-- query 18--
select Pname,sum(Hours) from PROJECT as P inner join WORKS_ON as W on P.Pnumber=W.Pno group by Pname;

-- query 19--
select avg(Salary) from EMPLOYEE as E where Sex="F";

