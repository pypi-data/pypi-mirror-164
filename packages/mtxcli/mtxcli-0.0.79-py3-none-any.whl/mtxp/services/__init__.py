import os
import sys
import threading
import logging
from .clash import ClashService
from .tor import TorService
from .pf import PfService
logger = logging.getLogger(__name__)

def start_all_services():

    logger.info(f"start_all_services() {os.getpid()}")
    ClashService().start()
    TorService().start()
    PfService().start()
