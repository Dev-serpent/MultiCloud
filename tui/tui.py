import curses
from tui.screens import MainScreen, LoginScreen, CloudAccountsScreen
from core.api import (
    login,
    register_user,
    add_cloud_account,
    list_cloud_accounts,
    remove_cloud_account,
    backup_folder,
    restore_latest,
    list_providers,
    list_vault_files,
    vault_info
)
from cloud.gdrive_auth import get_gdrive_credentials


def main(stdscr):
    curses.curs_set(0)
    user = None
    password = None

    while True:
        if not user:
            login_screen = LoginScreen(stdscr)
            while True:
                login_screen.draw()
                key = stdscr.getch()
                res = login_screen.handle_input(key)
                if res:
                    username, password = res
                    try:
                        user = login(username, password)
                        if not user:
                            # TODO: Show error message
                            # For now, just break and retry
                            break
                        else:
                            break
                    except Exception as e:
                        # TODO: Show error message
                        break
            if not user:
                # TODO: Implement registration screen
                # For now, just exit
                return

        main_screen = MainScreen(stdscr, user)
        while True:
            main_screen.draw()
            key = stdscr.getch()
            action = main_screen.handle_input(key)

            if action == "Logout":
                user = None
                break
            elif action == "Backup Folder":
                # TODO: Implement backup screen
                pass
            elif action == "Restore Backup":
                # TODO: Implement restore screen
                pass
            elif action == "Cloud Accounts":
                cloud_accounts_screen = CloudAccountsScreen(stdscr, user, password)
                while True:
                    cloud_accounts_screen.draw()
                    key = stdscr.getch()
                    cloud_action = cloud_accounts_screen.handle_input(key)
                    if cloud_action == "Back":
                        break
                    elif cloud_action == "Add Account":
                        # TODO: Implement add account screen
                        pass
                    elif cloud_action == "List Accounts":
                        stdscr.clear()
                        stdscr.addstr(0, 2, "Cloud Accounts:")
                        accounts = list_cloud_accounts(user, password)
                        for i, acc in enumerate(accounts):
                            stdscr.addstr(2 + i, 4, f"- {acc.name} ({acc.provider})")
                        stdscr.getch()
                    elif cloud_action == "Remove Account":
                        # TODO: Implement remove account screen
                        pass
            elif action == "List Providers":
                stdscr.clear()
                stdscr.addstr(0, 2, "Available Providers:")
                providers = list_providers()
                for i, p in enumerate(providers):
                    stdscr.addstr(2 + i, 4, p)
                stdscr.getch()
            elif action == "List Vault Files":
                stdscr.clear()
                stdscr.addstr(0, 2, "Vault Files:")
                files = list_vault_files()
                for i, f in enumerate(files):
                    stdscr.addstr(2 + i, 4, f)
                stdscr.getch()
            elif action == "Vault Info":
                stdscr.clear()
                info = vault_info()
                stdscr.addstr(0, 2, "Vault Info:")
                stdscr.addstr(2, 4, f"Files: {info['file_count']}")
                stdscr.addstr(3, 4, f"Size: {info['total_size_bytes']} bytes")
                stdscr.getch()

        if not user:
            # User logged out, loop back to login
            continue
        else:
            # Exit if user is still logged in (e.g. from a menu option)
            break


def run_tui():
    curses.wrapper(main)


if __name__ == "__main__":
    run_tui()
