CREATE OR REPLACE FUNCTION cmdbase_issuenature_get_or_create(_value text) RETURNS bigint LANGUAGE plpgsql AS $$
DECLARE
	_id bigint;
BEGIN
	_id := (SELECT id FROM cmdbase_issuenature WHERE value = _value);

	IF _id IS NULL THEN
		INSERT INTO cmdbase_issuenature AS d (value)
        VALUES (_value)
        ON CONFLICT (value)
        DO UPDATE SET id = d.id
        RETURNING id INTO _id;
    END IF;

	RETURN _id;
END $$;


-- ----------------------------------------------------------------------------
-- !reverse
--
DROP FUNCTION cmdbase_issuenature_get_or_create;
