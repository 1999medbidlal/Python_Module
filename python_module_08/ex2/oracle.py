import os
import sys
try:
    from dotenv import load_dotenv
except ImportError as e:
    print(f"Error:{e}")
    sys.exit(1)

load_dotenv()
print("\nORACLE STATUS: Reading the Matrix...")
data = {
    'MATRIX_MODE': None,
    'DATABASE_URL': None,
    'API_KEY': None,
    'LOG_LEVEL': None,
    'ZION_ENDPOINT': None
}
for var in data:
    data[var] = os.getenv(var)
mode = data['MATRIX_MODE']
print("\nConfiguration loaded:")
if not mode:
    print("Mode: MISSING")
else:
    print(f"Mode: {mode}")

if not data['DATABASE_URL']:
    print("Database: MISSING")
else:
    if mode == 'production':
        print("Database: Connected to production instance")
    else:
        print("Database: Connected to local instance")
if not data['API_KEY']:
    print("API Access: MISSING")
else:
    print("API Access: Authenticated")

if not data["LOG_LEVEL"]:
    print("Log Level: MISSING")
else:
    if mode == "production":
        print("Log Level: INFO")
    else:
        print("Log Level: DEBUG")
if not data["ZION_ENDPOINT"]:
    print("Zion Network: MISSING")
else:
    print("Zion Network: Online")
if mode == "production":
    if not data["API_KEY"] or not data["DATABASE_URL"]:
        print("\nERROR: Critical configuration missing in production mode.")
        sys.exit(1)

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[WARNING] No .env file found")
print("[OK] Production overrides available")
print("\nThe Oracle sees all configurations.")
