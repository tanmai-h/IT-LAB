CREATE VIEW TNS AS
SELECT m.title, r.stars, rv.name FROM Rating r inner join Movie m on r.mID=m.mID inner join Reviewer rv on r.rID=rv.rID;

select title from Movie where year in (select max(m.year) from Movie m inner join TNS t on t.title=m.title and t.name="Chris Jackson");
-- select t.title from Movie m inner join TNS t on t.title=m.title and t.name="Chris Jackson" order by(year) desc limit 1;

select title 
