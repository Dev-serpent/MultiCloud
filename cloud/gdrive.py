from typing import List
from cloud.base import CloudProvider


class GoogleDriveProvider(CloudProvider):
    """
    Cloud provider for Google Drive.
    """

    def __init__(self):
        self.service = None

    def login(self, credentials):
        """
        Authenticate with Google Drive using OAuth 2.0 credentials.
        """
        # from google.oauth2.credentials import Credentials
        # from googleapiclient.discovery import build
        #
        # creds = Credentials.from_authorized_user_info(info=credentials)
        # self.service = build('drive', 'v3', credentials=creds)
        print("Logging in to Google Drive (not implemented)")

    def upload(self, file_path: str, dest_filename: str) -> str:
        """
        Upload a file to Google Drive.
        """
        print(f"Uploading {file_path} to Google Drive as {dest_filename} (not implemented)")
        return f"gdrive:///{dest_filename}"

    def download(self, file_id: str, dest_path: str):
        """
        Download a file from Google Drive.
        """
        print(f"Downloading {file_id} from Google Drive to {dest_path} (not implemented)")

    def list_files(self) -> List[str]:
        """
        List all files in the Google Drive app folder.
        """
        print("Listing files from Google Drive (not implemented)")
        return []
