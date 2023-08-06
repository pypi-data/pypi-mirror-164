from time import ctime

from tensorgenerator import __version__


def run():
    cur_time = ctime()
    text = f"""
    # torch version

    version {__version__} ({cur_time} +0800)
    """
    print(text)
