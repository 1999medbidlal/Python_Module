print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("\nInitiating secure vault access...")
print("Vault connection established with failsafe protocols")
print("\nSECURE EXTRACTION:")
try:
    with open("classified_data.txt", "r") as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"Error : {e}")
print("\nSECURE PRESERVATION:")
with open("classified_data.txt", "a") as file1:
    file1.write("\n[CLASSIFIED] New security protocols archived")
    print("[CLASSIFIED] New security protocols archived")
print("Vault automatically sealed upon completion")
print("\nAll vault operations completed with maximum security.")
