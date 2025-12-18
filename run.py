# multicloud/run.py

import vendor_init  # adds ./vendor to sys.path

from platform import (
    is_ipad,
    available_interfaces,
)


def choose_interface(modes):
    print("Available interfaces:")
    for i, mode in enumerate(modes, 1):
        print(f"{i}. {mode}")

    while True:
        try:
            choice = int(input("Select interface: "))
            if 1 <= choice <= len(modes):
                return modes[choice - 1]
        except ValueError:
            pass
        print("Invalid choice.")


def main():
    modes = available_interfaces()

    # iPad auto-launch GUI
    if is_ipad():
        from gui.ipad_app import start_ipad_gui
        start_ipad_gui()
        return

    # Desktop: let user choose
    selected = choose_interface(modes)

    if selected == "cli":
        from cli.app import run_cli
        run_cli([])
    elif selected == "tui":
        from tui.app import start_tui
        start_tui()
    elif selected == "desktop_gui":
        from gui.desktop_app import start_desktop_gui
        start_desktop_gui()
    else:
        print("Unknown interface selected.")


if __name__ == "__main__":
    main()
