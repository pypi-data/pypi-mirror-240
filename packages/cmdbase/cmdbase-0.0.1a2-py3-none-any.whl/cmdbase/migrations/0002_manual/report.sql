CREATE OR REPLACE VIEW cmdbase_report_detail AS
SELECT
	r.id
	,r.at
	,r.by_id
	,r.origin
	,(SELECT COUNT(*) FROM cmdbase_reportitem rx WHERE rx.report_id = r.id AND rx.item_id IS NOT NULL) AS item_count
	,(SELECT COUNT(*) FROM cmdbase_issue i WHERE i.on_type_id = (SELECT id FROM django_content_type dct WHERE app_label = 'cmdbase' AND model = 'report') AND i.on_id = r.id) AS issue_count
    ,ri.id AS root_reportitem_id
	,ri.item_id AS root_item_id
	,ri.action AS root_action
	,ri.data AS root_data
	,r.created
FROM cmdbase_report r
LEFT OUTER JOIN cmdbase_reportitem ri ON ri.report_id = r.id AND ri.path IS NULL


-- ----------------------------------------------------------------------------
-- !reverse
--
DROP VIEW cmdbase_report_detail;
