# -*- coding: utf-8 -*-
import os
import sys

# =======

# Set FITPACK_DIR to local fitpack root directory.
#FITPACK_DIR = r"/home/avp5627/GIT/fitpack"
FITPACK_DIR = r"/home/avp5627/GIT/jam3d"


# =======

# Check that FITPACK_DIR points to a real place.
if not os.path.exists(FITPACK_DIR):
    raise RuntimeError("Change FITPACK_DIR to the fitpack root directory.")

# Add the FITPACK environmental variable.
if "FITPACK" not in os.environ:
    os.environ["FITPACK"] = FITPACK_DIR

# Add FITPACK_DIR to the PYTHONPATH.
if FITPACK_DIR not in sys.path:
    sys.path.append(FITPACK_DIR)

# Let this module be used like the fitpack package.
__path__ = [FITPACK_DIR]
