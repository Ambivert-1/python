# Import the importlib module, which provides functions to import and reload modules dynamically
import importlib
# Dynamically import the hello module using importlib
importlib.import_module("hello")

import hello
importlib.reload(hello)
