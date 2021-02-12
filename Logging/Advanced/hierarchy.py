import logging
import sys

custom1 = logging.getLogger("parent")

custom2 = custom1.getChild("child")
print(custom2.parent, custom2.propagate)  # returns some value

custom1_handler = logging.FileHandler("test1.log", "a")
custom2_handler = logging.StreamHandler(sys.stdout)

custom1.addHandler(custom1_handler)
custom2.addHandler(custom2_handler)

# print(custom1, custom2)

custom1.warning("This is a warning message given by the joseph.")

# This below warning will also be in filename since child propagates to its parent
custom2.warning("This is a warning message given by the jotaro.")
