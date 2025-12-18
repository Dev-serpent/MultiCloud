import argparse
import getpass
import sys

from core.backup import backup_folder
from core.restore import restore_backup
from vault.vault import Vault
from vault.models import CloudAccount


def cmd_backup(args):
    password = getpass.getpass("Vault password: ")
    backup_folder(args.folder, password=password)


def cmd_restore(args):
    password = getpass.getpass("Vault password: ")
    restore_backup(args.chunks, password=password, output_dir=args.output)


def cmd_vault_add(args):
    password = getpass.getpass("Vault password: ")
    vault = Vault(password)

    account = CloudAccount(
        name=args.name,
        provider=args.provider,
        access_key=args.access_key,
        secret_key=args.secret_key,
    )

    vault.add_account(account)
    print(f"Account '{args.name}' added.")


def cmd_vault_list(args):
    password = getpass.getpass("Vault password: ")
    vault = Vault(password)

    accounts = vault.list_accounts()
    if not accounts:
        print("No accounts stored.")
        return

    for acc in accounts:
        print(f"- {acc['name']} ({acc['provider']})")


def build_parser():
    parser = argparse.ArgumentParser(
        prog="multicloud",
        description="MultiCloud secure multi-provider backup tool",
    )

    sub = parser.add_subparsers(dest="command")

    # backup
    p_backup = sub.add_parser("backup", help="Backup a folder")
    p_backup.add_argument("folder", help="Folder to back up")
    p_backup.set_defaults(func=cmd_backup)

    # restore
    p_restore = sub.add_parser("restore", help="Restore from chunks")
    p_restore.add_argument("output", help="Output directory")
    p_restore.add_argument("chunks", nargs="+", help="Chunk files")
    p_restore.set_defaults(func=cmd_restore)

    # vault add
    p_vault_add = sub.add_parser("vault-add", help="Add cloud account")
    p_vault_add.add_argument("--name", required=True)
    p_vault_add.add_argument("--provider", required=True)
    p_vault_add.add_argument("--access-key", required=True)
    p_vault_add.add_argument("--secret-key", required=True)
    p_vault_add.set_defaults(func=cmd_vault_add)

    # vault list
    p_vault_list = sub.add_parser("vault-list", help="List stored accounts")
    p_vault_list.set_defaults(func=cmd_vault_list)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
