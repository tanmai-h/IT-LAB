CREATE VIEW TNS AS
SELECT m.title, r.stars, rv.name FROM Rating r 
inner join Movie m on r.mID=m.mID 
inner join Reviewer rv on r.rID=rv.rID;

select title from Movie where year in 
(select max(m.year) from Movie m inner join TNS t on t.title=m.title and t.name="Chris Jackson");
-- select t.title from Movie m inner join TNS t on t.title=m.title and t.name="Chris Jackson" order by(year) desc limit 1;

-- select title 

-- create view TNS as select title,name,stars from Movie M inner join Rating R on M.mID=R.mID inner join Reviewer Re on Re.rID=R.rID;
-- select max(year) from Movie M inner join TNS T on M.title=T.title and name="Chris Jackson";

create view RatingStats as 
select title, count(stars) as Count_Stars, avg(stars) as Avg_Stars 
from TNS group by title having count(stars) >= 1;

select title from RatingStats where Avg_Stars 
in (select max(Avg_Stars) from RatingStats 
where title in (select title from RatingStats where Count_Stars>=3));

create view favourites as 
select rID,mID from Rating where (rID,stars) 
in (select rID,max(stars) as Max_Stars from Rating group by rID);

select C.name,D.name,title from favourites A 
inner join favourites B on A.mID = B.mID and A.rID != B.rID 
inner join Reviewer C on A.rID=C.rID 
inner join Reviewer D on B.rID=D.rID 
inner join Movie M on M.mID=A.mID where A.rID > B.rID;