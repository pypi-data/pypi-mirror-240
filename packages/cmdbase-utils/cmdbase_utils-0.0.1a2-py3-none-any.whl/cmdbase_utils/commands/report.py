"""
Report item(s) to CMDBase.
"""
import logging
import jsonc
from argparse import ArgumentParser
from zut import skip_bom
from ..bases import BaseContext

logger = logging.getLogger(__name__)


def add_arguments(parser: ArgumentParser):
    parser.add_argument('content', nargs='+')


def handle(context: BaseContext, content: list[str]):
    for single in content:
        handle_single(context, single)


def handle_single(context: BaseContext, content: str):
    if content.startswith(('[','{')) and content.endswith((']','}')):
        logger.info(f"report item: {content}")
        data = jsonc.loads(content)
    else:
        logger.info(f"report item from file: {content}")
        with open(content, 'r', encoding='utf-8') as fp:
            skip_bom(fp)
            data = jsonc.load(fp)
            
    context.cmdbase_apiclient.report(data)
