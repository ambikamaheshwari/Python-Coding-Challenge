__author__ = 'Ambika'
import sys
import string

if sys.version_info[0] < 3:
    input = raw_input

# Function to get missing letters, sentence is string given by users
def get_missing_letters(sentence):
    #Converting alphabets to set
    alphabet = string.ascii_lowercase
    alphaset = set(alphabet)
    # Converting user input in lowercase,converting into set and sorting
    sentenceset = sorted(set(sentence.lower()))
    # comparing alphabet set and input sentence set
    notalpha = {x for x in alphaset if x not in sentenceset}
    if len(notalpha) == 0:
        return " "
    else:
        notalphastr = ''.join(list(sorted(notalpha)))
        return notalphastr
        
print(get_missing_letters(input('Sentence: ')))
