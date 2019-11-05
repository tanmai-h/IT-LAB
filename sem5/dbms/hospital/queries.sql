select pt.name, pt.PCP, ph.name from Patient pt 
inner join PhysicianE ph on pt.PCP=ph.EmployeeID 
where pt.pcp not in (select p.Head from Department p);

select pt.Name as "Patient",ph.name as "Physician" from Patient pt 
inner join PhysicianE ph on pt.PCP=ph.EmployeeID
where pt.SSN in (select a.Patient from Appointment a 
where a.PrepNurse in (select n.EmployeeID from Nurse n where n.Registered=1) 
group by a.Patient having count(a.Patient) >= 2);

-- select pt.Name as "Patient", ph.name as "Physician" from (select Patient ,Physician from Undergoes where Procedures in (select pr.Code from Procedures pr where pr.Cost > 5000)) as tmp inner join Patient pt on pt.SSN=tmp.Patient inner join PhysicianE ph on ph.EmployeeID=tmp.Physician;
select pt.Name as "Patient", ph.name as "Physician" 
from Patient pt inner join PhysicianE ph on pt.PCP=ph.EmployeeID 
where pt.SSN in (select Patient from Undergoes where Procedures 
in (select pr.Code from Procedures pr where pr.Cost > 5000));

select pt.Name as "Patient", ph.name as "Physician", ph.Position, pr.Name, u.DateUndergoes, train.CertificationExpires from Undergoes u 
inner join Patient pt on pt.SSN=u.Patient 
inner join PhysicianE ph on ph.EmployeeID=u.Physician
inner join Procedures pr on pr.Code=u.Procedures
inner join Trained_In train on u.Procedures=train.Treatment
where u.DateUndergoes > train.CertificationExpires;

-- select u.Physician from Undergoes u left join Trained_In train on u.Physician=train.Physician and u.Procedures=train.Treatment;

select distinct(ph.Name,un.Procedures) FROM PhysicianE ph, Undergoes un, Trained_In ti 
WHERE ph.EmployeeID = un.Physician AND ph.EmployeeID = ti.Physician 
AND (un.DateUndergoes > ti.CertificationExpires or un.Procedures not in 
(select treatment from Trained_In where Physician=ph.EmployeeID));