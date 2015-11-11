-- Revert endpoint_test:one from pg

BEGIN;

DROP SCHEMA endpoint;

COMMIT;
