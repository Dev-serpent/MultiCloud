from typing import List
from cloud.base import CloudProvider


class DropboxProvider(CloudProvider):
    """
    Cloud provider for Dropbox.
    """

    def __init__(self):
        self.dbx = None

    def login(self, credentials):
        """
        Authenticate with Dropbox using an access token.
        """
        # import dropbox
        # self.dbx = dropbox.Dropbox(credentials['access_token'])
        print("Logging in to Dropbox (not implemented)")

    def upload(self, file_path: str, dest_filename: str) -> str:
        """
        Upload a file to Dropbox.
        """
        print(f"Uploading {file_path} to Dropbox as {dest_filename} (not implemented)")
        return f"dropbox:///{dest_filename}"

    def download(self, file_id: str, dest_path: str):
        """
        Download a file from Dropbox.
        """
        print(f"Downloading {file_id} from Dropbox to {dest_path} (not implemented)")

    def list_files(self) -> List[str]:
        """
        List all files in the Dropbox app folder.
        """
        print("Listing files from Dropbox (not implemented)")
        return []
