# multicloud/platform.py

import sys
import os
import platform as _platform


def system_name():
    return _platform.system().lower()


def is_windows():
    return system_name() == "windows"


def is_linux():
    return system_name() == "linux"


def is_darwin():
    return system_name() == "darwin"


def is_ipad():
    """
    Detect iPad running Pythonista or Pyto
    """
    if not is_darwin():
        return False

    exe = sys.executable.lower()

    if "pythonista" in exe:
        return True
    if "pyto" in exe:
        return True
    if "PYTHONISTA" in os.environ:
        return True

    return False


def supports_cli():
    return True


def supports_tui():
    if is_ipad():
        return False
    if is_windows():
        return False
    return True


def supports_desktop_gui():
    return not is_ipad()
