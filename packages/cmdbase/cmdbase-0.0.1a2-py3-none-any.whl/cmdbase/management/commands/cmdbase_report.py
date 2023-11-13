import jsonc
import logging
from argparse import ArgumentParser
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from cmdbase.models import ReportOrigin
from cmdbase.reports import report_content, report_file

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Report item(s) to CMDBase."

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('content', nargs='+')
        parser.add_argument('--by', default='seeder')
        parser.add_argument('--origin', type=ReportOrigin, default=ReportOrigin.CODE)


    def handle(self, content: list[str], by: str, origin: ReportOrigin, **kwargs):
        by_user, created = get_user_model().objects.get_or_create(username=by)
        if created:
            logger.info(f"created user \"{by_user.get_username()}\"")


        def handle_single(content: str):
            if content.startswith(('[','{')) and content.endswith((']','}')):
                logger.info(f"report item: {content}")
                content = jsonc.loads(content)
                report_content(content, by=by_user, origin=origin)
            else:
                logger.info(f"report item from file: {content}")
                report_file(content, by=by_user, origin=origin)


        for single in content:
            handle_single(single)
