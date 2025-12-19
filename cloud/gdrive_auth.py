import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive.file']
CLIENT_SECRET_FILE = 'client_secret.json'

def get_gdrive_credentials():
    """
    Get Google Drive credentials using the OAuth 2.0 flow.
    """
    if not os.path.exists(CLIENT_SECRET_FILE):
        raise FileNotFoundError(
            f"'{CLIENT_SECRET_FILE}' not found. Please follow the instructions "
            "in the readme to create this file."
        )

    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)

    return {
        'token': creds.token,
        'refresh_token': creds.refresh_token,
        'token_uri': creds.token_uri,
        'client_id': creds.client_id,
        'client_secret': creds.client_secret,
        'scopes': creds.scopes
    }
