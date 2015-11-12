-- Deploy cards:author_table to pg

BEGIN;

CREATE TABLE author (
	id SERIAL NOT NULL,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100),
	address VARCHAR(300),
	PRIMARY KEY (id)
);


COMMIT;
