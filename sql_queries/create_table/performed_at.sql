use nightclubconsultants;

CREATE TABLE performed_at
(
deejay varchar(80) NOT NULL,
night_club varchar(80) NOT NULL,
date date NOT NULL,
PRIMARY KEY(deejay, night_club, date)
);
