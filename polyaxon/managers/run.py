# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import sys

from polyaxon.managers.base import BaseConfigManager
from polyaxon.schemas.api.experiment import ExperimentConfig
from polyaxon.utils.formatting import Printer


class RunManager(BaseConfigManager):
    """Manages run configuration .polyaxonrun file."""

    IS_GLOBAL = False
    IS_POLYAXON_DIR = True
    CONFIG_FILE_NAME = ".polyaxonrun"
    CONFIG = ExperimentConfig

    @classmethod
    def get_config_or_raise(cls):
        experiment = cls.get_config()
        if not experiment:
            Printer.print_error("No run uuid was provided.")
            sys.exit(1)

        return experiment
