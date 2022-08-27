import os
import sys


def move_up():
    """Move two levels up (../../)"""
    dir_name = os.path.dirname(__file__)
    parent_dir = os.pardir
    join_path = os.path.join(dir_name, parent_dir)
    join_path2 = os.path.join(join_path, parent_dir)
    PROJECT_ROOT = os.path.abspath(join_path2)
    # print()
    # print(PROJECT_ROOT)
    # print()
    return sys.path.append(PROJECT_ROOT)


move_up()
