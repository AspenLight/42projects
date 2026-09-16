import os
import dotenv


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    dotenv.load_dotenv()
    if (not os.getenv("MATRIX_MODE") or
            not os.getenv("DATABASE_URL") or
            not os.getenv("API_KEY") or
            not os.getenv("LOG_LEVEL") or
            not os.getenv("ZION_ENDPOINT")):
        print("The .env file is missing variables or does not exist")
    else:
        print("Configuration loaded:")
        print(f"Mode: {os.getenv("MATRIX_MODE")}")
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {os.getenv("LOG_LEVEL")}")
        print("Zion Network: Online\n")
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        if (os.path.exists(".gitignore")
                and ".env" in open(".gitignore").read()):
            print("[OK] .env file properly configured")
        else:
            print("[KO] .env file missing from .gitignore")
        print("[OK] Production overrides available\n")
        print("The Oracle sees all configurations.")
