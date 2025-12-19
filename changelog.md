# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-12-19

### Added
- **Cloud Provider Framework:**
    - Created a `CloudProvider` abstract base class (`cloud/base.py`) to define a common interface for all cloud providers.
    - Added placeholder implementations for AWS, Dropbox, Google Drive, OneDrive, and WebDAV in the `cloud/` directory.
    - Implemented a `CloudManager` (`core/cloud_manager.py`) to dynamically load and manage cloud providers.
- **Secure Login System:**
    - Upgraded password hashing to use `argon2` in `vault/auth.py` for enhanced security.
    - Introduced a `User` model (`vault/models.py`) to store user data, including associated cloud accounts.
    - Created a `UserManager` (`vault/user_manager.py`) to handle user creation, authentication, and management.
- **Cloud Account Management:**
    - Added API functions (`add_cloud_account`, `list_cloud_accounts`, `remove_cloud_account`) to `core/api.py`.
    - Implemented cloud account management methods in `vault/user_manager.py`.
    - Added CLI commands (`cloud-add`, `cloud-list`, `cloud-remove`) to `cli/cli.py`.
    - Implemented Google Drive OAuth 2.0 authentication flow in CLI (`cloud/gdrive_auth.py`).
    - Added "Cloud Accounts" menu to TUI with list functionality.
    - Implemented "Cloud Accounts" window in GUI with add, list, and remove functionality.
- **Configuration Management:**
    - Added a `config.ini` file for centralized application settings.
    - Implemented a `core/config.py` module to read and write configuration settings.
- **Comprehensive Logging:**
    - Implemented a logging system in `core/logging.py` to log events to a file and the console.
    - Integrated logging into `core/api.py` to track important application events and errors.
- **User Interfaces:**
    - **CLI:** Added `register` and `login` commands, and a `--providers` option for the `backup` command.
    - **TUI:** Refactored into a screen-based architecture with a login screen and main menu.
    - **GUI:** Implemented a login window and a main application window for the desktop GUI. Added a placeholder iPad GUI.
- **`.gitignore`:** Created a `.gitignore` file to exclude IDE-specific files, Python cache, and other temporary files.

### Changed
- **Project Structure:**
    - Refactored the project structure to align with `filesys.txt`.
    - Renamed `core/providers` to `cloud`.
    - Renamed `core/cloud.py` to `cloud/base.py`.
    - Renamed `readme.md` to `readme.txt`.
- **API (`core/api.py`):**
    - Updated the API to be user-aware, with `backup_folder` and `restore_latest` now requiring a `User` object.
    - Added `register_user` and `login` functions.
    - Updated to expose cloud account management functions.
- **`run.py`:**
    - Updated to use `argparse` for interface selection (CLI, TUI, GUI).
    - Corrected all interface imports and function calls.
- **`plat.py` (formerly `platform.py`):**
    - Removed the `available_interfaces` function as it is no longer used.
- **`readme.txt` (formerly `readme.md`):**
    - Updated the installation instructions to reflect the vendored dependency model.
    - Added detailed usage guides for CLI, TUI, and GUI, user management, cloud provider configuration, and troubleshooting.
- **`cli/cli.py`:**
    - Updated to include cloud account management commands and Google Drive OAuth.
- **`tui/screens.py`:**
    - Updated with `CloudAccountsScreen` and `MainScreen` modifications.
- **`tui/tui.py`:**
    - Updated to integrate `CloudAccountsScreen`.
- **`gui/gui_desktop.py`:**
    - Updated with `CloudAccountsWindow` and main GUI modifications.

## [0.1.0] - 2025-12-18

### Added
- Initial project structure with vendored dependencies.
- Core functionality for backup and restore to a local vault.
- Basic CLI, TUI, and GUI implementations.
