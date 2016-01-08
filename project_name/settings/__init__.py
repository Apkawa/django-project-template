# coding: utf-8
from __future__ import unicode_literals

from .base import *

try:
    from .local_settings import *
except ImportError:
    pass


if DEBUG:
    from .debug_toolbar import *

