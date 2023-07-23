import logging

def getLogger():
    __logger__ = logging.getLogger("")
    __logger__.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s')


    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    __logger__.addHandler(console_handler)

    return __logger__