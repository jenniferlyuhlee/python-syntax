def print_upper_words(words):
    """pass in a list of words
    the function prints the words in upper-case"""

    for word in words:
        print (word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])



def print_upper_words2(words):
    """pass in a list of words
    the function prints the words in upper-case
    if it starts with 'e'"""

    for word in words:
        if (word.upper()[0]=='e'.upper()):
            print (word.upper())

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"])



def print_upper_words3(words, must_start_with):
    """pass in a list of words, and a set of letters
    the function prints the words in upper-case 
    if it starts with any of those letter"""

    for word in words:
        for letter in must_start_with:
            if (word[0]==letter):
                print (word.upper())


print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
