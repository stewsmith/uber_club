use nightclubconsultants;

CREATE TABLE drinkers
(
name varchar(80) NOT NULL,
phone varchar(10) NOT NULL,
addr varchar(80),
city varchar(80),
gender varchar(1),
age int,

PRIMARY KEY(name, phone)
);