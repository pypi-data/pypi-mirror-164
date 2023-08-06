# -*- coding: utf-8 -*-
# File: __init__.py

"""
Init file for deepdoctection package
"""

import os

from packaging import version

from .utils.file_utils import get_tf_version, pytorch_available, tf_available
from .utils.logger import logger

__version__ = 0.16

if not tf_available() and not pytorch_available():
    logger.info(
        "Neither Tensorflow or Pytorch are available. You will not be able to use any Deep Learning model from"
        "the library."
    )

# disable TF warnings for versions > 2.4.1
if tf_available():
    if version.parse(get_tf_version()) > version.parse("2.4.1"):
        os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
    try:
        import tensorflow.python.util.deprecation as deprecation  # type: ignore # pylint: disable=E0401,R0402

        deprecation._PRINT_DEPRECATION_WARNINGS = False  # pylint: disable=W0212
    except Exception:  # pylint: disable=W0703
        try:
            from tensorflow.python.util import deprecation  # type: ignore # pylint: disable=E0401

            deprecation._PRINT_DEPRECATION_WARNINGS = False  # pylint: disable=W0212
        except Exception:  # pylint: disable=W0703
            pass

# pylint: disable=wrong-import-position
from .analyzer import *
from .dataflow import *
from .datapoint import *
from .datasets import *
from .eval import *
from .extern import *
from .mapper import *
from .pipe import *
from .train import *
from .utils import *

# pylint: enable=wrong-import-position
