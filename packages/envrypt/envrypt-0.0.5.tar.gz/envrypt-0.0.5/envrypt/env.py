
import os
import dotenv
import binascii
from .strcrypt import decrypt

dotenv.load_dotenv()


def get(key, default=None):
    """Get environment variable from .env file.

    Parameters:
    ----------
    key : str
        The key to get the value for.
    default : str
        The default value to return if the key is not found.

    Returns:
    -------
    str
        The value of the key, or the default value if the key is not found.
    """
    value = os.getenv(key, default)
    if value is None:
        return value
    try:
        decrypted_value = decrypt(value)
        return decrypted_value
    except binascii.Error:
        print("Cannot decrypt `%s` value, please check your encryption key." % key)
        return value
