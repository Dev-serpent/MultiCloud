import argparse
import getpass
from typing import List
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
from cloud.gdrive_auth import get_gdrive_credentials


def main(argv: List[str] = None):
    parser = argparse.ArgumentParser(
        prog="multicloud",
        description="MultiCloud local backup system"
    )

    sub = parser.add_subparsers(dest="cmd")

    # Register command
    reg = sub.add_parser("register", help="Register a new user")
    reg.add_argument("username")

    # Login command
    log = sub.add_parser("login", help="Login as a user")
    log.add_argument("username")

    # Cloud-add command
    ca = sub.add_parser("cloud-add", help="Add a cloud account")
    ca.add_argument("account_name")
    ca.add_argument("provider")
    ca.add_argument("-u", "--username", required=True)

    # Cloud-list command
    cl = sub.add_parser("cloud-list", help="List cloud accounts")
    cl.add_argument("-u", "--username", required=True)

    # Cloud-remove command
    cr = sub.add_parser("cloud-remove", help="Remove a cloud account")
    cr.add_argument("account_name")
    cr.add_argument("-u", "--username", required=True)

    # Backup command
    b = sub.add_parser("backup", help="Backup a folder")
    b.add_argument("folder")
    b.add_argument("-u", "--username", required=True)
    b.add_argument("-p", "--providers", required=True, nargs="+", help="Cloud providers to use")

    # Restore command
    r = sub.add_parser("restore", help="Restore latest backup")
    r.add_argument("output")
    r.add_argument("-u", "--username", required=True)

    # List providers command
    sub.add_parser("list-providers", help="List available cloud providers")

    sub.add_parser("list", help="List vault files")
    sub.add_parser("info", help="Vault info")

    args = parser.parse_args(argv)

    try:
        if args.cmd == "register":
            password = getpass.getpass("Enter password: ")
            password_confirm = getpass.getpass("Confirm password: ")
            if password != password_confirm:
                print("Passwords do not match.")
                return
            register_user(args.username, password)
            print(f"User '{args.username}' registered successfully.")

        elif args.cmd == "login":
            password = getpass.getpass("Enter password: ")
            user = login(args.username, password)
            if user:
                print(f"Logged in as '{args.username}'.")
            else:
                print("Login failed.")

        elif args.cmd == "cloud-add":
            password = getpass.getpass("Enter password: ")
            user = login(args.username, password)
            if not user:
                print("Login failed.")
                return
            
            credentials = {}
            if args.provider == "aws":
                credentials["access_key"] = input("Enter AWS Access Key ID: ")
                credentials["secret_key"] = getpass.getpass("Enter AWS Secret Access Key: ")
            elif args.provider == "dropbox":
                credentials["access_token"] = getpass.getpass("Enter Dropbox Access Token: ")
            elif args.provider == "gdrive":
                credentials = get_gdrive_credentials()
            # TODO: Add other providers
            
            add_cloud_account(user, password, args.account_name, args.provider, credentials)
            print(f"Cloud account '{args.account_name}' added successfully.")

        elif args.cmd == "cloud-list":
            password = getpass.getpass("Enter password: ")
            user = login(args.username, password)
            if not user:
                print("Login failed.")
                return
            accounts = list_cloud_accounts(user, password)
            if accounts:
                print("Cloud accounts:")
                for acc in accounts:
                    print(f"- {acc.name} ({acc.provider})")
            else:
                print("No cloud accounts configured.")

        elif args.cmd == "cloud-remove":
            password = getpass.getpass("Enter password: ")
            user = login(args.username, password)
            if not user:
                print("Login failed.")
                return
            remove_cloud_account(user, password, args.account_name)
            print(f"Cloud account '{args.account_name}' removed successfully.")

        elif args.cmd == "backup":
            password = getpass.getpass("Enter password: ")
            user = login(args.username, password)
            if not user:
                print("Login failed.")
                return
            files = backup_folder(user, args.folder, password)
            print("Backup complete:")
            for f in files:
                print(" ", f)

        elif args.cmd == "restore":
            password = getpass.getpass("Enter password: ")
            user = login(args.username, password)
            if not user:
                print("Login failed.")
                return
            restore_latest(user, password, args.output)
            print("Restore complete.")

        elif args.cmd == "list-providers":
            print("Available providers:")
            for p in list_providers():
                print(f"- {p}")

        elif args.cmd == "list":
            for f in list_vault_files():
                print(f)

        elif args.cmd == "info":
            info = vault_info()
            print(f"Files: {info['file_count']}")
            print(f"Size : {info['total_size_bytes']} bytes")

        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
