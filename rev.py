#!/usr/bin/env python

# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter
# words reversed (Just like the name of this Kata).
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spinWords(word_string):
    '''
    objective: reverse works of 5 or more char.
    parm: word_string  -- string to work on
    retun: rv_string   -- string with reversed words
    '''
    word_array = []
    wk_string = word_string
    str_list = wk_string.split(' ')
    for x in str_list:
        word_len = len(x)
        if word_len > 4:
            rv = (x[::-1])
            word_array.append(rv)
        else:
            word_array.append(x)

    s = ' '  #separator
    rv_string = s.join(word_array)
    return rv_string

def main():
    '''
    main method
    '''

    rw = spinWords("Hey fellow warriors")
    print rw
    print '==============================='
    rw = spinWords("This is a test")
    print rw
    print '==============================='
    rw = spinWords("This is another test")
    print rw 

if __name__ == "__main__": main()
