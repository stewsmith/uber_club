use nightclubconsultants;

CREATE TABLE beers
(
name varchar(80) NOT NULL,
manf varchar(80) NOT NULL,

PRIMARY KEY(name, manf)
);