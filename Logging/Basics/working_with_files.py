import logging
# This is just the basics for the log handling using files

# Handles  basics.py
logging.basicConfig(filename="basics.log", level=logging.DEBUG)
logging.info("This is just for the testing")
logging.error("Imagine There's a error in the line: 6")
logging.warning("Imagine i trigger a warning")
logging.debug("Yes Yes Yes")
logging.critical("Yes this is a Jojo Reference.")

