from dotenv import load_dotenv


def load_environment() -> None:
    """
    Load environment variables from .env file.
    """
    load_dotenv()
