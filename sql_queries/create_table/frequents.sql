use nightclubconsultants;

CREATE TABLE frequents
(
drinker varchar(80) NOT NULL,
night_club varchar(80) NOT NULL,
date date,
cover_fee int,

PRIMARY KEY(drinker, night_club, date)
);