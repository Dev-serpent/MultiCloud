import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, Listbox, Toplevel
from core.api import (
    register_user,
    login,
    add_cloud_account,
    list_cloud_accounts,
    remove_cloud_account,
    backup_folder,
    restore_latest,
    list_providers,
    list_vault_files,
    vault_info
)
from vault.models import User
from cloud.gdrive_auth import get_gdrive_credentials


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x150")
        self.user = None
        self.password = None

        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        self.password = self.password_entry.get()
        try:
            self.user = login(username, self.password)
            if self.user:
                self.root.destroy()
            else:
                messagebox.showerror("Error", "Login failed.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        try:
            register_user(username, password)
            messagebox.showinfo("Success", "User registered successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()
        return self.user, self.password


class CloudAccountsWindow:
    def __init__(self, parent, user, password):
        self.parent = parent
        self.user = user
        self.password = password
        self.win = Toplevel(parent)
        self.win.title("Cloud Accounts")

        self.listbox = Listbox(self.win)
        self.listbox.pack(pady=10)
        self.refresh_accounts()

        tk.Button(self.win, text="Add Account", command=self.add_account).pack(pady=5)
        tk.Button(self.win, text="Remove Account", command=self.remove_account).pack(pady=5)

    def refresh_accounts(self):
        self.listbox.delete(0, tk.END)
        accounts = list_cloud_accounts(self.user, self.password)
        for acc in accounts:
            self.listbox.insert(tk.END, f"{acc.name} ({acc.provider})")

    def add_account(self):
        # TODO: Create a more sophisticated UI for this
        account_name = simpledialog.askstring("Add Account", "Enter account name:")
        if not account_name:
            return
        provider = simpledialog.askstring("Add Account", "Enter provider (e.g., aws, gdrive):")
        if not provider:
            return

        credentials = {}
        if provider == "gdrive":
            try:
                credentials = get_gdrive_credentials()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to get Google Drive credentials: {e}")
                return
        else:
            # For other providers, ask for credentials manually
            # This is a simplified example
            messagebox.showinfo("Credentials", "Please enter credentials in the console.")
            if provider == "aws":
                credentials["access_key"] = input("Enter AWS Access Key ID: ")
                credentials["secret_key"] = getpass.getpass("Enter AWS Secret Access Key: ")
            elif provider == "dropbox":
                credentials["access_token"] = getpass.getpass("Enter Dropbox Access Token: ")

        try:
            add_cloud_account(self.user, self.password, account_name, provider, credentials)
            self.refresh_accounts()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def remove_account(self):
        selected = self.listbox.get(self.listbox.curselection())
        if not selected:
            return
        account_name = selected.split(" ")[0]
        try:
            remove_cloud_account(self.user, self.password, account_name)
            self.refresh_accounts()
        except Exception as e:
            messagebox.showerror("Error", str(e))


class DesktopGUI:
    def __init__(self, user: User, password: str):
        self.user = user
        self.password = password
        self.root = tk.Tk()
        self.root.title(f"MultiCloud - {user.username}")
        self.root.geometry("420x520")

        tk.Label(self.root, text="MultiCloud", font=("Arial", 20)).pack(pady=12)

        tk.Button(self.root, text="Create Backup", width=30, command=self.create_backup).pack(pady=6)
        tk.Button(self.root, text="Restore Backup", width=30, command=self.restore_backup).pack(pady=6)
        tk.Button(self.root, text="Cloud Accounts", width=30, command=self.open_cloud_accounts).pack(pady=6)
        tk.Button(self.root, text="List Providers", width=30, command=self.list_providers).pack(pady=6)
        tk.Button(self.root, text="List Vault Files", width=30, command=self.list_vault_files).pack(pady=6)
        tk.Button(self.root, text="Vault Info", width=30, command=self.vault_info).pack(pady=6)

        tk.Button(self.root, text="Exit", width=30, command=self.root.quit).pack(pady=20)

    def open_cloud_accounts(self):
        CloudAccountsWindow(self.root, self.user, self.password)

    def create_backup(self):
        src = filedialog.askdirectory(title="Select folder to back up")
        if not src:
            return
        
        # TODO: Add provider selection UI
        providers = [acc.provider for acc in self.user.cloud_accounts]
        if not providers:
            messagebox.showerror("Error", "No cloud accounts configured for this user.")
            return

        try:
            backup_folder(self.user, src, self.password)
            messagebox.showinfo("Success", "Backup created successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def restore_backup(self):
        dest = filedialog.askdirectory(title="Select restore destination")
        if not dest:
            return
            
        try:
            restore_latest(self.user, self.password, dest)
            messagebox.showinfo("Success", "Backup restored successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def list_providers(self):
        providers = list_providers()
        messagebox.showinfo("Providers", "\n".join(providers))

    def list_vault_files(self):
        files = list_vault_files()
        messagebox.showinfo("Vault Files", "\n".join(files))

    def vault_info(self):
        info = vault_info()
        messagebox.showinfo("Vault Info", f"Files: {info['file_count']}\nSize: {info['total_size_bytes']} bytes")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    login_root = tk.Tk()
    login_window = LoginWindow(login_root)
    user, password = login_window.run()

    if user:
        gui = DesktopGUI(user, password)
        gui.run()
