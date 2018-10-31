#A game with "word handling"

def first_line():
    return 'start'

word = {
        'direction':'north',
        'verb':'eat',
        'stop':'the',
        'noun':'bear',
        }

def scan():
    write = input('write something' )
    a = word.get(write)
    return a

