from pathlib import Path
from os import getenv

# from base import load_env
from dotenv import load_dotenv

ROOT_DIR = Path.cwd().parent
print(ROOT_DIR)
load_dotenv(ROOT_DIR.joinpath(".env"))

settings = {
    "OPENAI_KEY": getenv("OPENAI_KEY"),
}
print(settings)
