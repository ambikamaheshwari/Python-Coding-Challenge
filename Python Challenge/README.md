# Python-Zen-Challenge

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

Question 2

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
