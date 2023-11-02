# chatgptmax Documentation

This module provides tools for cleaning text, removing stopwords, reading text from files, and sending text data to ChatGPT via the OpenAI API.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Cleaning Text](#cleaning-text)
  - [Removing Stopwords](#removing-stopwords)
  - [Reading Data from Files](#reading-data-from-files)
  - [Sending Text to ChatGPT](#sending-text-to-chatgpt)
- [Contributing](#contributing)

## Installation

Before using the `chatgptmax` module, make sure you have the necessary dependencies installed, including OpenAI's Python library and `tiktoken`. You will also need to set up your OpenAI API key. Follow the instructions in the [OpenAI API documentation](https://platform.openai.com/docs/guides/authentication) for more information on setting up your API key.

You can install the required dependencies using `pip`:

```sh
pip install -r requirements.txt
```

If you plan to contribute, please also install and use `black` to format the files:

```sh
pip install --upgrade black
```

## Usage

To use the `chatgptmax` module, follow these steps:

1. Sign up for ChatGPT and create a secret API key. More information here: https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key
2. Ensure your key is present in the environment variable `OPENAI_API_KEY`. For instructions, read [Set up your OpenAI API key](./set_up_openai_api_key.md)
3. Import and use `chatgptmax` as shown in the examples below.

### Cleaning Text

The `clean.text` method can be used to clean text by removing URLs, email addresses, non-letter characters, and extra whitespace.

```python
from chatgptmax.clean import text

# Clean the input text
just_letters = text("Your input text goes here.")

# Print the cleaned text
print(just_letters)
```

### Removing Stopwords

The `clean.stopwords` method removes common stopwords from the provided text.

```python
from chatgptmax.clean import stopwords

# Remove stopwords from the input text
text_without_stopwords = stopwords("This is a sample text. It contains some stop words that should be removed. We will use the chatgptmax module to clean and process this text.")
```

### Reading Data from Files

The `read_data` method reads the content of a file and returns it as a string.

```python
from chatgptmax import read_data

# Specify the path to your file
file_path = "path_to_your_file.txt"

# Read the content of the file
file_content = read_data(file_path)
```

### Sending Text to ChatGPT

The `send` method sends text data to ChatGPT for processing. It can handle large text by splitting it into chunks.

```python
from chatgptmax import send

# Define your prompt and text data
prompt_text = "Summarize the following text for me:"
text_data = cleaned_text  # Use the cleaned text

# Send the text data to ChatGPT for summarization
responses = send(prompt=prompt_text, text_data=text_data)

# Print ChatGPT's responses
for response in responses:
    print(response)
```

## Contributing

If you would like to contribute to the `chatgptmax` module, please follow these steps:

1. Fork the repository to your GitHub account.
2. Create a new branch for your contributions.
3. Make your changes and improvements.
4. Commit your changes with clear and concise commit messages.
5. Push your changes to your forked repository.
6. Open a pull request against the `master` branch of the original repository.

For more details, see [CONTRIBUTING.md](CONTRIBUTING.md).

We welcome contributions and suggestions to improve this module.

Happy coding!
