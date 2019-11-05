delimiter //

-- *************************************************************** 
create table student_marks (
	id int primary key, 
	name char(50), sub1 int, sub2 int,
	 sub3 int, sub4 int, 
	 sub5 int, total int default 0, 
	 per_marks float default 0, 
	 grade varchar(100)
);

//


insert into student_marks (id,name, sub1,sub2,sub3,sub4,sub5) values (1,"asds", 0,0,0,0,0);
insert into student_marks (id,name, sub1,sub2,sub3,sub4,sub5) values (2,"pplp", 0,0,0,0,0);
insert into student_marks (id,name, sub1,sub2,sub3,sub4,sub5) values (3,"jghjghj", 0,0,0,0,0);
insert into student_marks (id,name, sub1,sub2,sub3,sub4,sub5) values (4,"tyrts", 0,0,0,0,0);

create trigger marks
	before update on student_marks
	for each row
	BEGIN
		set new.total = new.sub1+new.sub2+new.sub3+new.sub4+new.sub5;
		set new.per_marks = new.total / 5;
		if new.per_marks >= 90 then
			set new.grade = "excellent";
		elseif new.per_marks >= 75 then
			set new.grade = "very good";
		elseif new.per_marks >= 60 then
			set new.grade = "good";
		elseif new.per_marks >= 40 then
			set new.grade = "average";
		else
			set new.grade = "not promoted";
		end if;
	end
//



-- *************************************************************** 
CREATE TABLE blog (
	id int,
	title varchar(20),
	content varchar(20),
	deleted int,
	PRIMARY KEY (id)
);
//
CREATE TABLE audit( 
	blog_id int,
	changetype enum('NEW','EDIT','DELETE') NOT NULL,
	changetime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE
	CURRENT_TIMESTAMP,
	foreign key(blog_id) references blog(id)
);
//
create trigger b_insert 
	after insert on blog
	for each row
	BEGIN
		declare flag char(10) default("NEW");
		if new.deleted = 1 then
			set flag = "DELETE";
		end if;

		insert into audit (blog_id, changetype) values (new.id,flag);
	end
//

create trigger b_update
	after update on blog
	for each row
	BEGIN
		declare flag char(10) default("EDIT");
		if new.deleted = 1 then
			set flag = "DELETE";
		end if;

		insert into audit (blog_id, changetype) values (new.id, flag);
	end
//

delimiter ;

-- *************************************************************** 

create table patient (
	id int primary key,
	name varchar(100)
);

create table medicine (
	pid int,
	medicine varchar(100),
	foreign key (pid) references patient(id) on delete cascade on update cascade
);

create table bill (
	pid int,
	details text,
	foreign key (pid) references patient(id) on delete cascade on update cascade
);

create table room (
	room_no int primary key,
	pid int,
	room_status varchar(10)
);

DELIMITER //

create trigger update_records 
    after delete on patient
    for each row
    begin
    	delete from medicine where pid = old.id;
    	delete from bill where pid = old.id;
    	update room set room_status = 'EMPTY', pid = NULL where pid = old.id;
	end
//

delimiter ;

insert into patient values (1,	'patient1');
insert into medicine values (1,	'dolo');
insert into bill values (1,	'pfizer 100mg dolo');
insert into room values (20,1,'FULL');

delete from patient where id = 1;
