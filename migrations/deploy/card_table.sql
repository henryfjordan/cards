-- Deploy cards:card_table to pg

BEGIN;

CREATE TABLE card (
	id SERIAL NOT NULL,
	author INTEGER,
	message VARCHAR(1000),
	PRIMARY KEY (id),
	FOREIGN KEY(author) REFERENCES author (id)
);

COMMIT;
