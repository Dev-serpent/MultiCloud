from abc import ABC, abstractmethod
from typing import List


class CloudProvider(ABC):
    """
    Abstract base class for all cloud providers.
    """

    @abstractmethod
    def login(self, credentials):
        """
        Authenticate with the cloud provider.
        """
        pass

    @abstractmethod
    def upload(self, file_path: str, dest_filename: str) -> str:
        """
        Upload a file to the cloud.

        Args:
            file_path (str): The local path to the file to upload.
            dest_filename (str): The destination filename in the cloud.

        Returns:
            str: The public URL or identifier of the uploaded file.
        """
        pass

    @abstractmethod
    def download(self, file_id: str, dest_path: str):
        """
        Download a file from the cloud.

        Args:
            file_id (str): The identifier of the file to download.
            dest_path (str): The local path to save the downloaded file.
        """
        pass

    @abstractmethod
    def list_files(self) -> List[str]:
        """
        List all files in the cloud storage.

        Returns:
            List[str]: A list of file identifiers.
        """
        pass
