CREATE OR REPLACE VIEW cmdbase_categoryancestor AS
WITH RECURSIVE cte AS (
    SELECT id AS descendant_id, name AS descendant_name, slug AS descendant_slug, parent_id, 0 AS depth, id AS ancestor_id, name AS ancestor_name, slug AS ancestor_slug
    FROM cmdbase_category
    UNION ALL
    SELECT c.descendant_id, c.descendant_name, c.descendant_slug, t.parent_id, c.depth + 1, t.id, t.name, t.slug
    FROM cte c
    INNER JOIN cmdbase_category t ON t.id = c.parent_id
)
SELECT
    descendant_id * 1000 + depth AS id
	,descendant_id
	,descendant_name
	,descendant_slug
	,depth
	,ancestor_id
	,ancestor_name
	,ancestor_slug
FROM cte
ORDER BY descendant_name, depth DESC;


CREATE OR REPLACE VIEW cmdbase_categoryprop AS
--
-- List of configured props for each category, including parent category props.
--
SELECT
    category_id * 1000000000 + prop_id AS id
	,category_id
	,category_name
	,category_slug
	,prop_id
    ,prop_fullname
	,prop_category_id
	,prop_category_name
    ,prop_category_slug
    ,prop_name
    ,prop_parent_id
    ,prop_parent_name
    ,prop_parent_fullname
    ,prop_nature
    ,prop_ordinal
    ,prop_unit
    ,prop_index
    ,prop_index_with
    ,prop_search
    ,prop_help
FROM
	(SELECT
		c.descendant_id AS category_id
		,c.descendant_name AS category_name
		,c.descendant_slug AS category_slug
		,row_number() OVER (PARTITION BY c.descendant_id, p.fullname ORDER BY c.depth) AS rown
		,p.id AS prop_id
	    ,p.fullname AS prop_fullname
		,c.ancestor_id AS prop_category_id
		,c.ancestor_name AS prop_category_name
		,c.ancestor_slug AS prop_category_slug
	    ,p.name AS prop_name
	    ,p.parent_id AS prop_parent_id
	    ,pa.name AS prop_parent_name
	    ,pa.fullname AS prop_parent_fullname
	    ,p.ordinal AS prop_ordinal
	    ,p.nature AS prop_nature
	    ,p.unit AS prop_unit
	    ,p.index AS prop_index
	    ,p.index_with AS prop_index_with
	    ,p.search AS prop_search
	    ,p.help AS prop_help
	FROM cmdbase_categoryancestor c
	INNER JOIN cmdbase_prop p ON p.category_id = c.ancestor_id
	LEFT OUTER JOIN cmdbase_prop pa ON pa.id = p.parent_id
	) s
WHERE rown = 1
ORDER BY category_name, prop_parent_fullname NULLS FIRST, prop_ordinal, prop_fullname;


-- ----------------------------------------------------------------------------
-- !reverse
--
DROP VIEW cmdbase_categoryprop;
DROP VIEW cmdbase_categoryancestor;
