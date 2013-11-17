use nightclubconsultants;

CREATE TABLE sells
(
beer varchar(80) NOT NULL,
night_club varchar(80) NOT NULL,
price int,

PRIMARY KEY(beer, night_club)
);