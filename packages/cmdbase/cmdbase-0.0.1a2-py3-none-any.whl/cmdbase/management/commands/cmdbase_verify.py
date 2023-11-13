import logging
from argparse import ArgumentParser
from django.core.management import BaseCommand
from django.db import connection
from cmdbase.issues import IssueError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Verify consistency of CMDBase data."
    # TODO:
    # - List missing relations
    # - List undefined or misused properties
    # - List non-unique item names

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('--repair', '-r', action='store_true', help="Try to repair if possible.")


    def handle(self, repair: bool, **kwargs):
        self.verify_duplicate_item_slug()


    def verify_duplicate_item_slug(self):
        logger.info(f"search duplicate item slugs")

        with connection.cursor() as cursor:
            cursor.execute("""
        WITH non_unique_slugs AS (
            SELECT
                s.slug
                ,json_object_agg(s.category_name, s.item_name) AS categories
            FROM (
                SELECT
                    i.slug
                    ,c.name AS category_name
                    ,i.name AS item_name
                FROM (
                    SELECT
                        i.slug
                        ,i.category_id
                        ,i.name
                        ,count(*) OVER (PARTITION BY i.slug) AS rowc
                    FROM cmdbase_item i
                ) i
                LEFT OUTER JOIN cmdbase_category c On c.id = i.category_id
                WHERE i.rowc > 1
            ) s
            GROUP BY s.slug
        )
        INSERT INTO cmdbase_issue (nature_id, nature_args, on_id, on_type_id, context)
        SELECT cmdbase_issuenature_get_or_create(%s), json_build_object('slug', s.slug), i.id, (SELECT id FROM django_content_type WHERE app_label = 'cmdbase' AND model = 'item'), categories
        FROM non_unique_slugs s
        INNER JOIN cmdbase_item i ON i.slug = s.slug
        ON CONFLICT (nature_id, nature_args, on_id, on_type_id)
        DO UPDATE SET updated = NOW()
        """, [IssueError.DUPLICATE_ITEM_SLUG])
            
            if cursor.rowcount:
                logger.warning(f"duplicate item slugs: {cursor.rowcount}")
