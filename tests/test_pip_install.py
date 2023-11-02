import subprocess
import sys

install_command = [sys.executable, "-m", "pip", "install", "chatgptmax"]
subprocess.check_call(install_command)

from chatgptmax.clean import stopwords

def test_pypi_installation():
    text = "This is a test to remove stopwords from the text."
    cleaned_text = stopwords(text)
    assert cleaned_text == "This test remove stopwords from text."

if __name__ == "__main__":
    test_pypi_installation()
