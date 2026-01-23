WE ARE EXPERIENCING DATA LOSS ON MULTICLOUD PROJECT SO IT IS NOT READY , THANK YOU

MULTICLOUD
===========
PLEASE NOTE:
============

MULTICLOUD IS UNDER DEVELOPMENT AND IS HIGHLY EXPERMINTAL. WE ARE WORKING
ON V.1.1 WHICH IS TO BE USED PROPERLY AS AN ENCRPTION SOFTWARE BUT V.1.0
IS MAINLY EXPERMENTAL -W.G.

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
CURRENT STATUS (Dec 2025)
--------------------------------------------------

**NOTE:** The project currently has known issues with missing vendored
dependencies (`google-auth`, `selenium`). As a temporary workaround, several
cloud providers (`gdrive`, `mega`, `blomp`, `terabox`) have been disabled
in the code to allow the application to run.

The core file processing pipeline and the local user vault are functional.
The GUI can be launched, and user registration/login works.

--------------------------------------------------
GETTING STARTED
--------------------------------------------------

To run the application, use the `run.py` script. You can specify the
interface to use as a command-line argument:

   python3 run.py [interface]

Available interfaces are:
- `cli`: Command-line interface
- `tui`: Terminal user interface
- `gui`: Graphical user interface (recommended)

If no interface is specified, the application will default to the GUI.

A default user `testuser` with password `123` is created on first launch
for immediate testing.

--------------------------------------------------
USER MANAGEMENT
--------------------------------------------------

MultiCloud supports multiple users. Each user has their own set of
cloud accounts and backups.

You can register a new user or use the default `testuser`.

**Registration:**
- **CLI:** `python3 run.py cli register <username>`
- **GUI:** Enter a new username and password and click the "Register" button.

**Login:**
- **GUI:** Enter your username and password and click the "Login" button.

--------------------------------------------------
CLI USAGE
--------------------------------------------------

The command-line interface provides a scriptable way to interact with
MultiCloud.

**Commands:**

- `register <username>`: Register a new user.
- `backup <folder> -u <username> -p <provider1> ...`
- `restore <output> -u <username>`
- `list-providers`: List all available (and currently enabled) providers.

--------------------------------------------------
TUI USAGE
--------------------------------------------------

The terminal user interface provides an interactive, keyboard-driven way
to use MultiCloud. Launch with:

   `python3 run.py tui`

--------------------------------------------------
GUI USAGE
--------------------------------------------------

The graphical user interface is the recommended way to use MultiCloud.
Launch with:

   `python3 run.py gui`

You will be presented with a login window. You can log in as `testuser`
with password `123`, or register a new user.

Once logged in, the main application window will appear.

--------------------------------------------------
CLOUD PROVIDER CONFIGURATION
--------------------------------------------------

Cloud accounts can be managed directly through the GUI.

1.  From the main window, click "Cloud Accounts".
2.  In the Cloud Accounts window, click "Add Account".
3.  Enter a local name for the account (e.g., "My Personal Mega").
4.  Enter the provider name (e.g., `mega`, `dropbox`).
5.  A browser view will open within the application. Log in to your
    cloud account as you normally would.

The application will securely store the session information in your encrypted
vault. You do not need to manually handle tokens or credentials.

(Note: This is the intended workflow. The webview implementation is
currently a placeholder due to the dependency issues mentioned above).

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
