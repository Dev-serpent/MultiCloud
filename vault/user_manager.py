from typing import Optional, List

from vault.models import User, CloudAccount
from vault.store import load_vault, save_vault
from vault.auth import hash_password, verify_password


class UserManager:
    """
    Manages users in the vault.
    """

    def __init__(self, password: str):
        self.password = password
        self.vault_data = load_vault(password)
        self.users = self.vault_data.get("users", {})

    def save(self):
        """
        Save the user data to the vault.
        """
        self.vault_data["users"] = self.users
        save_vault(self.vault_data, self.password)

    def create_user(self, username: str, password: str) -> User:
        """
        Create a new user.
        """
        if username in self.users:
            raise ValueError(f"User already exists: {username}")

        password_hash = hash_password(password)
        user = User(username=username, password_hash=password_hash)
        self.users[username] = user.__dict__
        self.save()
        return user

    def get_user(self, username: str) -> Optional[User]:
        """
        Get a user by username.
        """
        user_data = self.users.get(username)
        if user_data:
            # Manually deserialize cloud_accounts
            user_data['cloud_accounts'] = [CloudAccount(**acc) for acc in user_data.get('cloud_accounts', [])]
            return User(**user_data)
        return None

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """
        Authenticate a user.
        """
        user = self.get_user(username)
        if user and verify_password(user.password_hash, password):
            return user
        return None

    def add_cloud_account(self, username: str, account_name: str, provider: str, credentials: dict):
        """
        Add a cloud account to a user.
        """
        user = self.get_user(username)
        if not user:
            raise ValueError(f"User not found: {username}")

        for acc in user.cloud_accounts:
            if acc.name == account_name:
                raise ValueError(f"Cloud account already exists: {account_name}")

        cloud_account = CloudAccount(name=account_name, provider=provider, credentials=credentials)
        user.cloud_accounts.append(cloud_account)
        self.users[username] = user.__dict__
        self.save()

    def list_cloud_accounts(self, username: str) -> List[CloudAccount]:
        """
        List all cloud accounts for a user.
        """
        user = self.get_user(username)
        if not user:
            raise ValueError(f"User not found: {username}")
        return user.cloud_accounts

    def remove_cloud_account(self, username: str, account_name: str):
        """
        Remove a cloud account from a user.
        """
        user = self.get_user(username)
        if not user:
            raise ValueError(f"User not found: {username}")

        user.cloud_accounts = [acc for acc in user.cloud_accounts if acc.name != account_name]
        self.users[username] = user.__dict__
        self.save()


def get_user_manager(password: str) -> UserManager:
    """
    Get a UserManager instance.
    """
    return UserManager(password)
