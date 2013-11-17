use nightclubconsultants;

CREATE TABLE serves
(
bartender varchar(80) NOT NULL,
drinker varchar(80) NOT NULL,
beer varchar(80),
tip int,
date date,
time time NOT NULL,
night_club varchar(80) NOT NULL,

PRIMARY KEY(bartender, drinker, time)
);