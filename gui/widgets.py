def format_accounts(accounts):
    if not accounts:
        return "No accounts configured."
    return "\n".join(f"{a['name']} ({a['provider']})" for a in accounts)
