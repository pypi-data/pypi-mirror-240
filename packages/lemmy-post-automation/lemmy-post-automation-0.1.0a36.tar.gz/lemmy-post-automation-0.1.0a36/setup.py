from setuptools import setup
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if __name__ == "__main__":
    setup(
        version="0.1.0-alpha.36",
        long_description=long_description,
        long_description_content_type='text/markdown'
    )
