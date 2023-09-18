# chatgptmax

[![PyPI Version](https://img.shields.io/pypi/v/chatgptmax)](https://pypi.org/project/chatgptmax/)
[![Python Version](https://img.shields.io/pypi/pyversions/chatgptmax)](https://pypi.org/project/chatgptmax/)
[![License](https://img.shields.io/pypi/l/chatgptmax)](https://github.com/victoriadrake/chatgptmax/blob/main/LICENSE)

A Python package for sending long input text to OpenAI's GPT models using message chunking.

## Installation

You can install `chatgptmax` using pip:

```bash
pip install chatgptmax
```

## Usage

Here's are basic usage examples of the `chatgptmax` module. This assumes you have an [OpenAI API key set up](/docs/set_up_openai_api_key.md) as an environment variable, `OPENAI_API_KEY`.

### Clean text with preprocessing

Suppose you have a file named `sample.txt` with the following content:

```txt
This is a sample text. It contains some stop words that should be removed. We will use the chatgptmax module to clean and process this text.
```

You can use the `clean_text_from_file` function to read and clean the text from this file:

```python
from chatgptmax import clean_text_from_file

# Specify the path to your file
file_path = "sample.txt"

# Clean and process the text from the file
cleaned_text = clean_text_from_file(file_path)

# Print the cleaned text
print(cleaned_text)
```

This code will read the content of `sample.txt`, remove common stopwords, and print the cleaned text:

```txt
"This sample text contains stop words removed. We chatgptmax module clean process text."
```

### Send lots of text to ChatGPT

You can use the `send` function to send a prompt along with a large amount of text data from a file to ChatGPT:

```python
from chatgptmax import send, read_data

# Define the path to your text file
file_path = "path_to_your_file.txt"

# Read the text data from the file
text_data = read_data(file_path)

# Define your prompt
prompt_text = "Summarize the following text for me:"

# Send the text data to ChatGPT for summarization
responses = send(prompt=prompt_text, text_data=text_data)

# Print ChatGPT's responses
for response in responses:
    print(response)

```

This code will send the cleaned text as text data to ChatGPT along with the prompt. ChatGPT will provide responses based on your prompt and text data.

Please make sure you have your [OpenAI API key properly set up](/docs/set_up_openai_api_key.md) as an environment variable or using a secret management service for this example to work.

## Documentation

For more information on how to use chatgptmax, please refer to the official [documentation](/docs/).

## Contributing

If you'd like to contribute to this project, please read our [Contribution Guide](CONTRIBUTING.md) for details on how to get started.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
