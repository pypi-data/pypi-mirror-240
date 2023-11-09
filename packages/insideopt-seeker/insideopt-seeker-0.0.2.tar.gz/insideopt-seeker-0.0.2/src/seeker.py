import sys
import os
import platform
import importlib.util

# Get the major and minor Python version
py_version = f"{sys.version_info.major}{sys.version_info.minor}"

# Get the operating system
os_name = platform.system().lower()

def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp
   __file__ = pkg_resources.resource_filename(__name__,f"seeker.0.0.1.cpython-{py_version}-{os_name}.so")
   __loader__ = None; del __bootstrap__, __loader__
   imp.load_dynamic(__name__,__file__)
__bootstrap__()
