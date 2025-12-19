from typing import List
from cloud.base import CloudProvider


class WebDAVProvider(CloudProvider):
    """
    Cloud provider for WebDAV servers.
    """

    def __init__(self):
        self.client = None

    def login(self, credentials):
        """
        Authenticate with a WebDAV server.
        """
        # from webdav3.client import Client
        #
        # options = {
        #  'webdav_hostname': credentials['hostname'],
        #  'webdav_login':    credentials['login'],
        #  'webdav_password': credentials['password']
        # }
        # self.client = Client(options)
        print("Logging in to WebDAV (not implemented)")

    def upload(self, file_path: str, dest_filename: str) -> str:
        """
        Upload a file to a WebDAV server.
        """
        print(f"Uploading {file_path} to WebDAV as {dest_filename} (not implemented)")
        return f"webdav:///{dest_filename}"

    def download(self, file_id: str, dest_path: str):
        """
        Download a file from a WebDAV server.
        """
        print(f"Downloading {file_id} from WebDAV to {dest_path} (not implemented)")

    def list_files(self) -> List[str]:
        """
        List all files on a WebDAV server.
        """
        print("Listing files from WebDAV (not implemented)")
        return []
