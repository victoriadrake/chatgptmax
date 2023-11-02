import re
from chatgptmax.read_data import read_data

def text(text):
    """
    Cleans the provided text by removing URLs, email addresses, non-letter characters, and extra whitespace.

    Args:
    - text (str): The input text to be cleaned.

    Returns:
    - str: The cleaned text.
    """
    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # Remove everything that's not a letter (a-z, A-Z)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove whitespace, tabs, and new lines
    text = "".join(text.split())

    return text

def stopwords(text: str) -> str:
    """
    Removes common stopwords from the provided text.

    Args:
    - text (str): The input text from which stopwords should be removed.

    Returns:
    - str: The text with stopwords removed.
    """
    stopwords = [
        "a",
        "an",
        "and",
        "at",
        "but",
        "how",
        "in",
        "is",
        "on",
        "or",
        "the",
        "to",
        "what",
        "will",
    ]
    tokens = text.split()
    clean_tokens = [t for t in tokens if not t in stopwords]
    return " ".join(clean_tokens)


def text_from_file(file):
    """
    Reads the content of a file, cleans it by removing stopwords, and returns the cleaned text.

    Args:
    - file (str): The path to the file whose content should be cleaned.

    Returns:
    - str: The cleaned content of the file or an error message if the file could not be read.
    """
    try:
        text = read_data(file)
    except:
        return "Error: could not read your file."
    return stopwords(text)