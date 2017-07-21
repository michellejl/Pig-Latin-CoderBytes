user_input = 'continue'

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def get_first_letter():
    first_letter = user_input[:1]
    return first_letter

def get_second_letter():
    second_letter = user_input[1:2]
    return second_letter

def is_letter_a_vowel(letter):
    if letter in vowels:
        return True
    else:
        return False

first_letter = get_first_letter()
second_letter = get_second_letter()
first = is_letter_a_vowel(first_letter)
second = is_letter_a_vowel(second_letter)

if first == True:
    # Rule 3
    print user_input + 'way'
elif second == False:
    # Rule 2
    print user_input[2:] + user_input[:2] + 'ay'
else:
    # Rule 3
    print user_input[1:] + user_input[:1] + 'ay'


# RULES
# 1. If a word starts with a consonant and a vowel, put the first letter of the word at the end of the word and add "ay."  Example: Happy = appyh + ay = appyhay

# 2. If a word starts with two consonants move the two consonants to the end of the word and add "ay." Example: Child = Ildch + ay = Ildchay

# 3. If a word starts with a vowel add the word "way" at the end of the word. Example: Awesome = Awesome +way = Awesomeway
