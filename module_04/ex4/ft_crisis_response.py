def crisis_handler(file_name):
    if file_name == "standard_archive.txt":
        print(f"\nROUTINE ACCESS: Attempting access to '{file_name}'...")
    else:
        print(f"\nCRISIS ALERT: Attempting access to '{file_name}'...")
    try:
        with open(f"{file_name}", "r") as file:
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
crisis_handler('lost_archive.txt')
crisis_handler('classified_vault.txt')
crisis_handler('standard_archive.txt')
print("\nAll crisis scenarios handled successfully. Archives secure.")
