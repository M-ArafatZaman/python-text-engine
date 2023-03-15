import os
import sys

def clearScreen():
    """
    Clears the console
    """
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")