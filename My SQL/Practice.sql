CREATE DATABASE UDAY;
USE UDAY;
CREATE TABLE UDAY_ESWAR(
U_Name varchar(50),
U_Num varchar(50),
U_Add varchar(50)
);

select * from UDAY_ESWAR;
DROP TABLE UDAY_ESWAR;

insert into UDAY_ESWAR (U_Name,U_Num,U_Add)
values("uday","9491143753","NDD");
alter table UDAY_ESWAR add column vasu varchar(50);

rename table UDAY_ESWAR to GOWTHAM;
DROP table GOWTHAM;
select * from GOWTHAM;
alter table GOWTHAM modify U_Num VARCHAR(20);
alter table GOWTHAM CHANGE U_Num D_Num VARCHAR (50);
SELECT * FROM GOWTHAM;
alter table GOWTHAM drop column D_Num;
create table UDAY.VASUDEVS (select* FROM GOWTHAM);

SELECT * FROM VASUDEVS;
truncate table vasudevs;

select * from VASUDEV;

DROP table VASUDEV;

