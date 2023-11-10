import sys
import os
import platform
import importlib.util

print("Welcome to Seeker!", flush=True)

# Get the major and minor Python version
py_version = f"{sys.version_info.major}{sys.version_info.minor}"

# Get the operating system
os_name = platform.system().lower()

def __bootstrap__():
   global __bootstrap__, __loader__, __file__
   import sys, pkg_resources, imp
   so_file = os.path.join(os.path.dirname(__file__),f"seeker.1.0.0.cpython-{py_version}-{os_name}.so")
   print("loading .so from", so_file)
   spec = importlib.util.spec_from_file_location("seeker", so_file)
   mylib = importlib.util.module_from_spec(spec)
   spec.loader.exec_module(mylib)
#   __file__ = pkg_resources.resource_filename(__name__,f"seeker.0.0.1.cpython-{py_version}-{os_name}.so")
#   __loader__ = None; del __bootstrap__, __loader__
#   imp.load_dynamic(__name__,__file__)
__bootstrap__()

