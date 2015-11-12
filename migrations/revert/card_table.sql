-- Revert cards:card_table from pg

BEGIN;

DROP TABLE card CASCADE;

COMMIT;
