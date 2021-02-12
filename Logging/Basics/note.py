import logging

# This is the disadvantage of the basic log handling


def log_test1():
    logging.basicConfig(filename="test1.log", filemode="w")
    logging.warning("logged test1.log")


def log_test2():
    logging.basicConfig(filename="test2.log", filemode="w")
    logging.warning("logged test2.log")


log_test2()
log_test1()
# both this logs will be stored in the first file i.e here test2.log
