# conftest.py

from ex48 import parser, lexicon 
from ex48.parser import *
import pytest

@pytest.fixture
def wordlist_fix():
    return lexicon.scan('the princess kill bear')


@pytest.fixture
def parse_error_msg():
    return lexicon.scan('the the the the') 
# All the "the" is to NOT get a match.
