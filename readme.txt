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
INTERFACES
--------------------------------------------------

1) CLI (Command Line)
   - Scriptable
   - Automation friendly

   Example:
   multicloud backup /path/to/folder
   multicloud restore BACKUP_ID

2) TUI (Terminal UI)
   - Keyboard driven
   - Interactive menus
   - Works over SSH

   Launch:
   multicloud tui

3) Desktop GUI
   - Built using customtkinter
   - Dark mode
   - Mouse + keyboard

4) iPad GUI
   - Built using Pythonista UI
   - Touch friendly
   - Uses the same core engine

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
INSTALLATION (DESKTOP)
--------------------------------------------------

1) Clone repository
   git clone <repo_url>

2) Install dependencies
   pip install -r requirements.txt

3) Run
   python run.py

--------------------------------------------------
INSTALLATION (IPAD)
--------------------------------------------------

1) Install Pythonista
2) Copy the multicloud folder into Pythonista
3) Open run.py
4) Tap Run

--------------------------------------------------
CLI USAGE
--------------------------------------------------

Backup:
multicloud backup <folder>

Restore:
multicloud restore <backup_id>

List clouds:
multicloud clouds list

--------------------------------------------------
DISCLAIMER
--------------------------------------------------
This project is for learning and experimentation.
Always test restores before trusting important data.

--------------------------------------------------
LICENSE
--------------------------------------------------
MIT License
