MULTICLOUD
===========

MultiCloud is a secure, cross-platform, multi-provider storage system.
It packages folders, encrypts them, splits them into chunks, and distributes
those chunks across multiple cloud providers.

This project supports:
- CLI (command mode)
- TUI (terminal UI)
- Desktop GUI (customtkinter)
- iPad GUI (Pythonista / Pyto)

--------------------------------------------------
CORE CONCEPT
--------------------------------------------------
Folder -> Package -> Encrypt -> Split -> Hash -> Upload
Restore -> Download -> Verify -> Reassemble -> Decrypt -> Unpack

Cloud providers never see plaintext data.

--------------------------------------------------
SECURITY MODEL
--------------------------------------------------
- AES-256-GCM encryption
- Argon2id key derivation
- SHA-256 integrity checks
- Encrypted credential vault
- Zero-trust cloud providers
- No plaintext secrets stored

--------------------------------------------------
PLATFORM SUPPORT
--------------------------------------------------

Desktop:
- Linux
- macOS
- Windows
- Python 3.10+

iPad:
- Pythonista (recommended)
- Pyto

Platform detection is automatic.

--------------------------------------------------
DEPENDENCIES
--------------------------------------------------

This project uses a "vendored" dependency model. All required third-party
libraries are included in the `vendor/` directory. There is no need to
install any packages using `pip` or other package managers.

The project is pre-configured to find and use these libraries automatically.

--------------------------------------------------
GETTING STARTED
--------------------------------------------------

To run the application, use the `run.py` script. You can specify the
interface to use as a command-line argument:

   python run.py [interface]

Available interfaces are:
- `cli`: Command-line interface
- `tui`: Terminal user interface
- `gui`: Graphical user interface

If no interface is specified, the application will default to the GUI on
desktop platforms and the iPad GUI on iPad.

--------------------------------------------------
USER MANAGEMENT
--------------------------------------------------

MultiCloud now supports multiple users. Each user has their own set of
cloud accounts and backups.

You must register a user before you can use the application.

**Registration:**
- **CLI:** `python run.py cli register <username>`
- **GUI:** Enter a username and password and click the "Register" button.
- **TUI:** (Not yet implemented)

**Login:**
- **CLI:** The `backup` and `restore` commands require a username. You will be
  prompted for your password.
- **GUI:** Enter your username and password and click the "Login" button.
- **TUI:** Enter your username and password on the login screen.

--------------------------------------------------
CLI USAGE
--------------------------------------------------

The command-line interface provides a scriptable way to interact with
MultiCloud.

**Commands:**

- `register <username>`: Register a new user.
- `login <username>`: (Not a direct command) Used with `backup` and `restore`.
- `backup <folder> -u <username> -p <provider1> [<provider2> ...]`
    - Back up a folder for the specified user.
    - You must specify at least one cloud provider to use.
- `restore <output> -u <username>`
    - Restore the latest backup for the specified user.
- `list-providers`: List all available cloud providers.
- `list`: List all files in the local vault.
- `info`: Show information about the local vault.

**Example:**

1. Register a new user:
   `python run.py cli register myuser`

2. Back up a folder:
   `python run.py cli backup /path/to/my/folder -u myuser -p aws dropbox`

3. Restore a backup:
   `python run.py cli restore /path/to/restore/location -u myuser`

--------------------------------------------------
TUI USAGE
--------------------------------------------------

The terminal user interface provides an interactive, keyboard-driven way
to use MultiCloud.

Launch the TUI with:

   `python run.py tui`

You will be prompted to log in. Once logged in, you can use the arrow keys
and Enter to navigate the menus.

**Features:**
- Login screen
- Main menu with options for backup, restore, etc.
- (Backup and restore functionality is not yet fully implemented in the TUI)

--------------------------------------------------
GUI USAGE
--------------------------------------------------

The graphical user interface provides a user-friendly, mouse-driven way
to use MultiCloud.

Launch the GUI with:

   `python run.py gui`

You will be presented with a login window. You can either log in as an
existing user or register a new user.

Once logged in, the main application window will appear, with buttons for
the various functions.

**Features:**
- Login and registration window.
- Main window with buttons for backup, restore, etc.
- (Provider selection for backups is not yet implemented in the GUI)

--------------------------------------------------
CLOUD PROVIDER CONFIGURATION
--------------------------------------------------

To use cloud providers, you must first add your credentials to your user
account. This functionality is not yet exposed in the UI, but you can
add accounts by manually editing the `vault.sec` file (not recommended).

The structure of a cloud account in the `vault.sec` file is as follows:

```json
{
  "users": {
    "myuser": {
      "username": "myuser",
      "password_hash": "...",
      "cloud_accounts": [
        {
          "name": "My AWS Account",
          "provider": "aws",
          "credentials": {
            "access_key": "YOUR_AWS_ACCESS_KEY",
            "secret_key": "YOUR_AWS_SECRET_KEY"
          }
        },
        {
          "name": "My Dropbox Account",
          "provider": "dropbox",
          "credentials": {
            "access_token": "YOUR_DROPBOX_ACCESS_TOKEN"
          }
        }
      ]
    }
  }
}
```

**NOTE:** The `vault.sec` file is encrypted. You would need to decrypt it,
edit it, and then re-encrypt it. A future version of MultiCloud will
provide a UI for managing cloud accounts.

--------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------

**Error: "Folder not found"**
- Make sure the folder you are trying to back up exists and you have the
  correct permissions to read it.

**Error: "Login failed"**
- Double-check your username and password.
- If you have forgotten your password, there is currently no way to recover
  it. You will need to create a new user.

**Error: "Provider not found"**
- Make sure you have spelled the provider name correctly.
- You can see a list of available providers with the `list-providers`
  command in the CLI.

**Error: "User has no cloud accounts configured"**
- You must configure at least one cloud account for your user before you
  can create a backup. See the "Cloud Provider Configuration" section.

--------------------------------------------------
DISCLAIMER
--------------------------------------------------
This project is for learning and experimentation.
Always test restores before trusting important data.

--------------------------------------------------
LICENSE
--------------------------------------------------
MIT License
