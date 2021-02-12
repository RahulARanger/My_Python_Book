import logging
import sys

custom = logging.getLogger(__name__)
# create custom handler
custom_handler = logging.StreamHandler(sys.stdout)
custom_handler.setLevel(logging.DEBUG)

# add the handler
custom.addHandler(custom_handler)

custom.debug("This is a debug message")
custom.error("Another Error")

try:
    1/0
except Exception as e:
    custom.exception(e)
