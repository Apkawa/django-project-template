# coding: utf-8
from __future__ import unicode_literals
from . import *

INSTALLED_APPS += [
    'debug_toolbar',
]

PROFILING = False

if PROFILING:
    MIDDLEWARE_CLASSES = [
                             'debug_toolbar.middleware.DebugToolbarMiddleware',
                         ] + MIDDLEWARE_CLASSES
else:
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
if PROFILING:
    DEBUG_TOOLBAR_PANELS.append('debug_toolbar.panels.profiling.ProfilingPanel')
