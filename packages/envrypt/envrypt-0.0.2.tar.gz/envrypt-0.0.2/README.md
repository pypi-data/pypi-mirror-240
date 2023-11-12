![envrypt logo](./envrypt-logo.jpg)

# Envrypt

Envrypt is a Python tool/library designed to secure environment variables by encrypting them both in disk and memory. It works with `dotenv` and provides a simple interface to access encrypted environment variables in your program.

Envrypt uses a simple XOR encryption mechanism. While XOR is relatively basic and not recommended for high-security requirements, it can be sufficient for obfuscating environment variables in scenarios where the threat model allows for it. Note that the XOR encryption strength highly depends on the length and randomness of the key. Due to the simplicity of the algorithm, it is important to maintain the secrecy of the encryption key for the encryption to remain effective.

## Installation

To install `envrypt`, use pip:

```
pip install envrypt
```

## Usage

### Step 1: Create .env.raw file

Create a file named `.env.raw`. This file should contain the real, unencrypted values of your environment variables.
Example:

```
MY_SECRET_KEY=123456
ETHEREUM_PRIVATE_KEY=d3514e92efab55576e3ca338795428fabb8ce14a01e5fe2140619e5b0b30c8ae
ENVRIPT_SECRET_TEXT="Secret text"

REGULAR_VAR=12345
BASE_URL=https://example.com/
```

### Step 2: Compile .env.raw file

Compile the `.env.raw` file using `python -m envrypt.encrypt` command. This command will encrypt the variable values with a key where the name ends with `_KEY` or begins with `ENVRIPT_`:

```
python -m envrypt.encrypt > .env
```

Example output:

```
SECRET_KEY=XEtAUVZE

# encrypted
ETHEREUM_PRIVATE_KEY=CUpGVFcXXEYOAxgPTEZQVEQARwgESl5BRFxWRldMDQQbD0EQAFJGBERaAEwLHEFUV0JTRVIATA9JEVZTEV0VDg==

# encrypted
ENVRIPT_NEXTJS_VAR=PhwQFwYGRQAOHQ0=

REGULAR_VAR=12345
BASE_URL=https://example.com/
```

### Step 3: Load encrypted variables in your program

In your Python program, you can load the encrypted variables using `dotenv` as usual, and read it using `envrypt`.

Example:

```python
import dotenv
from envrypt import env

# load the `.env` file using `dotenv.load_dotenv()`:
dotenv.load_dotenv()

# Finally, you can access the encrypted variables using the `env.get()` method:
env.get("MY_SECRET_KEY")
```

The `env.get()` method will automatically decrypt the variable during runtime, ensuring that the variables are secure in memory and only decrypted when needed.

Note: Make sure to keep the `.env.raw` and `.env` files secure and do not commit them to version control systems.

When the application starts, it will prompt the user to input the encryption key in the terminal:

```bash
$ python hello.py
For dev convenience, you can create a .envrypt file with a single line containing the encryption key.
Enter encryption key:
```

You should only need to input the encryption key once, and the key will remain in memory for the duration of the application’s runtime.

For development convenience or scenarios where you don’t want the interactive terminal interruption, you can store the encryption key on disk:
Create a `.envrypt` file in the same directory as your `.env` files:

```
# .envrypt
TheEncryptionKeyYouWantToUse
```

Note: Storing encryption keys on disk presents inherent risks and should be managed carefully, particularly in production environments.

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/anvie/envrypt).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


[] Robin Syihab ([@anvie](https://x.com/anvie))
