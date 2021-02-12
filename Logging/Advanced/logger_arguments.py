import logging
import sys

custom = logging.getLogger("Custom Logger")
custom_handler = logging.StreamHandler(sys.stdout)
custom.addHandler(custom_handler)
custom.setLevel(logging.INFO)

custom.info("This is a info message", stack_info=True)

custom.info("Rem Chan is the Best!!!", stacklevel=2)