-- Revert cards:author_table from pg

BEGIN;

DROP TABLE author CASCADE;

COMMIT;
