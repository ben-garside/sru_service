from sru.support.web import Response
from sru.support.data_process import encode
import logging
from . import main

log = logging.getLogger(__name__)


def restart(**kwargs):
    results = main.restart()
    return results