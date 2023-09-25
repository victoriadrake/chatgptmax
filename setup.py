from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="chatgptmax",
    version="1.0.2",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "openai",
        "tiktoken"
    ],
    author="Victoria Drake",
    author_email="hello@victoria.dev",
    description="Take large input or read a file and send it in chunks to ChatGPT.",
    license="MIT",
    keywords="chatgpt openai",
    url="https://github.com/victoriadrake/chatgptmax/",
)
