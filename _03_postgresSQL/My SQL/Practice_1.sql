create table vasudev(
f_frnd varchar(50),
s_frnd varchar(50),
t_frnd varchar(50)
)
comment = "This table contains my frnds list";
show table status where name = "Vasudev";

select * from vasudev;
insert into vasudev(f_frnd,s_frnd,t_frnd)
values("uday","vasu","vasudev"),("Swapna","Swetha","Gwotham");
alter table vasudev comment = "This is alter Comment";
select f_frnd from VASUDEV;

drop table vasudev
