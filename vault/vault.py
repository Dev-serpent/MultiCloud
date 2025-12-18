from vault.store import save_vault, load_vault
from vault.models import CloudAccount


class Vault:
    def __init__(self, password: str):
        self.password = password
        self.data = load_vault(password)

        if "accounts" not in self.data:
            self.data["accounts"] = []

    def add_account(self, account: CloudAccount):
        self.data["accounts"].append(account.__dict__)
        save_vault(self.data, self.password)

    def list_accounts(self):
        return self.data.get("accounts", [])

    def get_account(self, name: str):
        for acc in self.data.get("accounts", []):
            if acc["name"] == name:
                return acc
        return None
