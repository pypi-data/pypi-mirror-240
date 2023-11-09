import operator
import re

import pendulum
import web
from mf import discover_post_type
from web import tx

__all__ = ["tx", "operator", "discover_post_type", "post_mkdn", "re", "pendulum"]


def post_mkdn(content):
    return web.mkdn(content)  # XXX , globals=micropub.markdown_globals)
