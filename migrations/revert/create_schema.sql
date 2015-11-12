-- Revert cards:create_schema from pg

BEGIN;

DROP SCHEMA cards CASCADE;

COMMIT;
