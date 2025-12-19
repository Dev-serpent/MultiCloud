import os
from typing import List, Optional

from core.backup import backup_folder as create_backup
from core.restore import restore_backup
from vault.vault import Vault
from core.cloud_manager import cloud_manager
from vault.user_manager import get_user_manager
from vault.models import User, CloudAccount
from core.logging import logger


# ---------------------------
# High-level API
# ---------------------------

def register_user(username: str, password: str) -> User:
    """
    Create a new user.
    """
    logger.info(f"Registering new user: {username}")
    user_manager = get_user_manager(password)
    user = user_manager.create_user(username, password)
    logger.info(f"User '{username}' registered successfully.")
    return user


def login(username: str, password: str) -> Optional[User]:
    """
    Authenticate a user.
    """
    logger.info(f"Attempting to log in user: {username}")
    user_manager = get_user_manager(password)
    user = user_manager.authenticate_user(username, password)
    if user:
        logger.info(f"User '{username}' logged in successfully.")
    else:
        logger.warning(f"Failed login attempt for user: {username}")
    return user


def add_cloud_account(user: User, password: str, account_name: str, provider: str, credentials: dict):
    """
    Add a cloud account to a user.
    """
    logger.info(f"Adding cloud account '{account_name}' for user '{user.username}'.")
    user_manager = get_user_manager(password)
    user_manager.add_cloud_account(user.username, account_name, provider, credentials)
    logger.info(f"Cloud account '{account_name}' added successfully.")


def list_cloud_accounts(user: User, password: str) -> List[CloudAccount]:
    """
    List all cloud accounts for a user.
    """
    logger.info(f"Listing cloud accounts for user '{user.username}'.")
    user_manager = get_user_manager(password)
    return user_manager.list_cloud_accounts(user.username)


def remove_cloud_account(user: User, password: str, account_name: str):
    """
    Remove a cloud account from a user.
    """
    logger.info(f"Removing cloud account '{account_name}' for user '{user.username}'.")
    user_manager = get_user_manager(password)
    user_manager.remove_cloud_account(user.username, account_name)
    logger.info(f"Cloud account '{account_name}' removed successfully.")


def backup_folder(user: User, folder_path: str, password: str) -> List[str]:
    """
    Create a backup of a folder and store it in the cloud.

    Returns:
        List of encrypted chunk filenames stored in vault
    """
    logger.info(f"Starting backup for user '{user.username}' of folder: {folder_path}")
    if not os.path.isdir(folder_path):
        logger.error(f"Folder not found: {folder_path}")
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    if not password:
        logger.error("Password cannot be empty")
        raise ValueError("Password cannot be empty")

    if not user.cloud_accounts:
        logger.error(f"User '{user.username}' has no cloud accounts configured.")
        raise ValueError("User has no cloud accounts configured")

    chunk_paths = create_backup(folder_path, password)
    logger.info(f"Created {len(chunk_paths)} chunks for backup.")

    # Distribute chunks across user's cloud accounts
    logger.info("Distributing chunks across cloud providers.")
    for i, chunk_path in enumerate(chunk_paths):
        cloud_account = user.cloud_accounts[i % len(user.cloud_accounts)]
        provider = cloud_manager.get_provider(cloud_account.provider)()
        logger.debug(f"Uploading chunk {chunk_path} to provider {cloud_account.provider}")
        provider.login(cloud_account.credentials)
        provider.upload(chunk_path, os.path.basename(chunk_path))

    logger.info("Backup complete.")
    return chunk_paths


def restore_latest(user: User, password: str, output_dir: str):
    """
    Restore the latest backup from the cloud.

    Args:
        user (User): The user to restore the backup for.
        password (str): The password to decrypt the backup.
        output_dir (str): The directory to restore the backup to.
    """
    logger.info(f"Starting restore for user '{user.username}' to folder: {output_dir}")
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    if not password:
        logger.error("Password cannot be empty")
        raise ValueError("Password cannot be empty")

    # TODO: Get the list of chunks from the cloud
    # For now, we'll assume the chunks are available locally
    # in the vault.
    logger.info("Restoring from local vault (cloud restore not implemented).")
    restore_backup(password, output_dir)
    logger.info("Restore complete.")


def list_providers() -> List[str]:
    """
    List all available cloud providers.
    """
    return cloud_manager.list_providers()


def list_vault_files() -> List[str]:
    """
    List all files currently stored in the vault.

    Returns:
        List of filenames in the vault.
    """
    vault = Vault()
    return vault.list_files()


def vault_info() -> dict:
    """
    Basic vault metadata (count + size)
    """
    vault = Vault()
    files = vault.list_files()

    total_size = 0
    for f in files:
        path = vault.get(f)
        if os.path.exists(path):
            total_size += os.path.getsize(path)

    return {
        "file_count": len(files),
        "total_size_bytes": total_size
    }
