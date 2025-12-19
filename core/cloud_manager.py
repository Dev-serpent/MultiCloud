import pkgutil
import inspect
from typing import Dict, Type
from cloud.base import CloudProvider
import cloud as providers


class CloudManager:
    """
    Manages all available cloud providers.
    """

    def __init__(self):
        self.providers: Dict[str, Type[CloudProvider]] = {}
        self.load_providers()

    def load_providers(self):
        """
        Dynamically load all cloud providers from the providers package.
        """
        for _, name, _ in pkgutil.iter_modules(providers.__path__):
            module = __import__(f"cloud.{name}", fromlist=["*"])
            for item_name, item in inspect.getmembers(module, inspect.isclass):
                if issubclass(item, CloudProvider) and item is not CloudProvider:
                    self.providers[name] = item

    def get_provider(self, name: str) -> Type[CloudProvider]:
        """
        Get a cloud provider by name.
        """
        provider = self.providers.get(name)
        if not provider:
            raise ValueError(f"Provider not found: {name}")
        return provider

    def list_providers(self) -> list[str]:
        """
        List the names of all available providers.
        """
        return list(self.providers.keys())


cloud_manager = CloudManager()
