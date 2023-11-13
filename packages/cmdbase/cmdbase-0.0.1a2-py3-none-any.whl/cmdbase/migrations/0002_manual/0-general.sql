CREATE EXTENSION unaccent;

CREATE OR REPLACE FUNCTION slugify(input text) RETURNS text LANGUAGE sql STRICT IMMUTABLE AS $$
    -- Normalize the string: replace diacritics by standard characters, lower the string, etc
    WITH "step1" AS (
        SELECT lower(unaccent(input)) AS value
    )
    -- Remove special characters
    ,"step2" AS (
        SELECT regexp_replace(value, '[^a-z0-9\s\-]', '', 'g') AS value
        FROM "step1"
    )
    -- Replace spaces and successive separators by a single separator
    ,"step3" AS (
        SELECT regexp_replace(value, '[\s\-]+', '-', 'g') AS value
        FROM "step2"
    )
    -- Strips separator
    SELECT regexp_replace(regexp_replace(value, '\-+$', ''), '^\-+', '') AS value
    FROM "step3";
$$;
--TODO: veririfer quer null => null


-- ----------------------------------------------------------------------------
-- !reverse
--
DROP FUNCTION slugify;
DROP EXTENSION unaccent;
