import subprocess
import sys

install_command = [sys.executable, "-m", "pip", "install", "chatgptmax"]
subprocess.check_call(install_command)

from chatgptmax import send

def test_pypi_installation():
    assert send("Hello", "This is a test") == ["Response 1", "Response 2"]

if __name__ == "__main__":
    test_pypi_installation()
