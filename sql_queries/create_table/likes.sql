use nightclubconsultants;

CREATE TABLE likes
(
drinker varchar(80) NOT NULL,
beer varchar(80) NOT NULL,

PRIMARY KEY(drinker, beer)
);