use nightclubconsultants;

CREATE TABLE works_at
(
bartender varchar(80) NOT NULL,
night_club varchar(80) NOT NULL,

PRIMARY KEY(bartender, night_club)
);