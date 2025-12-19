import curses

class Screen:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def draw(self):
        pass

    def handle_input(self, key):
        pass


class MainScreen(Screen):
    def __init__(self, stdscr, user):
        super().__init__(stdscr)
        self.user = user
        self.options = [
            "Backup Folder",
            "Restore Backup",
            "Cloud Accounts",
            "List Providers",
            "List Vault Files",
            "Vault Info",
            "Logout"
        ]
        self.idx = 0

    def draw(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 2, f"MultiCloud TUI - Logged in as {self.user.username}", curses.A_BOLD)

        for i, opt in enumerate(self.options):
            mode = curses.A_REVERSE if i == self.idx else curses.A_NORMAL
            self.stdscr.addstr(2 + i, 4, opt, mode)

    def handle_input(self, key):
        if key == curses.KEY_UP and self.idx > 0:
            self.idx -= 1
        elif key == curses.KEY_DOWN and self.idx < len(self.options) - 1:
            self.idx += 1
        elif key in (10, 13):
            return self.options[self.idx]
        return None


class CloudAccountsScreen(Screen):
    def __init__(self, stdscr, user, password):
        super().__init__(stdscr)
        self.user = user
        self.password = password
        self.options = ["Add Account", "List Accounts", "Remove Account", "Back"]
        self.idx = 0

    def draw(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 2, "Cloud Accounts", curses.A_BOLD)

        for i, opt in enumerate(self.options):
            mode = curses.A_REVERSE if i == self.idx else curses.A_NORMAL
            self.stdscr.addstr(2 + i, 4, opt, mode)

    def handle_input(self, key):
        if key == curses.KEY_UP and self.idx > 0:
            self.idx -= 1
        elif key == curses.KEY_DOWN and self.idx < len(self.options) - 1:
            self.idx += 1
        elif key in (10, 13):
            return self.options[self.idx]
        return None


class LoginScreen(Screen):
    def __init__(self, stdscr):
        super().__init__(stdscr)
        self.username = ""
        self.password = ""
        self.active_field = 0  # 0 for username, 1 for password

    def draw(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 2, "Login", curses.A_BOLD)
        self.stdscr.addstr(2, 4, "Username: ")
        self.stdscr.addstr(3, 4, "Password: ")
        self.stdscr.addstr(2, 14, self.username)
        self.stdscr.addstr(3, 14, "*" * len(self.password))

    def handle_input(self, key):
        if key == curses.KEY_UP:
            self.active_field = 0
        elif key == curses.KEY_DOWN:
            self.active_field = 1
        elif key == 10: # Enter
            return self.username, self.password
        elif key == curses.KEY_BACKSPACE or key == 127:
            if self.active_field == 0:
                self.username = self.username[:-1]
            else:
                self.password = self.password[:-1]
        else:
            if self.active_field == 0:
                self.username += chr(key)
            else:
                self.password += chr(key)
        return None