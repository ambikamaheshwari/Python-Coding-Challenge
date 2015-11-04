# Python-Challenge

Question 1

Create a method print_github_graph which takes a string parameter,
search_term,

performs a “Users Search” using the GitHib’s API’s search function

(https://developer.github.com/v3/users/) and returns a string that
represents an

ASCII graph of the letter frequency of a GitHub API query.

Your submission should be a single file, which must contain the method

print_github_graph(search_term).

For example,

print_github_graph(search_term=”barack”)

would result in the following call being made:

https://api.github.com/search/users?q=barack

and, GitHub would return many results that look like:

{login: "PresidentObama", id: 10196880, avatar_url:

"https://avatars.githubusercontent.com/u/10196880?v=3",

url: "https://api.github.com/users/PresidentObama",

:

type: "User",

score: 43.27139}

Sort over the results by login attribute. Using up to five Users’ login
attributes (or fewer if API

results contain fewer Users), please output 26 letters of the alphabet
and “other”)

(ignoring upper or lower case) and an ‘*’ for each time the letter or
non letter characters that appear

in the name attribute, each separated by a newline.
____________________________________________________________________________________________________________
Problem 2

The sentence "A quick brown fox jumps over the lazy dog" contains every
single letter in the

alphabet. Such sentences are called pangrams. You are to write a method

get_missing_letters, which takes a string, sentence, and returns a
string with all the

letters it is missing (which prevent it from being a pangram). You
should ignore the case of the

letters in sentence, and your return should be all lower case letters,
in alphabetical order.

Your submission should be a single file which must contain the method

get_missing_letters(sentence).

Examples: (Note: the double quotes should not be considered part of the
input or output strings.)

1) "A quick brown fox jumps over the lazy dog"

Returns: ""

(This sentence contains every letter)

2) "A slow yellow fox crawls under the proactive dog"

Returns: "bjkmqz"

3) "Lions, and tigers, and bears, oh my!"

Returns: "cfjkpquvwxz"

4) ""

Returns: "abcdefghijklmnopqrstuvwxyz"

___________________________________________________________________________________________________________________-
Problem 3

You are to write a program that takes a list of strings containing integers and words and returns a sorted version of the list. 
The goal is to sort this list in such a way that all words are in alphabetical order and all integers are in numerical order. Furthermore, if the nth element in the list is an integer it must remain an integer, and if it is a word it must remain a word. 
In addition, the strings and integers may contain characters that are ascii symbols that neither belong to letter set nor digit set (i.e. "#", "%", ";", etc). You are required to remove them during the process so that the output will contain only letters or digits. For example, if a string is "sym*bo+l", the output should be "symbol". If an integer is "12%3", the output should be "123".
You don't have to worry about handling the following case: 
Strings or integers that contain only non-letter-non-digit characters, like "^!?", "&", etc. We will not test your program with this.

The input will be a file includes a single, possibly empty, line containing a space-separated list of strings to be sorted. Words will not contain spaces, will contain upper-case, lower-case letters a-z and maybe non-letter-non-digit characters. Integers will be in the range -999999 to 999999, and might also contain non-letter-non-digit characters. 
The program must be printed into a file named "result.txt". The content of the file is the list of strings, sorted per the requirements above. Strings must be separated by a single space, with no leading space at the beginning of the line or trailing space at the end of the line. 

The program should take the input file name as the first argument, output file as the second argument:

	root:#  ./listSorting.py <path-to-input-file>/list.txt <path-to-output-file>/result.txt 

EG: car 10 truck 4 2 bus

Output: bus 2 car 4 10 truck
