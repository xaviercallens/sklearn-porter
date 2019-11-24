# -*- coding: utf-8 -*-

from argparse import RawTextHelpFormatter, _SubParsersAction
from logging import DEBUG
from textwrap import dedent
from typing import Dict

# sklearn-porter
from sklearn_porter import Estimator, options
from sklearn_porter.cli.common import arg_debug, arg_help


def config(sub_parser: _SubParsersAction):
    header = 'The subcommand `show` lists all supported ' \
             'estimators and programming languages.'
    footer = dedent("""
        Examples:
          `porter show`
    """)

    parser = sub_parser.add_parser(
        'show',
        description=header,
        help='Show the supported estimators and programming languages.',
        epilog=footer,
        formatter_class=RawTextHelpFormatter,
        add_help=False,
    )
    for group in parser._action_groups:
        group.title = str(group.title).capitalize()

    for fn in (arg_debug, arg_help):
        fn(parser)

    parser.set_defaults(func=main)


def _get_qualname(obj: object):
    return obj.__class__.__module__ + '.' + obj.__class__.__qualname__


def main(args: Dict):
    if args.get('debug'):
        options['logging.level'] = DEBUG

    estimators = Estimator.classifiers() + Estimator.regressors()

    for e in estimators:
        print(e.__name__)