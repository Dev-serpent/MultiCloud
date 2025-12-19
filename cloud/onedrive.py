from typing import List
from cloud.base import CloudProvider


class OneDriveProvider(CloudProvider):
    """
    Cloud provider for Microsoft OneDrive.
    """

    def __init__(self):
        self.client = None

    def login(self, credentials):
        """
        Authenticate with OneDrive using OAuth 2.0 credentials.
        """
        # import onedrivesdk
        # from onedrivesdk.helpers import GetAuthCodeServer
        #
        # http_provider = onedrivesdk.HttpProvider()
        # auth_provider = onedrivesdk.AuthProvider(
        #     http_provider=http_provider,
        #     client_id=credentials['client_id'],
        #     scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite'])
        #
        # # This is a bit more complex, requires user interaction
        # auth_url = auth_provider.get_auth_url(credentials['redirect_uri'])
        # code = GetAuthCodeServer.get_auth_code(auth_url, credentials['redirect_uri'])
        # auth_provider.authenticate(code, credentials['redirect_uri'], credentials['client_secret'])
        # self.client = onedrivesdk.OneDriveClient(auth_url, auth_provider, http_provider)
        print("Logging in to OneDrive (not implemented)")

    def upload(self, file_path: str, dest_filename: str) -> str:
        """
        Upload a file to OneDrive.
        """
        print(f"Uploading {file_path} to OneDrive as {dest_filename} (not implemented)")
        return f"onedrive:///{dest_filename}"

    def download(self, file_id: str, dest_path: str):
        """
        Download a file from OneDrive.
        """
        print(f"Downloading {file_id} from OneDrive to {dest_path} (not implemented)")

    def list_files(self) -> List[str]:
        """
        List all files in the OneDrive app folder.
        """
        print("Listing files from OneDrive (not implemented)")
        return []
