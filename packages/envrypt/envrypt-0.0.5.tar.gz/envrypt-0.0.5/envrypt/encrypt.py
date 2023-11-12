#!/usr/bin/env python
#
# This script will encrypt all environment variables in .env file
#
import sys
import os
import dotenv

RAW_ENV_FILE = os.path.join(os.getcwd(), ".env.raw")

from .strcrypt import encrypt

def main():
    print("# Envrypt managed environment file.\n")
    
    # check if .env.raw exists
    if not os.path.exists(RAW_ENV_FILE):
        print(f"No `.env.raw` file found. Please create one first.")
        sys.exit(1)

    for k, v in dotenv.dotenv_values(dotenv_path=RAW_ENV_FILE).items():
        # only encrypt key that ends with _KEY
        if not (k.endswith("_KEY") or k.startswith("ENVRIPT_")):
            print(f"{k}={v}")
            continue

        print(f"# encrypted")
        encrypted = encrypt(v)
        print(f"{k}={encrypted}\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
