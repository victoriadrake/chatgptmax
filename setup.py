from setuptools import setup, find_packages

setup(
    name="chatgptmax",
    version="0.1",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "openai",
        "tiktoken",
        "re"
    ],
    author="Victoria Drake",
    author_email="hello@victoria.dev",
    description="A module to interact with ChatGPT with extended input.",
    license="MIT",
    keywords="chatgpt openai",
    url="https://github.com/victoriadrake/chatgptmax/",
)
