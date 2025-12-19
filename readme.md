MultiCloud
===========

MultiCloud is a learning-focused, secure, multi-cloud backup system designed for:
- Arch / Linux terminal users (CLI-first)
- iPad users (GUI mode) who want an easy homelab-style cloud storage setup

The same core logic powers both modes.

--------------------------------
CORE FEATURES
--------------------------------
- Folder backup and restore
- Automatic compression and splitting
- Encrypted storage (client-side)
- Multi-cloud support (via adapters)
- Secure credential vault
- CLI for power users
- GUI for beginners (iPad-friendly)

--------------------------------
RUNNING MULTICLOUD
--------------------------------

From the project root:

    python run.py

The program will detect your platform and launch:
- CLI (Linux / terminal)
- GUI (iPad / touch-first environment)

--------------------------------
CLI GUIDE (ARCH / LINUX)
--------------------------------

All CLI commands are run through:

    python run.py <command>

---- Backup a folder ----

    python run.py backup <folder>

Example:
    python run.py backup ~/Documents

---- Restore a backup ----

    python run.py restore <output_dir> <chunk1> <chunk2> ...

Example:
    python run.py restore restored/ backup.part0 backup.part1

---- Add a cloud account ----

    python run.py vault-add --name <name> --provider <provider> --access-key <key> --secret-key <secret>

Example:
    python run.py vault-add --name myaws --provider aws --access-key ABC --secret-key XYZ

---- List stored cloud accounts ----

    python run.py vault-list

--------------------------------
VAULT SECURITY
--------------------------------

- One master password protects all credentials
- Credentials are encrypted on disk
- Passwords are never stored in plaintext
- Hashing + encryption are handled locally

--------------------------------
IPAD MODE (BEGINNER)
--------------------------------

On iPad, MultiCloud runs in GUI mode and provides:
- Button-based backup and restore
- Simple vault setup
- No terminal knowledge required

This mode is intended for learning and light usage.

--------------------------------
PROJECT STRUCTURE
--------------------------------

See filesys.txt for the full directory layout.

--------------------------------
DISCLAIMER
--------------------------------

This project is for learning, experimentation, and personal use.
Not intended to replace enterprise backup solutions.
