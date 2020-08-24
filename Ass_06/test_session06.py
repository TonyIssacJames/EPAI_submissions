import pytest
import random
import session_06
import os


#Read Me Tests
def test_readme_exists():
    assert os.path.isfile("README.md"), "README is not there"

