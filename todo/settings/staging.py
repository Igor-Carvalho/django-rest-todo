"""Configurações de pré-produção."""

from .base import *

# Security
DEBUG = False
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

REST_FRAMEWORK = REST_FRAMEWORK.copy()
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = ('rest_framework.renderers.JSONRenderer',)
