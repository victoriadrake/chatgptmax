# chatgptmax.py

import os
import openai
import tiktoken
import re

# Set up your OpenAI API key
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


def clean(text):
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


def clean_stopwords(text: str) -> str:
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


def clean_text_from_file(file):
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
    return clean_stopwords(text)


def send(
    prompt=None,
    text_data=None,
    chat_model="gpt-3.5-turbo",
    model_token_limit=8192,
    max_tokens=2500,
):
    """
    Send the prompt at the start of the conversation and then send chunks of text_data to ChatGPT via the OpenAI API.
    If the text_data is too long, it splits it into chunks and sends each chunk separately.

    Args:
    - prompt (str, optional): The prompt to guide the model's response.
    - text_data (str, optional): Additional text data to be included.
    - max_tokens (int, optional): Maximum tokens for each API call. Default is 2500.

    Returns:
    - list or str: A list of model's responses for each chunk or an error message.
    """

    # Check if the necessary arguments are provided
    if not prompt:
        return "Error: Prompt is missing. Please provide a prompt."
    if not text_data:
        return "Error: Text data is missing. Please provide some text data."

    # Initialize the tokenizer
    tokenizer = tiktoken.encoding_for_model(chat_model)

    # Encode the text_data into token integers
    token_integers = tokenizer.encode(text_data)

    # Split the token integers into chunks based on max_tokens
    chunk_size = max_tokens - len(tokenizer.encode(prompt))
    chunks = [
        token_integers[i : i + chunk_size]
        for i in range(0, len(token_integers), chunk_size)
    ]

    # Decode token chunks back to strings
    chunks = [tokenizer.decode(chunk) for chunk in chunks]

    responses = []
    messages = [
        {"role": "user", "content": prompt},
        {
            "role": "user",
            "content": "To provide the context for the above prompt, I will send you text in parts. When I am finished, I will tell you 'ALL PARTS SENT'. Do not answer until you have received all the parts.",
        },
    ]

    for chunk in chunks:
        messages.append({"role": "user", "content": chunk})

        # Check if total tokens exceed the model's limit and remove oldest chunks if necessary
        while (
            sum(len(tokenizer.encode(msg["content"])) for msg in messages)
            > model_token_limit
        ):
            messages.pop(1)  # Remove the oldest chunk

        response = openai.ChatCompletion.create(model=chat_model, messages=messages)
        chatgpt_response = response.choices[0].message["content"].strip()
        responses.append(chatgpt_response)

    # Add the final "ALL PARTS SENT" message
    messages.append({"role": "user", "content": "ALL PARTS SENT"})
    response = openai.ChatCompletion.create(model=chat_model, messages=messages)
    final_response = response.choices[0].message["content"].strip()
    responses.append(final_response)

    return responses
