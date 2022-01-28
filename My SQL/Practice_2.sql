create table my_frnds(
f_frnd varchar(50),
s_frnd varchar(50),
num varchar(50),
ff_frnd varchar(50)
);

select * from my_frnds;

insert into my_frnds (f_frnd,s_frnd,num,ff_frnd)
values('vasanth','vasudev','vassunitha','chinthalli'),
('gowtham','simha','swetha','pawapna'),
('ajith','balu','cahrry','devil'),
('madhu','balu','fish','kaza');

select * from my_frnds;

drop table my_frnds;

select f_frnd from my_frnds;

select * from my_frnds where f_frnd = 'vasanth'; 

select * from  my_frnds where f_frnd like 'a%';

select * from my_frnds where f_frnd like '%u';

select * from my_frnds order by s_frnd desc;

select * from my_frnds order by s_frnd asc;

select * from my_frnds order by t_frnd asc;

select f_frnd,t_frnd from my_frnds group by s_frnd;

select * from my_frnds having s_no <=1;






delete from my_frnds where s_frnd = 'simha';
select * from my_frnds;












