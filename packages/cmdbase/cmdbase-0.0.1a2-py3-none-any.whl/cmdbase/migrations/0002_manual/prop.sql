CREATE OR REPLACE FUNCTION cmdbase_prop_fullname_update() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
    WITH RECURSIVE cte AS (
        SELECT id AS id, parent_id, 0 AS ancestor_level, name
        FROM cmdbase_prop
        UNION ALL
        SELECT c.id, t.parent_id, c.ancestor_level + 1, t.name
        FROM cte c
        INNER JOIN cmdbase_prop t ON t.id = c.parent_id
    ),
    fullnames AS (
        SELECT id, string_agg(name, '.' ORDER BY ancestor_level DESC) AS fullname
        FROM cte
        GROUP BY id
    )
    UPDATE cmdbase_prop AS d
    SET fullname = s.fullname
    FROM fullnames s
    WHERE s.id = d.id;

    RETURN null;
END $$;


CREATE OR REPLACE TRIGGER cmdbase_prop_fullname_trigger AFTER INSERT OR UPDATE
ON cmdbase_prop FOR EACH STATEMENT WHEN (pg_trigger_depth() = 0)
EXECUTE FUNCTION cmdbase_prop_fullname_update();


-- ----------------------------------------------------------------------------
-- !reverse
--
DROP TRIGGER cmdbase_prop_fullname_trigger;
DROP FUNCTION cmdbase_prop_fullname_update;
