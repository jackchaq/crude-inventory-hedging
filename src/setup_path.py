import os
import sys


def add_project_root():  # noqa: E302
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    if root not in sys.path:
        sys.path.append(root)
