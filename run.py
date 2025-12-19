# multicloud/run.py

import argparse
import sys
import vendor_init  # adds ./vendor to sys.path
import tkinter as tk # Import tkinter here

from plat import (
    is_ipad,
)


def main():
    parser = argparse.ArgumentParser(
        prog="multicloud",
        description="MultiCloud local backup system"
    )

    parser.add_argument(
        "interface",
        nargs="?",
        default="auto",
        help="Specify the interface to run: cli, tui, gui, or auto (default)"
    )

    args, remaining_args = parser.parse_known_args()

    if is_ipad():
        from gui.gui_ipad import iPadGUI
        iPadGUI().run()
        return

    if args.interface == "cli":
        from cli.cli import main as cli_main
        cli_main(remaining_args)
    elif args.interface == "tui":
        from tui.tui import run_tui
        run_tui()
    elif args.interface == "gui":
        from gui.gui_desktop import DesktopGUI, LoginWindow
        login_root = tk.Tk()
        login_window = LoginWindow(login_root)
        user = login_window.run()

        if user:
            gui = DesktopGUI(user)
            gui.run()
    elif args.interface == "auto":
        # Default to GUI for desktop if not iPad
        from gui.gui_desktop import DesktopGUI, LoginWindow
        login_root = tk.Tk()
        login_window = LoginWindow(login_root)
        user = login_window.run()

        if user:
            gui = DesktopGUI(user)
            gui.run()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
