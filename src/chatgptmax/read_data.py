
def read_data(file):
    """
    Reads the content of a file and returns it as a string.

    Args:
    - file (str): The path to the file to be read.

    Returns:
    - str: The content of the file.
    """
    # Open the file and read the text
    with open(file, "r", encoding="UTF-8") as f:
        text = f.read()
    return text