import sys
sys.path.append("./")
import pytest
from src.chatgptmax import clean, read_data, send

# Test the clean text function
def test_clean():
    text = "Check out this link: http://example.com and email me at test@example.com!"
    cleaned_text = clean.text(text)
    assert cleaned_text == "Checkoutthislinkandemailmeat"


# Test the clean stopwords function
def test_clean_stopwords():
    text = "This is a test to remove stopwords from the text."
    cleaned_text = clean.stopwords(text)
    assert cleaned_text == "This test remove stopwords from text."


# Test the read_data function
def test_read_data(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("This is a test file.")
    assert read_data(file) == "This is a test file."


# Test the clean_text_from_file function
def test_clean_text_from_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("This is a test to remove stopwords from the file.")
    cleaned_text = clean.text_from_file(file)
    assert cleaned_text == "This test remove stopwords from file."


# Test the send function
def test_send():
    prompt = "Summarize the following text for me:"
    text_data = "This is a test text to be summarized by ChatGPT."
    response = send(prompt, text_data)
    assert isinstance(response, list)
    assert len(response) > 0


# Test the send function with missing prompt
def test_send_missing_prompt():
    response = send()
    assert response == "Error: Prompt is missing. Please provide a prompt."


# Test the send function with missing data
def test_send_missing_data():
    prompt = "Summarize the following text for me:"
    response = send(prompt)
    assert response == "Error: Text data is missing. Please provide some text data."
