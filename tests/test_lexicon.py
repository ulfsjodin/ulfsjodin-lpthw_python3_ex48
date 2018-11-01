
import pytest
from ex48 import lexicon 

#Same kind of test of directions as the Nose test in the book.
#@pytest.mark.skip(reason='not completed in ex48/test.py')
def test_directions():
    assert lexicon.scan('south') == [('direction', 'south')]
    result = lexicon.scan('north south east')
    assert result == [('direction', 'north'), 
                      ('direction', 'south'),
                      ('direction', 'east')]


#One can test all in one go with parametized test.
@pytest.mark.parametrize('one_in, two_out', [

        ('north',[('direction','north')]),
        ('south',[('direction','south')]),
        ('east',[('direction','east')]),
        ('down',[('direction','down')]),
        ('eat',[('verb','eat')]),
        ('go',[('verb','go')]),
        ('the',[('stop','the')]),
        ('in',[('stop','in')]),
        ('door',[('noun','door')]), 
        ('cabinet',[('noun','cabinet')]),
        ])
#@pytest.mark.skip(reason='not completed in ex48/test.py')
def test_params(one_in, two_out):
    assert lexicon.scan(one_in) == two_out

#Test to make sure the lexicon is complete.
def test_lexikon2():
    complete_dict = lexicon.lexicon
    assert complete_dict == {
        'north':'direction',
        'south':'direction',
        'east':'direction',
        'west':'direction',
        'down':'direction',
        'up':'direction',
        'left':'direction',
        'right':'direction',
        'back':'direction',
        'go':'verb',
        'stop':'verb',
        'kill':'verb',
        'eat':'verb',
        'the':'stop',
        'in':'stop',
        'of':'stop',
        'at':'stop',
        'it':'stop',
        'door':'noun',
        'bear':'noun',
        'princess':'noun',
        'cabinet':'noun',
        }
#Test to see that a string of number is converted to integers.
#@pytest.mark.skip(reason='not completed in ex48/test.py')
def test_number():
    test_num = lexicon.scan('1234')
    assert test_num == [('number', 1234)]

#I found 'poppycock' on Google translate :-)
poppycock = 'anything_not_in_lexicon'

#Test to see that a word not in lexicon returns None.
#@pytest.mark.skip(reason='not completed in ex48/test.py')
def test_lexikon():
    blunder = lexicon.lexicon.get(poppycock)
    assert blunder == None

#Test to see a error message occurs
#@pytest.mark.skip(reason='not completed in ex48/test.py')
def test_raise_error():
    error_msg = 'error'
    not_in_dict = lexicon.scan(poppycock)
    assert not_in_dict == [(error_msg, poppycock)]
