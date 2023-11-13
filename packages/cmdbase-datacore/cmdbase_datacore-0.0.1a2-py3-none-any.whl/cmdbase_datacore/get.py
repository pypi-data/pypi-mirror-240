"""
Make a custom HTTP GET request on the Datacore API.
"""
from argparse import ArgumentParser
from pprint import pprint
from .commons import Context


def add_arguments(parser: ArgumentParser):
    parser.add_argument('endpoint', help="API endpoint (example: /hosts).")
    parser.add_argument('--api-version', default=None, help="Use a specific API version (example: 2.0).")
    Context.add_argument(parser)


def handle(context: Context, endpoint: str, api_version: str = None):
    result = context.get_with_retries(endpoint, api_version=api_version)
    pprint(result, sort_dicts=False)
