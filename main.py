'''In Sweden, there is a simple child’s game similar to Pig Latin called Rovarspr ¨ aket (Robbers Lan- ˚
guage).
In this version of Rovarspraket, every consonant is replaced by three letters, in the following ˚
order:
• the consonant itself;
• the vowel closest to the consonant in the alphabet (e.g., if the consonant is d, then the closest
vowel is e), with the rule that if the consonant falls exactly between two vowels, then the
vowel closer to the start of the alphabet will be chosen (e.g., if the consonant is c, then the
closest vowel is a);
• the next consonant in the alphabet following the original consonant (e.g., if the consonant is
d, then the next consonant is f) except if the original consonant is z, in which case the next
consonant is z as well.
Vowels in the word remain the same. (Vowels are a, e, i, o, u and all other letters are consonants.)
Write a program that translates a word from English into Rovarspr ¨ aket. ˚

Input Specification
The input consists of one word entirely composed of lower-case letters. There will be at least one
letter and no more than 30 letters in this word.
'''


def rovarsprak(word):
    vowels = 'aeiou'
    rovar_word = ''
    for char in word:
        if char not in vowels:
            next_consonant = chr(ord(char) + 1)
            if char == 'z':
                next_consonant = 'z'
            closest_vowel = min([v for v in vowels if v >= char], default=vowels[0])
            rovar_word += char + closest_vowel + next_consonant
        else:
            rovar_word += char
    return rovar_word

word = input()
print(rovarsprak(word))


def rovarsprak(word):
    vowels = 'aeiou'
    rovar_word = ''
    for char in word:
        if char not in vowels:
            next_consonant = chr(ord(char) + 1)
            if char == 'z':
                next_consonant = 'z'
            closest_vowel = min([v for v in vowels if v >= char], default=vowels[0])
            rovar_word += char + closest_vowel + next_consonant
        else:
            rovar_word += char
    return rovar_word

word = input()
print(rovarsprak(word))