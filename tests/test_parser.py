from ex48 import parser, lexicon
from ex48.parser import *
import pytest

@pytest.fixture
def wordlist_fix():
    return lexicon.scan('the princess kill bear')

@pytest.fixture
def wordlist_error_fix():
    return lexicon.scan('the bear princess kill') # Sentence with Yoda 'grammar' 

@pytest.fixture
def parse_error_msg():
    return lexicon.scan('the the the the') # Sentence with Yoda 'grammar' 

def test_Sentence():
    a = Sentence(('noun','princess'), ('verb', 'kill'), ('noun', 'bear'))
    assert a.subject == 'princess'
    assert a.verb == 'kill'
    assert a.object == 'bear'

def test_peek(wordlist_fix):
    assert parser.peek(wordlist_fix) ==  'stop'  

def test_peek_empty():
    wordlist = []
    assert parser.peek(wordlist) == None

def test_match(wordlist_fix):
    w = wordlist_fix.pop(0)
    assert w == ('stop','the') # Popped off from wordlist_fix
    x = wordlist_fix
    assert x == [('noun', 'princess'),('verb', 'kill'), ('noun', 'bear')]
    # Remainder of wordlist_fix

def test_skip(wordlist_fix):
    assert peek(wordlist_fix) == 'stop'

def test_parse_verb(wordlist_fix):
    skip(wordlist_fix, 'stop')
    match(wordlist_fix, 'expecting') 
    # "expecting" can be replace to anything to make peek(wordlist_fix) equal to 'verb'
    # otherwise it only equals 'noun'.  (correct ?) 
    assert peek(wordlist_fix) == 'verb'

def test_object(wordlist_fix):
    skip(wordlist_fix, 'stop')
    next_word = peek(wordlist_fix)
    assert next_word == 'noun'

def test_subject(wordlist_fix):
    skip(wordlist_fix, 'stop')
    next_word = peek(wordlist_fix)
    assert next_word == 'noun'
    skip(wordlist_fix, 'verb')
    next_word = peek(wordlist_fix)
    assert next_word == 'noun'

def test_parse_sentence(wordlist_fix):
    subj = parse_subject(wordlist_fix)
    verb = parse_verb(wordlist_fix)
    obj = parse_object(wordlist_fix)
    assert subj == ('noun', 'princess')
    assert verb == ('verb', 'kill')
    assert obj == ('noun', 'bear')

def test_error_message_parse_verb(parse_error_msg):
    with pytest.raises(ParserError) as excinfo:
        parse_verb(parse_error_msg)
    assert str(excinfo.value) == 'Expected a verb next.'

def test_error_message_parse_subject(parse_error_msg):
    with pytest.raises(ParserError) as excinfo:
        parse_subject(parse_error_msg)
    assert str(excinfo.value) == 'Expected a verb next.'

def test_error_message_parse_object(parse_error_msg):
    with pytest.raises(ParserError) as excinfo:
        parse_object(parse_error_msg)
    assert str(excinfo.value) == 'Expected a noun or direction next.'
